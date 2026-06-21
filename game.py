import pygame
import random
from utils import generage_number, pull_board_line, evaluate, UIManager

NROW = 4
NCOL = 4
CELL_SIZE = 100
WIN_WIDTH = CELL_SIZE * NCOL
WIN_HEIGHT = CELL_SIZE * NROW + 50

COLOR_BOARD1 = (180, 100, 60)
COLOR_BOARD2 = (180, 150, 20)

is_running = True

board = [
    [None, None, None, 1],
    [None, None, None, 1],
    [None, None, None, 1],
    [None, None, None, 1],
]

board = [
    [1, 2, 2, 2],
    [1, 1, 2, 2],
    [1, 1, 1, 2],
    [1, 1, 1, 1],
]

board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

board = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

pygame.font.init()
screen = pygame.display.set_mode([WIN_WIDTH, WIN_HEIGHT])
font = pygame.font.SysFont('consolas', 40)
font_small = pygame.font.SysFont('consolas', 20)

iteration = 0

is_clicked = False

is_key_down_left = False
is_key_down_right = False
is_key_down_up = False
is_key_down_down = False

game_state = "intro"

ui_manager = UIManager(screen, font_small, (WIN_WIDTH, WIN_HEIGHT), game_state)

while is_running:
    for event in pygame.event.get():
        # print(event)
        
        if event.type == 256:
            is_running = False
            break
        
        elif event.type == 768:
            if game_state == "player_choice":
                if event.key == pygame.K_LEFT:
                    is_key_down_left = True
                    game_state = 'player_choice'
                elif event.key == pygame.K_RIGHT:
                    is_key_down_right = True
                    game_state = 'player_choice'
                elif event.key == pygame.K_UP:
                    is_key_down_up = True
                    game_state = 'player_choice'
                elif event.key == pygame.K_DOWN:
                    is_key_down_down = True
                    game_state = 'player_choice'
                elif event.key == pygame.K_SPACE:  ## test
                    # generage_number(board)
                    game_state = 'player_choice'
                
                
    # generate number
    # generage_number(board)
    if game_state == 'intro':
        generage_number(board)
        game_state = 'player_choice'
        
    elif game_state == 'player_choice':
        if is_key_down_left == True:
            pull_board_line(board, "left")
            is_key_down_left = False
            game_state = 'generate_number'
        elif is_key_down_right == True:
            pull_board_line(board, "right")
            is_key_down_right = False
            game_state = 'generate_number'
        elif is_key_down_up == True:
            pull_board_line(board, "up")
            is_key_down_up = False
            game_state = 'generate_number'
        elif is_key_down_down == True:
            pull_board_line(board, "down")
            is_key_down_down = False
            game_state = 'generate_number'
        else:
            game_state = 'player_choice'
            
        board_state = evaluate(board)
        if board_state == "lose":
            game_state = "end"
            ui_manager.set_state_msg(board_state)
       
                        
    elif game_state == 'generate_number':
        generage_number(board)
        game_state = 'player_choice'
        
    elif game_state == "end":
        pass
    
        
        
    screen.fill((0, 0, 0))
    for i in range(NROW):
        for j in range(NCOL):
            # if board[i][j] == None:
            if (i + j) % 2 == 0:
              color = COLOR_BOARD1
            else:
              color = COLOR_BOARD2  
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
            # text
            if board[i][j] != None:
                tile_x = j * CELL_SIZE
                tile_y = i * CELL_SIZE
                
                text_content = f"{board[i][j]}"
                text = font.render(text_content, True, (255, 255, 255))
                
                text_w = text.get_width()
                text_h = text.get_height()
                
                center_x = tile_x + (CELL_SIZE - text_w) // 2
                center_y = tile_y + (CELL_SIZE - text_h) // 2
                screen.blit(text, (center_x, center_y))
                
    ui_manager.draw()
                
    
    
            
    pygame.display.flip()