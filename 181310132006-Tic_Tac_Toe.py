'''
Name: Shrey Bodra
En. No. : 181310132006
'''

#-------------------------Tic Tac Toe-------------------------------


def sample_board():
    # Display sample board
    print("--------------Sample Board--------------")
    board1 = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(board1[7], "|", board1[8], "|", board1[9])
    print("---------")
    print(board1[4], "|", board1[5], "|", board1[6])
    print("---------")
    print(board1[1], "|", board1[2], "|", board1[3])


def user_choice():
    # Asking user to choose X or O
    # return: (X,O) or (O,X)
    choice = input("\n[Human]: Enter your choice (x/o): ").upper()
    if choice == "X":
        print("\n[Human] you have choosen X. You play first.")
        return "X", "O"
    else:
        print("\n[Human] you have selected O. So, [CPU] will play first.")
        return "O", "X"


def display_board():
    # return: Board containing Moves of user and cpu
    print()
    print(board[7], "|", board[8], "|", board[9])
    print("---------")
    print(board[4], "|", board[5], "|", board[6])
    print("---------")
    print(board[1], "|", board[2], "|", board[3])


def user_input():
    # take input from user 
    while True:
        inp = int(input("\nEnter your move [Human] : "))
        if board[inp] == " ":
            return inp
        else:
            print("Invalid move [Human]. It's already selected ")


def win_move(i,mark):
    # checking winning possibility for both user and cpu
    # and selecting move for cpu accordingly

    temp_board = list(board)
    temp_board[i] = mark
    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for win_place in winning_place:
        if temp_board[win_place[0]] == temp_board[win_place[1]] == temp_board[win_place[2]] == mark:
            return True
    return False


def cpu_input(Human, Cpu):

    # attacking move
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, Cpu):
            return i

    # defensive move
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, Human):
            return i

    # Highest chance for win move
    for i in [5, 1, 3, 7, 9, 2, 8, 6, 4]:
        if board[i] == ' ':
            return i


def win_check(Human,Cpu):
    # check weather any one has won or not

    win_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [3, 5, 7], [1, 5, 9]]
    for x in win_place:
        if board[x[0]] == board[x[1]] == board[x[2]] == Human:
            print("\n[Human] wins!!!")
            return False

        elif board[x[0]] == board[x[1]] == board[x[2]] == Cpu:
            print("\n[CPU] wins!!!")
            return False

    # draw condition
    if ' ' not in board:
        print("\nDraw........")
        return False

    return True


def play():
    global board
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    p = True
    sample_board()
    Human, Cpu = user_choice()    # selection of (x,o) by user

    while p:
        if Human == "X":                        #user goes first
            inp = user_input()
            board[inp] = Human
            display_board()
            p = win_check(Human, Cpu)

            if p:
                inp2 = cpu_input(Human, Cpu)
                board[inp2] = Cpu
                print("\n[CPU] played it's move ")
                display_board()
                p = win_check(Human, Cpu)
        else:
            inp3 = cpu_input(Human, Cpu)                # cpu goes first
            board[inp3] = Cpu
            print("\n[CPU] played it's move ")
            display_board()
            p = win_check(Human, Cpu)
            if p:
                inp4 = user_input()
                board[inp4] = Human
                display_board()
                p = win_check(Human, Cpu)


if __name__ == '__main__':
    play()