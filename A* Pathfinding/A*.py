# TODO
# - add instructions to make the setup process more intuitive
# - add drag feature for obstacle placement
# - heap optimization

import pygame
import time
import colors
import Grid_obj
from Node_obj import Node
import drawtool

#manipulate to change game
FRAMERATE = 25
START = None
END = None

#setup pygame
pygame.init()
screen = pygame.display.set_mode(Grid_obj.WINDOW_SIZE)
pygame.display.set_caption("A* Pathfinder")

pygame.font.init()
font = pygame.font.Font("/System/Library/Fonts/NewYork.ttf", 100)

#initialize grid
grid = Grid_obj.Grid(START, END)

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

#used to animate shortest path when found
path = [None]

#Loop until the user clicks the close button.
running = True
game_on = False
no_path = False
setting_up = True

while running:
    if no_path:
        colors.EXP_COLOR = colors.YELLOW
    else:
        colors.EXP_COLOR = (235, 30, 50)

    for event in pygame.event.get():
        #quit on close
        if event.type == pygame.QUIT:
            pygame.font.quit()
            pygame.quit()
            running = False

        #mouse click
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #get mouse position
            pos = pygame.mouse.get_pos()

            #convert raw mouse position to row-column format
            col = pos[0] // (Grid_obj.WIDTH + Grid_obj.MARGIN)
            row = pos[1] // (Grid_obj.HEIGHT + Grid_obj.MARGIN)

            #if in setup mode, in bounds of grid, not on start, not on target, and not duplicate
            if (setting_up and row < Grid_obj.NUM_ROWS and col < Grid_obj.NUM_COLUMNS and 
            (START is None or not (grid.start.row == row and grid.start.col == col)) and 
            (END is None or not (grid.target.row == row and grid.target.col == col))):
                if END is None:
                    END = (row, col)
                    grid = Grid_obj.Grid(None, END)
                elif START is None:
                    START = (row, col)
                    grid = Grid_obj.Grid(START, END)
                else:
                    if (row, col) in grid.obstacles:
                        grid.obstacles.remove((row, col))
                    else:
                        grid.obstacles.append((row, col))
            
            
            #clicked start button
            elif row >= Grid_obj.NUM_ROWS and row < Grid_obj.NUM_ROWS + Grid_obj.START_BUTTON_OFFSET and col < Grid_obj.NUM_COLUMNS:
                if setting_up and START is not None and END is not None:
                    game_on = True
                    setting_up = False
                else:
                    #reset
                    game_on = False
                    no_path = False
                    setting_up = True
                    START = None
                    END = None
                    path = [None]
                    grid = Grid_obj.Grid(None, None)
                

    #path found
    if game_on and (not grid.single_a_star_iter() or len(grid.open) == 0):
        game_on = False
        if len(grid.open) == 0:
            no_path = True
        continue

    #display
    if game_on:
        drawtool.draw(screen, font, grid)
    else:
        path[0] = grid.target
        drawtool.draw_final(screen, grid, font, path)

    pygame.display.flip()

    clock.tick(FRAMERATE)

"""
running = True
while running:
    for event in pygame.event.get():
        #quit on close
        if event.type == pygame.QUIT:
            running = False
    
    #display
    
    pygame.display.flip()

    clock.tick(FRAMERATE)
"""
pygame.font.quit()
pygame.quit()