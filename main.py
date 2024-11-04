# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

BLACK = (0, 0, 0)

pygame.init()
clock = pygame.time.Clock()
dt = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BLACK)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

    


if __name__ == "__main__":
    main()
    pygame.quit()
