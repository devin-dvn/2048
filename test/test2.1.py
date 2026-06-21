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
    [None, None, 1, 1],
    [1, None, None, 2],
    [None, None, 3, 3],
    [None, None, None, 4],
]
board = [
    [1, None, None, 1],
    [1, None, None, 2],
    [None, None, 3, 3],
    [None, None, None, 4],
]
board = [
    [1, None, 1, 1],
    [1, 2, None, 2],
    [3, 3, 3, 3],
    [None, 1, 4, 4],
]
board = [
    [None, None, None, 1],
    [None, None, 1, None],
    [None, 1, None, None],
    [1, None, None, None],

    [None, None, 2, 2],
    [None, 2, None, 2],
    [None, 2, 2, None],
    [2, None, None, 2],
    [2, None, 2, None],
    [2, 2, None, None],

    [None, 3, 3, 3],
    [3, None, 3, 3],
    [3, 3, None, 3],
    [3, 3, 3, None],

    [4, 4, 4, 4],
]
pprint(board)

def _pull_line_one_step(board, direction, k):
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

            # print(f"[{i}/{j}] cnt_none: {cnt_none}")
            # pprint(board, depth=1)


def pull_board_line(board, direction, k):
    if direction == "left":
        j = NCOL - 1
        while j >= 1:
            # print(j)
        # for j in range(NCOL - 1, 0, -1):
            if board[k][j] == None:
                j -= 1
                continue

            same_indice_list = [j]
            for _j in range(j - 1, -1, -1):
                if board[k][_j] == None:
                    continue
                elif board[k][_j] != board[i][j]:
                    break
                
                same_indice_list.append(_j)
            # print(f"[{k}/{j}] same_indice_list: {same_indice_list}")

            if len(same_indice_list) > 1:
                # scale = 2 ** (len(same_indice_list) // 2)
                # value = board[k][same_indice_list[0]] * scale
                value = board[k][same_indice_list[0]] + 1
                for _i in range(len(same_indice_list) - len(same_indice_list) % 2):
                    __i = same_indice_list[_i]
                    board[k][__i] = None
                
                __i = same_indice_list[len(same_indice_list) - len(same_indice_list) % 2 - 1]
                board[k][__i] = value

                if len(same_indice_list) % 2 == 1:
                    j = same_indice_list[-1] + 1
                else:
                    j = same_indice_list[-1]
                
                # continue

            
            j -= 1
            # print(f">>> j: {j}")
            # pprint(board)
        _pull_line_one_step(board, direction, k)
        


                

            

for i in range(len(board)):
    pull_board_line(board, "left", i)




pprint(board)