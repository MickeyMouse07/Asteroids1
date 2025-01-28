import sys
import pygame
import constants
#from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    play = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    AsteroidField()
    

    dt = 0


    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                 
 
        for update in updatable:
            update.update(dt)
            

        for asteroid in asteroids:
            if asteroid.collision(play):
                print("Game over!")
                sys.exit()

            for bullet in shots:
                if asteroid.collision(bullet):
                    asteroid.kill()
                    bullet.kill()

        for draw in drawable:
            draw.draw(screen)


        

        
        pygame.display.flip()
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()