def pprint(board, depth=0):
    print("==================")
    for line in board:
        print("\t" * depth, end="")
        for col in line:
            if col == None:
                print("-", end=" ")
            else:
                print(col, end=" ")
        print()
        
NROW = 4
NCOL = 4

board = [
    [None, 0, None, 1],
    [00, None, None, 2],
    [None, None, 0, 3],
    [None, None, None, 4],
]
pprint(board)


def pull_board_line(board, direction, k):
    if direction == "left":
        for j in range(NCOL - 1, 0, -1):
            if board[i][j] == None:
                continue

            _j = j - 1
            cnt_none = 0
            while _j >= 0:
                if board[i][_j] == None:
                    cnt_none += 1
                else:
                    break
                _j -= 1
            for _j in range(j, NCOL):
                board[i][_j - cnt_none] = board[i][_j]
            
            for _j in range(cnt_none):
                board[i][NCOL - _j - 1] = None

            print(f"[{i}/{j}] cnt_none: {cnt_none}")
            pprint(board, depth=1)

            # for j in range(NCOL - 1):
            #     board[k][j] = board[k][j + 1]
    # pprint(board)

for i in range(NROW):
    j = 0
    while j <= NCOL - 1:
        if board[i][j] == None:
            pull_board_line(board, "left", i)

        j += 1




pprint(board)