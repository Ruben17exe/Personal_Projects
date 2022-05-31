from connect_four import *
from colorama import Fore, init
init()



def two_ai_game(symbol_player):
    my_board = make_board()

    if symbol_player == "X":
        symbol_ia = "O"
    elif symbol_player == "O":
        symbol_ia = "X"

    while not game_is_over(my_board):
        print(Fore.GREEN + "{0} Turn".format(symbol_player) + Fore.WHITE)
        position = int(input("Select your new position: "))
        select_space(my_board, position, symbol_player)
        print_board(my_board)

        if not game_is_over(my_board):
            result = minimax(my_board, False, 4, -float("Inf"), float("Inf"), ia_evaluate_board)
            print(Fore.RED + "{0} Turn\n{1} selected ".format(symbol_ia, symbol_ia), str(result[1]) + Fore.WHITE)
            select_space(my_board, result[1], symbol_ia)
            print_board(my_board)
    if has_won(my_board, "X"):
        print("X won!")
    elif has_won(my_board, "O"):
        print("O won!")
    else:
        print("It's a tie!")


def my_evaluate_board(board):
    x_two_streak = 0
    o_two_streak = 0
    if has_won(board, "X"):
        return float("Inf")
    elif has_won(board, "O"):
        return -float("Inf")

    for col in range(len(board) - 1):
        for row in range(len(board[0])):
            if board[col][row] == "X" and board[col + 1][row] == "X":
                x_two_streak += 1
            elif board[col][row] == "O" and board[col + 1][row] == "O":
                o_two_streak += 1

    return x_two_streak - o_two_streak


print(Fore.YELLOW + "Welcome to connect four!!" + Fore.WHITE)
symbol_player = str(input("Choose your symbol: "))

two_ai_game(symbol_player)
