import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game

FPS = 60

pygame.init()  # Initialize Pygame
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')
pygame.display.set_icon(pygame.image.load('assets/logo.png'))

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def draw_start_menu(win):
    win.fill(WHITE)
    font = pygame.font.SysFont(None, 74)
    text = font.render('Start Game', True, RED)
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
    win.blit(text, text_rect)
    pygame.display.update()
    return text_rect

def main_menu():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if draw_start_menu(WIN).collidepoint(pos):
                    run = False

        draw_start_menu(WIN)

def main():
    main_menu()  # Show the start menu
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
