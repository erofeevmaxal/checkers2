import pygame
from .constants import SQUARE_SIZE, BOX_SIZE, PIECE_DIAM, OUTLINE, OUTLINE_COLLOR, CROWN_WHITE, CROWN_BLACK, WHITE, BLACK


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.attack = False
        
        self.direction = 1 if color == BLACK else -1
        self.x = 0
        self.y = 0
        self.calculate_pos()
    
    def calculate_pos(self):
        self.x = SQUARE_SIZE * self.col + BOX_SIZE + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + BOX_SIZE + SQUARE_SIZE // 2
        
    def make_king(self):
        self.king = True
    
    def draw_crown(self, window):
        image = CROWN_WHITE if self.color == WHITE else CROWN_BLACK
        window.blit(image, (self.x - image.get_width() // 2, self.y - image.get_height() // 2))
            
        
    def draw(self, window):
        pygame.draw.circle(window, OUTLINE_COLLOR, (self.x, self.y), PIECE_DIAM // 2 + OUTLINE)
        pygame.draw.circle(window, self.color, (self.x, self.y), PIECE_DIAM // 2)
        
        if self.king:
            self.draw_crown(window)
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_pos()
        
    def print(self):
        return (self.row, self.col)