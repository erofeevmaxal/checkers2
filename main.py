import pygame
from checkers.constants import WIDTH, HEIGHT, BOX_SIZE, SQUARE_SIZE
from checkers.board import Board
from checkers.game import Game

WINDOW = pygame.display.set_mode((WIDTH + BOX_SIZE * 2, HEIGHT + BOX_SIZE * 2))
pygame.display.set_caption('Сheckers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = (y - BOX_SIZE) // SQUARE_SIZE
    col = (x - BOX_SIZE) // SQUARE_SIZE
    return row, col

def main():
    game = Game(WINDOW)
    game.selected = game.board.board[1][2]
    run = True
        
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        game.update()
    pygame.quit()
    
main()