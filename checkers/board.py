import pygame
from .piece import Piece
from typing import Tuple, Set
from .constants import LIGHT, DARK, BOX_COLLOR, ROWS, COLS, BOX_SIZE, SQUARE_SIZE, WIDTH, HEIGHT, LINES, BLACK, WHITE, OUTLINE_COLLOR, MOVE_RAD



class Board:
    def __init__(self):
        self.board = [[0]*COLS for i in range(ROWS)]
        self.white_left = self.black_left = 12
        self.white_kings = self.black_kings = 0
    
    def inside(self, row, col):
        return 0 <= row < ROWS and 0 <= col < COLS

    def get_piece(self, row, col):
        if not self.inside(row, col):
            return -1
        return self.board[row][col]
    
    def calculate_pos(self, row, col):
        x = SQUARE_SIZE * col + BOX_SIZE + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + BOX_SIZE + SQUARE_SIZE // 2
        return (x, y)
        
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
            for col in range(1 - row % 2, COLS, 2):
                self.board[row][col] = Piece(row, col, WHITE)

    def draw_pieces(self, window):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    continue
                elif type(self.board[row][col]) == Piece:
                    self.board[row][col].draw(window)
    
    def draw_valid_move(self, window, move):
        row, col, target = move
        pygame.draw.circle(window, OUTLINE_COLLOR, self.calculate_pos(row, col), MOVE_RAD)
                    
    def draw(self, window):
        self.draw_squares(window)
        self.draw_pieces(window)
        
    def move_piece(self, piece, row, col) -> int:
        if self.board[row][col] != 0:
            return 0
        
        self.board[piece.row][piece.col] = 0
        self.board[row][col] = piece
        piece.move(row, col)
        
        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.black_kings += 1
        return 1
        
    def remove_piece(self, piece):
        self.board[piece.row][piece.col] = 0
    
    def get_сhecker_walknig_moves(self, piece: Piece):
        output = set()

        for y in (-1, 1):
            pos = self.get_piece(piece.row + piece.direction, piece.col + y)
            if pos == 0:
                output.add((piece.row + piece.direction, piece.col + y, None))
                
        return output       
            
    def get_checker_attacking_moves(self, piece: Piece):
        output = set()
        
        for x in (-1, 1):
            for y in (-1, 1):
                first = self.get_piece(piece.row + x, piece.col + y)
                second = self.get_piece(piece.row + x * 2, piece.col + y * 2)
                if first and second == 0 and first.color != piece.color:
                    output.add((piece.row + x * 2, piece.col + y * 2, first))
        return output
    
    def get_valid_moves(self, piece, must_attack):
        if piece.king:
            pass
        else:
            attacking_moves = self.get_checker_attacking_moves(piece)
            if attacking_moves or must_attack:
                return attacking_moves
            return self.get_сhecker_walknig_moves(piece)

    def possible_to_attack(self, turn):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                if not piece:
                    continue
                if piece.color != turn:
                    continue
                
                if piece.king:
                    pass
                else:
                    moves = self.get_checker_attacking_moves(piece)
                    
                if moves:
                    return True
        return False