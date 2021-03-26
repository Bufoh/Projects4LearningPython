# Initialize board configuration
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
turn = 0

# Print board function


def print_board():
    print(9 * "-")
    print(f"| {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"| {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"| {board[2][0]} {board[2][1]} {board[2][2]} |")
    print(9 * "-")


# Print empty board
print_board()


# Enter board configuration
# selection = input("Enter cells: ")
# board = [[selection[0], selection[1], selection[2]], [selection[3], selection[4], selection[5]],
#          [selection[6], selection[7], selection[8]]]
# print_board()

def get_game_status():
    # seqs = [selection[:3], selection[3:6], selection[6:], selection[0] + selection[3] + selection[6],
    #    selection[1] + selection[4] + selection[7], selection[2] + selection[5] + selection[8],
    #    selection[0] + selection[4] + selection[8], selection[2] + selection[4] + selection[6]]
    seqs = [board[0][:3], board[1][:3], board[2][:3], board[0][0] + board[1][0] + board[2][0],
            board[0][1] + board[1][1] + board[2][1], board[0][2] + board[1][2] + board[2][2],
            board[0][0] + board[1][1] + board[2][2], board[0][2] + board[1][1] + board[2][0]]
    board_string = ""
    for i in range(3):
        for j in range(3):
            board_string += board[i][j]
    count_x = [group.count("X") for group in seqs]
    count_o = [group.count("O") for group in seqs]
    if abs(board_string.count("X") - board_string.count("O")) > 1 or (3 in count_x and 3 in count_o):
        return "Impossible"
    elif 3 in count_x:
        return "X wins"
    elif 3 in count_o:
        return "O wins"
    elif board_string.count("_") == 0:
        return "Draw"
    else:
        return "Game not finished"


while True:
    next_move = input("Enter the coordinates: ").split()
    if next_move[0].isdecimal() and next_move[1].isdecimal:
        if int(next_move[0]) > 3 or int(next_move[1]) > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        elif board[int(next_move[0]) - 1][int(next_move[1]) - 1] in ("X", "O"):
            print("This cell is occupied! Choose another one!")
            continue
        else:
            if turn % 2 == 0:
                board[int(next_move[0]) - 1][int(next_move[1]) - 1] = "X"
            else:
                board[int(next_move[0]) - 1][int(next_move[1]) - 1] = "O"
            print_board()
    else:
        print("You should enter numbers!")
        continue
    if get_game_status() in ("X wins", "O wins", "Draw"):
        print(get_game_status())
        break
    turn += 1
