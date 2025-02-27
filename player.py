import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.BulletTimer = 0


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.BulletTimer -= dt
        keys = pygame.key.get_pressed()
        #self.BulletTimer = max(self.BulletTimer  - dt, 0) 
       
        

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.BulletTimer <= 0:
                self.shoot()
                self.BulletTimer = PLAYER_SHOOT_COOLDOWN
  
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        bullet = Shot(self.position.x,self.position.y)
        speed = pygame.Vector2(0, 1)
        speedface = speed.rotate(self.rotation)
        superspeed = speedface * PLAYER_SHOOT_SPEED
        bullet.velocity = superspeed

