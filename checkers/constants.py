import pygame

WIDTH = HEIGHT = 800
ROWS = COLS = 8
LINES = 3
SQUARE_SIZE = WIDTH // COLS
BOX_SIZE = 30

LIGHT = (95, 192, 206)
DARK = (1, 89, 101)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BOX_COLLOR = (31, 107, 117)
OUTLINE_COLLOR = (128, 128, 128)

PIECE_DIAM = 0.6 * SQUARE_SIZE
MOVE_RAD = 10
OUTLINE = 3

CROWN_WHITE = pygame.transform.scale(pygame.image.load('assets/crown_white.png'), (45, 30))
CROWN_BLACK = pygame.transform.scale(pygame.image.load('assets/crown_black.png'), (45, 30))

FONT_SIZE = 30
