import pygame
from .piece import Piece
from .constants import LIGHT, DARK, BOX_COLLOR, ROWS, COLS, BOX_SIZE, SQUARE_SIZE, WIDTH, \
    HEIGHT, LINES, BLACK, WHITE, OUTLINE_COLLOR, MOVE_RAD, FONT_SIZE


class Board:
    def __init__(self) -> None:
        self.board = [[0]*COLS for i in range(ROWS)]
        self.white_left = self.black_left = 12
    
    def inside(self, row: int, col: int) -> bool:
        return 0 <= row < ROWS and 0 <= col < COLS

    def get_piece(self, row: int, col: int) -> int | Piece:
        if not self.inside(row, col):
            return -1
        return self.board[row][col]
    
    def calculate_pos(self, row: int, col: int) -> tuple[int, int]:
        x = SQUARE_SIZE * col + BOX_SIZE + SQUARE_SIZE // 2
        y = SQUARE_SIZE * row + BOX_SIZE + SQUARE_SIZE // 2
        return (x, y)
        
    def create_board(self) -> None:
        for row in range(LINES):
            for col in range(1 - row % 2, COLS, 2):
                self.board[row][col] = Piece(row, col, BLACK)
                
        for row in range(ROWS - LINES, ROWS):
            for col in range(1 - row % 2, COLS, 2):
                self.board[row][col] = Piece(row, col, WHITE)        
    
    def draw_squares(self, window: pygame.Surface) -> None:
        window.fill(BOX_COLLOR)
        pygame.draw.rect(window, LIGHT, (BOX_SIZE, BOX_SIZE, WIDTH, HEIGHT))
        
        for row in range(ROWS):
            for col in range(1 - row % 2, COLS, 2):
                pygame.draw.rect(window, DARK, (BOX_SIZE + SQUARE_SIZE * col, BOX_SIZE + SQUARE_SIZE * row, SQUARE_SIZE, SQUARE_SIZE))

    def draw_pieces(self, window: pygame.Surface) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == 0:
                    continue
                elif type(self.board[row][col]) == Piece:
                    self.board[row][col].draw(window)

    def draw_coordinates(self, window: pygame.Surface) -> None:
        for col in range(COLS):
            x = BOX_SIZE + col * SQUARE_SIZE + SQUARE_SIZE // 2
            y1 = BOX_SIZE // 2
            y2 = BOX_SIZE + ROWS * SQUARE_SIZE + BOX_SIZE // 2
            
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render(chr(col + ord('a')), True, BLACK)

            text_rect1 = text.get_rect(center=(x, y1))
            text_rect2 = text.get_rect(center=(x, y2))
            
            window.blit(text, text_rect1)
            window.blit(text, text_rect2)
            
        for row in range(ROWS):
            x1 = BOX_SIZE // 2
            x2 = BOX_SIZE + COLS * SQUARE_SIZE + BOX_SIZE // 2
            y = BOX_SIZE + SQUARE_SIZE * row + SQUARE_SIZE // 2
            
            font = pygame.font.Font(None, FONT_SIZE)
            text = font.render(chr(8 - row + ord('0')), True, BLACK)

            text_rect1 = text.get_rect(center=(x1, y))
            text_rect2 = text.get_rect(center=(x2, y))
            
            window.blit(text, text_rect1)
            window.blit(text, text_rect2)
            
    def draw_valid_move(self, window: pygame.Surface, move: tuple[int, int, Piece | None]) -> None:
        row, col, target = move
        pygame.draw.circle(window, OUTLINE_COLLOR, self.calculate_pos(row, col), MOVE_RAD)
                
    def draw(self, window: pygame.Surface) -> None:
        self.draw_squares(window)
        self.draw_pieces(window)
        self.draw_coordinates(window)
        
    def move_piece(self, piece: Piece, row: int, col: int) -> int:
        if self.board[row][col] != 0:
            return 0
        
        self.board[piece.row][piece.col] = 0
        self.board[row][col] = piece
        piece.move(row, col)
        
        if row == ROWS - 1 or row == 0:
            piece.make_king()

        return 1
        
    def remove_piece(self, piece: Piece) -> None:
        self.board[piece.row][piece.col] = 0
        
        if piece.color == WHITE:
            self.white_left -= 1
        else:
            self.black_left -= 1
    
    def get_checker_walking_moves(self, piece: Piece) -> set[tuple[int, int, None]]:
        output = set()

        for y in (-1, 1):
            pos = self.get_piece(piece.row + piece.direction, piece.col + y)
            if pos == 0:
                output.add((piece.row + piece.direction, piece.col + y, None))
                
        return output       
            
    def get_checker_attacking_moves(self, piece: Piece) -> set[tuple[int, int, Piece]]:
        output = set()
        
        for x in (-1, 1):
            for y in (-1, 1):
                first = self.get_piece(piece.row + x, piece.col + y)
                second = self.get_piece(piece.row + x * 2, piece.col + y * 2)
                if first and second == 0 and first.color != piece.color:
                    output.add((piece.row + x * 2, piece.col + y * 2, first))
        return output
    
    def get_king_walking_moves(self, piece: Piece) -> set[tuple[int, int, None]]:
        output = set()
        
        for x in (-1, 1):
            for y in (-1, 1):
                for step in range(1, 8):
                    row, col = piece.row + x * step, piece.col + y * step
                    square = self.get_piece(row, col)
                    if square:
                        break
                    
                    output.add((row, col, None))
        return output
                    
    def get_king_attacking_moves(self, piece: Piece) -> set[tuple[int, int, Piece]]:
        output = set()
        target = None
    
        for x in (-1, 1):
            for y in (-1, 1):
                for step in range(1, 8):
                    row, col = piece.row + x * step, piece.col + y * step
                    square = self.get_piece(row, col)
                    if square == -1:
                        break
                    
                    if square:
                        if target or square.color == piece.color:
                            break
                        else:
                            target = square
                    elif target:
                        output.add((row, col, target))
                
                target = None
        return output
                                                     
    def get_valid_moves(self, piece: Piece, must_attack: bool) -> set[tuple[int, int, Piece | None]]:
        if piece.king:
            attacking_moves = self.get_king_attacking_moves(piece)
            if attacking_moves or must_attack:
                return attacking_moves
            return self.get_king_walking_moves(piece)
        
        else:
            attacking_moves = self.get_checker_attacking_moves(piece)
            if attacking_moves or must_attack:
                return attacking_moves
            return self.get_checker_walking_moves(piece)

    def possible_to_attack(self, turn: tuple[int, int, int]) -> bool:
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                
                if not piece:
                    continue
                if piece.color != turn:
                    continue
                
                if piece.king:
                    moves = self.get_king_attacking_moves(piece)
                else:
                    moves = self.get_checker_attacking_moves(piece)
                    
                if moves:
                    return True
        return False

    def possible_to_move(self, turn: tuple[int, int, int], must_attack: bool) -> bool:
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.get_piece(row, col)
                
                if not piece:
                    continue
                if piece.color != turn:
                    continue
                
                moves = self.get_valid_moves(piece, must_attack)
                    
                if moves:
                    return True
        return False