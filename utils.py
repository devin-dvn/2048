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
        
        max_num = 1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != None and board[i][j] > max_num:
                    max_num = board[i][j]
        # number = random.randint(1, EXPONENT_MAX - 1)
        number = random.randint(1, max_num)
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
    
    
def evaluate(board):
    final_number = EXPONENT_MAX
    cnt_none = 0
    cnt_final = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == None:
                cnt_none += 1
            elif board[i][j] == final_number:
                cnt_final += 1
    
    if cnt_none == 0:
        return "lose"
    elif cnt_final >= 1:
        return "win"
    
class UIManager:
    def __init__(self, screen, font, win_size, game_state):
        self.screen = screen
        self.font = font
        self.font_small = font
        self.WIN_WIDTH = win_size[0]
        self.WIN_HEIGHT = win_size[1]
        self.state_msg = "----"
        self.game_state = game_state
        
    def set_state_msg(self, text):
        self.state_msg = text
    
    def _show_state_msg(self):
        text_content = f"{self.state_msg}"
        text = self.font.render(text_content, True, (255, 255, 255))
        self.screen.blit(text, (10, self.WIN_HEIGHT - 30))
        
    def draw(self):
        text_content = f"game_state: {self.game_state}"
        text = self.font_small.render(text_content, True, (255, 255, 255))
        self.screen.blit(text, (10, self.WIN_HEIGHT - 50))
        
        self._show_state_msg()
        