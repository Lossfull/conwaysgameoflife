import pygame, sys
from pygame.locals import *
import gameoflife

def main():
    pygame.init()
    #initialize constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    game_size = 30           #game screen is a gamesize x gamesize square
    blockSize = 25           #size of each block
    window_size = game_size*blockSize

    screen = pygame.display.set_mode((window_size, window_size), 0, 32)
    screen.fill(BLACK)
    pygame.display.set_caption("Conway's Game of Life")
    game = gameoflife.gameoflife(game_size, game_size)

    preparation = True
    startscreen = True

    # Start screen (real pain to work with texts in pygame)
    while (startscreen):
        screen.fill(BLACK)
        font = pygame.font.SysFont("Britannic Bold", 40)
        font2 = pygame.font.SysFont("Britannic Bold", 30)
        font3 = pygame.font.SysFont("Britannic Bold", 25)
        nlabel = font.render("Conway's Game of Life", 1, WHITE)
        nlabel2 = font2.render('press any button to start', 1, WHITE)
        nlabel3 = font3.render('Left mouse button to create life', 1, WHITE)
        nlabel4 = font3.render('Spacebar to start simulating', 1, WHITE)

        text_rect = nlabel.get_rect(center=(window_size / 2, window_size / 2 - 25))
        text_rect2 = nlabel2.get_rect(center=(window_size / 2, window_size / 2 + 25))
        text_rect3 = nlabel3.get_rect(center=(window_size-140, window_size-100))
        text_rect4 = nlabel4.get_rect(center=(window_size-140, window_size-50))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                startscreen = False
        screen.blit(nlabel, text_rect)
        screen.blit(nlabel2, text_rect2)
        screen.blit(nlabel3, text_rect3)
        screen.blit(nlabel4, text_rect4)
        pygame.display.flip()

    screen.fill(BLACK)
    # Drawing grid, placing blocks

    while preparation:
        for x in range(window_size // blockSize):
            for y in range(window_size // blockSize):
                rect = pygame.Rect(x * blockSize, y * blockSize,
                                   blockSize, blockSize)
                pygame.draw.rect(screen, GREY, rect, 1)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                game.gameboard[mouse_position[0]//blockSize][mouse_position[1]//blockSize] = 1
                rect = pygame.Rect(mouse_position[0]//blockSize * blockSize + 1, mouse_position[1]//blockSize * blockSize + 1,
                                   blockSize - 1, blockSize - 1)
                pygame.draw.rect(screen, WHITE, rect)
                pygame.display.update()

            elif event.type == KEYDOWN:
                if pygame.K_BACKSPACE:
                    preparation = False
        pygame.display.update()

    # Simulation starts

    while True:
        screen.fill(BLACK)
        for x in range(game_size):
            for y in range(game_size):
                if game.gameboard[x][y] == 1:
                    rect = pygame.Rect(x * blockSize + 1, y * blockSize + 1,
                                       blockSize-1, blockSize-1)
                    pygame.draw.rect(screen, WHITE, rect)
        game.turn()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.time.wait(80)
        pygame.display.update()

if __name__ == "__main__":
    main()
