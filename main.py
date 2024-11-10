import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys

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
    shots = pygame.sprite.Group()


    # Set the Asteroid containers field to automatically add instances to these groups

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)


    # Calculate center position
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # Instantiate the Player object at the center of the screen
    print("Creating player at center of screen.")
    player = Player(x, y)

    # Add the player to the updatable and drawable groups
    updatable.add(player)
    drawable.add(player)
    print("Player created.")

     # Create the AsteroidField object, which will add itself to the updatable group
    print("Creating asteroid field.")
    asteroid_field = AsteroidField()
    print("Asteroid field created.")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update all objects in the updatable group
        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()

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
