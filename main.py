import pygame, sys
from pygame.locals import *
import gameoflife

def main():
    pygame.init()
    #initialize constants
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (128,128,128)

    game_size = 30           #side length of the screen
    blockSize = 20

    WINDOW_HEIGHT = game_size*blockSize
    WINDOW_WIDTH = game_size*blockSize

    screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH), 0, 32)
    screen.fill(BLACK)
    pygame.display.set_caption("Conway's Game of Life")

    game = gameoflife.gameoflife(game_height, game_width)
    preparation = True
    while preparation:
        for x in range(WINDOW_WIDTH // blockSize):
            for y in range(WINDOW_HEIGHT // blockSize):
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
    while True:
        screen.fill(BLACK)
        for x in range(game_width):
            for y in range(game_height):
                if game.gameboard[x][y] == 1:
                    rect = pygame.Rect(x * blockSize + 1, y * blockSize + 1,
                                       blockSize-1, blockSize-1)
                    pygame.draw.rect(screen, WHITE, rect)
        game.turn()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # elif event.type == MOUSEMOTION:
            #     if (drawing):
            #         mouse_position = pygame.mouse.get_pos()
            #         if last_pos is not None:
            #             pygame.draw.line(screen, BLACK, last_pos, mouse_position, 1)
            #         last_pos = mouse_position
            # elif event.type == MOUSEBUTTONUP:
            #     mouse_position = (0, 0)
            #     drawing = False
            # elif event.type == MOUSEBUTTONDOWN:
            #     drawing = True
        pygame.time.wait(80)
        pygame.display.update()

if __name__ == "__main__":
    main()
