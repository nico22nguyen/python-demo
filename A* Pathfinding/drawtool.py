import Grid_obj
import pygame
import colors

#helper for draw function
def draw_rect(screen, row, col, color):
    pygame.draw.rect(screen, color, [(Grid_obj.MARGIN + Grid_obj.WIDTH) * col + Grid_obj.MARGIN,
                              (Grid_obj.MARGIN + Grid_obj.HEIGHT) * row + Grid_obj.MARGIN,
                              Grid_obj.WIDTH,
                              Grid_obj.HEIGHT])

#helper for draw function
def draw_text(screen, font, row, col, content, color):
    text = font.render(str(content), True, color)
    screen.blit(text, ((Grid_obj.MARGIN + Grid_obj.WIDTH) * col + 1.5 * Grid_obj.MARGIN, 
        (Grid_obj.MARGIN + Grid_obj.HEIGHT) * row + 1.5 * Grid_obj.MARGIN))

#draw function, runs 60 times/sec
def draw(screen, font, grid):
    #fill background
    screen.fill(colors.BG_COLOR)
    draw_text(screen, font, Grid_obj.NUM_ROWS, 3.5, "START", colors.TEXT_COLOR)

    #fill all cells
    for row in range(Grid_obj.NUM_ROWS):
        for col in range(Grid_obj.NUM_COLUMNS):
            draw_rect(screen, row, col, colors.UNEXP_COLOR)

    #color obstacles
    for cell in grid.obstacles:
        draw_rect(screen, cell[0], cell[1], colors.OBS_COLOR)

    #color frontier nodes
    for node in grid.open:
        draw_rect(screen, node.row, node.col, colors.FRONTIER_COLOR)

    #color explored nodes
    for node in grid.closed:
        draw_rect(screen, node.row, node.col, colors.EXP_COLOR)

    #color start and target
    if grid.start is not None:
        draw_rect(screen, grid.start.row, grid.start.col, colors.START_COLOR)
    if grid.target is not None:
        draw_rect(screen, grid.target.row, grid.target.col, colors.TARGET_COLOR)

def draw_final(screen, grid, font, path):
    #take last node in list
    trav = path[-1]
    #append its parent to list
    if path[0] is not None and not trav.parent is None:
        path.append(trav.parent)

    #draw screen and all nodes in path
    draw(screen, font, grid)

    if path[0] is not None:
        for node in path:
            draw_rect(screen, node.row, node.col, colors.TARGET_COLOR)


    