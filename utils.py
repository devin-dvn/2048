import random

EXPONENT_MAX = 11

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

def transpose(board):
    new_board = [[None] * len(board) for _ in range(len(board[0]))]
    for i in range(len(new_board)):
        for j in range(len(new_board[0])):
            new_board[i][j] = board[j][i]

    return new_board
        

def generage_number(board: [[int]]):
    empty_cell_pos_list = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                empty_cell_pos_list.append((i, j))
         
    if len(empty_cell_pos_list) > 0:
        i, j = random.choice(empty_cell_pos_list)
        # number = 2 ** random.randint(1, EXPONENT_MAX)
        number = random.randint(1, EXPONENT_MAX - 1)
        board[i][j] = number
        print(f"[generage_number()] (i, j): {i, j} / number: {number}")
        
    return 

def pull_board_line(board, direction):
    NCOL = len(board[0])
    NROW = len(board)
    
    if direction == "right":
        for k in range(len(board)):
            line = [value for value in board[k] if value != None]
            # print(line)
            for j in range(len(line) - 1, 0, -1):
                if line[j] == line[j - 1]:
                    line[j - 1] = line[j] + 1
                    line.pop(j)
            _line = [None] * (NCOL - len(line)) + line
            board[k] = _line

    elif direction == "left":
        for k in range(len(board)):
            line = [value for value in board[k] if value != None]
            # print(line)
            j = 0
            while j < len(line) - 1:
                if line[j] == line[j + 1]:
                    line[j + 1] = line[j] + 1
                    line.pop(j)
                    continue
                j += 1
            _line = line + [None] * (NCOL - len(line))
            board[k] = _line

    elif direction == "up":
        for k in range(len(board[0])):
            line = [board[i][k] for i in range(len(board)) if board[i][k] != None]
            # print(line)
            j = 0
            while j < len(line) - 1:
                if line[j] == line[j + 1]:
                    line[j + 1] = line[j] + 1
                    line.pop(j)
                    continue
                j += 1
            _line = line + [None] * (NROW - len(line))
            for i in range(len(board)):
                board[i][k] = _line[i]

    elif direction == "down":
        for k in range(len(board[0])):
            line = [board[i][k] for i in range(len(board)) if board[i][k] != None]
            print(line)
            for j in range(len(line) - 1, 0, -1):
                if line[j] == line[j - 1]:
                    line[j - 1] = line[j] + 1
                    line.pop(j)
            _line = [None] * (NROW - len(line)) + line
            for i in range(len(board)):
                board[i][k] = _line[i]
                
    pprint(board)