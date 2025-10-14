import pygame
from .board import Board
from .constants import WHITE, DARK

class Game:
    def __init__(self, board: Board):
        self.turn = WHITE
        self.board = board
        
    def move(self, x, y, target_x, target_y):
        pass

    def atack(self, x, y, target_x, target_y):
        pass
    
    def process_mousebutton(self, event):
        pass
    
    