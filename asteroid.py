import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        # Initialize the parent class with position and radius
        super().__init__(x, y, radius)

        # Add this asteroid to the specified groups
        if Asteroid.containers:
            for group in Asteroid.containers:
                group.add(self)

    def draw(self, screen):
        # Draw the asteroid as a circle on the given screen
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        