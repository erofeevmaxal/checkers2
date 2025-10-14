import pygame
from .board import Board
from .constants import WHITE, BLACK

class Game:
    def __init__(self, window):
        self.turn = WHITE
        self.selected = None
        self.attacking_moves = set()
        self.walking_moves = set()
        self.window = window
        
        self.board = Board()
        self.board.create_board()
        
    def update(self):
        self.board.draw(self.window)
        if self.selected:
            self.attacking_moves = self.board.get_attacking_moves(self.selected)
            self.walking_moves = self.board.get_walknig_moves(self.selected)
        self.draw_valid_moves()
        pygame.display.update()
        
    def select(self, row, col) -> bool:
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        return False
        
    def move(self, row, col) -> bool:
        if (row, col) in self.walking_moves:
            self.board.move_piece(self.selected, row, col)
            
        elif (row, col) in self.attacking_moves:
            self.board.move_piece(self.selected, row, col)        
            
        else:
            return False
        
        return True

    def change_turn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

    def draw_valid_moves(self):
        if self.selected:
            for move in self.attacking_moves | self.walking_moves:
                self.board.draw_valid_move(self.window, move)