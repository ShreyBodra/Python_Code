def eq(j1, j2, c):
    list1 = []
    min1 = []
    # To find all possible set (x,y) in range (-3,3)
    for x in range(-3, 4):
        for y in range(-3, 4):
            if j1 * x + j2 * y == c:
                list1.append((x, y))    #list1 = [(-1,2), (2,-2)]

    #find sum of absolute values of individual sets
    for i in range(len(list1)):
        min1.append(abs(list1[i][0]) + abs(list1[i][1]))     #min1 = [3 ,4]


    temp = min1.index(min(min1))
    if list1[temp][0] > list1[temp][1]:
        return 0
    return 1


def gcd(j1, j2, c):
    i = 2
    #checking if i is a factor of both or not
    while i <= min([j1, j2]):
        if j1 % i == 0 and j2 % i == 0:
            print("No solution")
            break
        i += 1

    if i == min([j1, j2]) + 1:
        print("solution exist")
        solve(j1, j2, c)


def solve(j1, j2, c):

    choice = eq(j1, j2, c)

    if choice == 0:
        j1,j2 = j2,j1

    x=0
    y=0

    while x != c:
        # fill second jug
        if y < j2 : 
            y = j2 
            print(x,y,f"\tFill up {j2} liters of jug ")

        # transfer rule
        if x+y <= j1:
            x = x + y
            y = 0
            print(x,y)

        # transfer rule
        if x+y >= j1:
            x1 = j1 - x
            y = y - x1
            x = j1
            print(x,y)

        # empty the jug
        if x>0 and y != 0 :
            x = 0
            print(x,y,f"\tEmpty {j1} liters of jug ")
        
        
        if x+y <= j1 and y>0:
            x = x + y
            y = 0
            print(x,y)

    print("Goal State is reached")




#Driver code
if __name__ == '__main__':
    j1 = int(input("Enter capacity of 1st jug: "))
    j2 = int(input("Enter capacity of 2nd jug: "))
    c = int(input("Enter the amount of water required: "))
    gcd(j1, j2, c)
