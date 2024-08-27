import pygame
from .constants import RED, WHITE, BLUE, BLACK, ROWS, COLS, SQUARE_SIZE
from .piece import Piece
class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([]) # Appends an empty list to the board.
            for col in range (COLS):
                if col % 2 == ((row+1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE)) # Appends a white piece to the board.
                    elif row > 4:
                        self.board[row].append(Piece(row, col, RED)) # Appends a red piece to the board.
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win): # Draws the board.
        self.draw_squares(win) # Draws the squares.
        for row in range(ROWS): # Loops through the rows.
            for col in range(COLS): # Loops through the columns.
                piece = self.board[row][col] # Gets the piece.
                if piece != 0: 
                    piece.draw(win) # Draws the piece.