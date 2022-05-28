from tic_tac_toe_library import *
from copy import deepcopy
from random import randint


# We evaluate if we have finished the game
def game_is_over(board):
    return has_won(board, "X") or has_won(board, "O") or len(available_moves(board)) == 0


# We check the result of the game
def evaluate_board(board):
    if has_won(board, "X"):
        return 1
    elif has_won(board, "O"):
        return -1
    else:
        return 0


def minimax(input_board, is_maximizing):
    # We check if we have finished the game
    if game_is_over(input_board):
        return [evaluate_board(input_board), ""]
    best_move = ""
    if is_maximizing:
        best_value = -float("Inf")  # We should start best_value at something lower than the lowest possible value
        symbol = "X"
    else:
        best_value = float("Inf")  # We should start best_value at something higher than the highest possible value
        symbol = "O"
    for move in available_moves(input_board):
        new_board = deepcopy(input_board)  # Board copy
        select_space(new_board, move, symbol)  # We move tab
        # Match Result: x_win, o_win, draw
        hypothetical_value = minimax(new_board, not is_maximizing)[0]
        if is_maximizing and hypothetical_value > best_value:
            best_value = hypothetical_value
            best_move = move
        if not is_maximizing and hypothetical_value < best_value:
            best_value = hypothetical_value
            best_move = move
    return [best_value, best_move]  # [Game Result, Tile Position]


new_game = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]


def start_x(position):
    select_space(new_game, position, "X")
    print_board(new_game)

    select_space(new_game, minimax(new_game, False)[1], "O")
    print_board(new_game)


def start_o():
    select_space(new_game, randint(1, 9), "X")
    print_board(new_game)

    position = int(input("Select your position: "))
    select_space(new_game, position, "O")
    print_board(new_game)


# Always start the X symbol
print("Welcome to Tic Tac Toe, the Game!!")
print("The symbol 'X' goes first, 'O' goes second")
player = str(input("Which one do you want: "))

loop = True
while loop:
    if player == "X":
        position = int(input("Select your position: "))
        start_x(position)
        while minimax(new_game, True)[0] == 0:
            position = int(input("Select your position: "))
            select_space(new_game, position, "X")
            print_board(new_game)

            if len(available_moves(new_game)) == 0:
                print("It's a draw, Game Over!!")
                loop = False
                break

            select_space(new_game, minimax(new_game, False)[1], "O")
            print_board(new_game)

        if minimax(new_game, True)[0] == 1:
            print("'X' wins the game!!")
            break
        elif minimax(new_game, True)[0] == -1:
            print("'O' wins the game!!")
            break

    else:
        start_o()
        while minimax(new_game, True)[0] == 0:
            select_space(new_game, minimax(new_game, True)[1], "X")
            print_board(new_game)

            if len(available_moves(new_game)) == 0:
                print("Tie, Game Over!!")
                loop = False
                break

            position = int(input("Select your position: "))
            select_space(new_game, position, "O")
            print_board(new_game)

        if minimax(new_game, True)[0] == 1:
            select_space(new_game, minimax(new_game, True)[1], "X")
            print_board(new_game)
            print("'X' wins the game!!")
            break
        elif minimax(new_game, True)[0] == -1:
            select_space(new_game, minimax(new_game, True)[1], "X")
            print_board(new_game)
            print("'O' wins the game!!")
            break
