import pygame
from .piece import Piece
from .constants import LIGHT, DARK, BOX_COLLOR, ROWS, COLS, BOX_SIZE, SQUARE_SIZE, WIDTH, HEIGHT, LINES, BLACK, WHITE



class Board:
    def __init__(self):
        self.board = [[0]*COLS for i in range(ROWS)]
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
        for row in range(LINES):
            for col in range(1 - row % 2, COLS, 2):
                self.board[row][col] = Piece(row, col, BLACK)
                
        for row in range(ROWS - LINES, ROWS):
            for col in range(row % 2, COLS, 2):
                self.board[row][col] = Piece(row, col, WHITE)

    def draw_pieces(self, window):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    continue
                elif type(self.board[row][col]) == Piece:
                    self.board[row][col].draw(window)