
current_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
numbers_board = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
turn = "O"


def display_board(board):
    print('')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[7] == mark and board[8] == mark and board[9] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the left side
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  #


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


def player_choice(board):
    position = int(input('Choose your next position: (1-9): '))

    if space_check(current_board, position):
        return position
    else:
        position = int(input('Pick another position: '))
        if space_check(current_board, position):
            return position
        else:
            position = int(input('Last Chance: '))
            if space_check(current_board, position):
                return position
            else:
                print("I'm Done")


print("\n" * 100)
print("Welcome to Tic Tac Toe")
play_game = input("Are you ready to play the game? Y/N: ")

if play_game.lower() == "y":
    game_on = True
    display_board(numbers_board)
elif play_game.lower() == "n":
    game_on = False
else:
    print("\n")
    print("Unknown answer")

while game_on:

    if turn == "O":
        position_chosen = player_choice(current_board)
        print("\n" * 100)
        display_board(numbers_board)
        place_marker(current_board, turn, int(position_chosen))
        display_board(current_board)

        if win_check(current_board, "O"):
            print('Congratulations! You have won the game!')
            game_on = False
        else:
            if full_board_check(current_board):
                print('The game is a draw!')
                break
            else:
                turn = 'X'


    else:
        position_chosen = player_choice(current_board)
        print("\n" * 100)
        display_board(numbers_board)
        place_marker(current_board, turn, int(position_chosen))
        display_board(current_board)

        if win_check(current_board, "X"):
            print('Congratulations! You have won the game!')
            game_on = False
        else:
            if full_board_check(current_board):
                print('The game is a draw!')
                break
            else:
                turn = 'O'

