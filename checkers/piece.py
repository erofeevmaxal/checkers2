import pygame
from .constants import LIGHT, DARK, SQUARE_SIZE, BOX_SIZE, PIECE_DIAM, PIECE_BORDER, PIECE_BORDER_COLLOR


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        
        self.direction = 1 if color == DARK else -1
        self.x = 0
        self.y = 0
        self.calculate_pos()
    
    def calculate_pos(self):
        self.x = SQUARE_SIZE * self.col + BOX_SIZE + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + BOX_SIZE + SQUARE_SIZE // 2
        
    def make_king(self):
        self.king = True
        
    def draw(self, window):
        pygame.draw.circle(window, PIECE_BORDER_COLLOR, (self.x, self.y), PIECE_DIAM // 2 + PIECE_BORDER)
        pygame.draw.circle(window, self.color, (self.x, self.y), PIECE_DIAM // 2)