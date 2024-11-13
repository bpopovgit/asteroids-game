import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random


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

    def split(self):
        # Killing the current asteroid
        self.kill()

        #If the asteroid ist oo small to split, just return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Calculating the radius for the new smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Generating a random angle for splitting between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Creating two new velocity vectors for the split asteroids
        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2
        

        #Creating two new asteroids with the new radius and velocities
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = new_velocity_1


        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = new_velocity_2
        