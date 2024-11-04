import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

BLACK = (0, 0, 0)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Calculate center position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Instantiate the Player object at the center of the screen
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen
        screen.fill(BLACK)

        # Update and draw the player
        player.draw(screen)  # Draw player on screen each frame

        # Update the display
        pygame.display.flip()

        # Cap the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds for delta time

if __name__ == "__main__":
    main()
