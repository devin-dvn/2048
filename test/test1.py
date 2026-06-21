from pprint import pprint
NROW = 4
NCOL = 4

board = [
    [None, None, None, 1],
    [None, None, None, 2],
    [None, None, None, 3],
    [None, None, None, 4],
]

def pull_board_line(board, direction, k):
    if direction == "left":
        for j in range(NCOL - 1):
            board[k][j] = board[k][j + 1]

for i in range(NROW):
    j = 0
    while j <= NCOL - 1:
        if board[i][j] == None:
            pull_board_line(board, "left", i)




pprint(board)