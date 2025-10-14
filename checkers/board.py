import pygame
from .constants import LIGHT, DARK, BOX_COLLOR, ROWS, COLS, BOX_SIZE, SQUARE_SIZE, WIDTH, HEIGHT


class Board:
    def __init__(self):
        self.board = []
        selected_piece = None
        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0
        
    def draw_squares(self, window):
        window.fill(BOX_COLLOR)
        pygame.draw.rect(window, LIGHT, (BOX_SIZE, BOX_SIZE, WIDTH, HEIGHT))
        
        for row in range(ROWS):
            for col in range(1 - row % 2, COLS, 2):
                pygame.draw.rect(window, DARK, (BOX_SIZE + SQUARE_SIZE * col, BOX_SIZE + SQUARE_SIZE * row, SQUARE_SIZE, SQUARE_SIZE))
                
    def create_board(self):
        pass