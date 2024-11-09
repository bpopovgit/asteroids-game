import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid

BLACK = (0, 0, 0)



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    # Set the Asteroid containers field to automatically add instances to these groups

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable


    # Calculate center position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Instantiate the Player object at the center of the screen
    player = Player(x, y)

    # Add the player to the updatable and drawable groups
    updatable.add(player)
    drawable.add(player)

     # Create the AsteroidField object, which will add itself to the updatable group
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects in the updatable group
        updatable.update(dt)

        # Clear the screen
        screen.fill(BLACK)

        # Draw all objects in the drawable group

        for obj in drawable:
            if hasattr(obj, 'draw'):
                obj.draw(screen)


        # Update the display
        pygame.display.flip()

        # Cap the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds for delta time

if __name__ == "__main__":
    main()
