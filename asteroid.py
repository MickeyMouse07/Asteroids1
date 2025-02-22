import pygame
from constants import *
from circleshape import CircleShape

import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen,"white",( self.position.x, self.position.y),self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        randomAngle = random.uniform(20,50)
        smallerA = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
        smallerB = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS ))
        smallerA.velocity = pygame.math.Vector2.rotate(self.velocity, randomAngle) * 1.2
        smallerB.velocity = pygame.math.Vector2.rotate(self.velocity, -randomAngle) * 1.2
