import pygame
from typing import Tuple
from checkers.constants import WIDTH, HEIGHT, BOX_SIZE, SQUARE_SIZE, ROWS, COLS
from checkers.board import Board
from checkers.game import Game

WINDOW = pygame.display.set_mode((WIDTH + BOX_SIZE * 2, HEIGHT + BOX_SIZE * 2))
pygame.display.set_caption('Сheckers')
pygame.font.init()

def get_row_col_from_mouse(pos: tuple[int, int]) -> tuple[int, int] | None:
    x, y = pos
    row = (y - BOX_SIZE) // SQUARE_SIZE
    col = (x - BOX_SIZE) // SQUARE_SIZE
    if 0 <= row < ROWS and 0 <= col < COLS:
        return row, col
    return None

def main():
    game = Game(WINDOW)
    run = True
        
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                point = get_row_col_from_mouse(pos)
                if not point:
                    continue
                
                row, col = point
                game.select(row, col)
        
        game.update()
    pygame.quit()
    
main()