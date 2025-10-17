import pygame, sys
from .board import Board
from .constants import WHITE, BLACK

class Game:
    def __init__(self, window):
        self.turn = WHITE
        self.selected = None
        self.valid_moves = set()
        self.attack_continue = False
        self.must_attack = False
        self.window = window
        
        self.board = Board()
        self.board.create_board()
        
    def update(self):
        if self.board.white_left < 1 :
            print("black win")
            pygame.quit()
            sys.exit()
    
        elif self.board.black_left < 1:
            print("white win")
            pygame.quit()
            sys.exit()
        
        elif not self.board.possible_to_move(self.turn, self.must_attack):
            if self. turn == WHITE:
                print("black win (no moves for white)")
            else:
                print("white win (no moves for black)")
            pygame.quit()
            sys.exit()
            
        self.board.draw(self.window)        
                
        if self.selected:
            self.valid_moves = self.board.get_valid_moves(self.selected, self.must_attack)
        self.draw_valid_moves()
        
        pygame.display.update()
        
    def select(self, row, col) -> bool:
        
        if self.selected:
            result = self.move(row, col)
            if not result and not self.attack_continue:
                self.selected = None
                self.select(row, col)
        else:
            piece = self.board.get_piece(row, col)
            if piece and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece, self.must_attack)
    
                return True
            
        return False
        
    def move(self, row, col) -> bool:
        move = self.find_valid_move(row, col)
        if not move:
            return False
        
        row, col, target = move
        
        if target:
            self.board.move_piece(self.selected, row, col)
            self.board.remove_piece(target)
            
            self.attack_continue = True
            
            piece = self.board.get_piece(row, col)
            
            if not self.board.get_valid_moves(piece, self.must_attack):
                self.change_turn()
            
        else:
            self.board.move_piece(self.selected, row, col)
            self.change_turn()
            
        return True
    
    def find_valid_move(self, row, col):
        for move in self.valid_moves:
            if (row, col) == (move[0], move[1]):
                return move
        return None

    def draw_valid_moves(self, ):
        if self.selected:
            for move in self.valid_moves:
                self.board.draw_valid_move(self.window, move)

    def change_turn(self):        
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

        self.selected = None
        self.attack_continue = False
        self.must_attack = self.board.possible_to_attack(self.turn)

                
 