import pygame
from checkers.constants import WIDTH, HEIGHT, BOX_SIZE
from checkers.board import Board

WINDOW = pygame.display.set_mode((WIDTH + BOX_SIZE * 2, HEIGHT + BOX_SIZE * 2))
pygame.display.set_caption('Сheckers')


def main():
    board = Board()
    board.create_board()
    run = True
    
    while run:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw_squares(WINDOW)
        board.draw_pieces(WINDOW)
        pygame.display.update()
    pygame.quit()
    
main()