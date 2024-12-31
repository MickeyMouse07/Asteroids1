import pygame
import constants
from player import Player



def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    Player.containers = (updatable, drawable)
    Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    

    dt = 0


    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
    

        for draw in drawable:
            draw.draw(screen)

        for update in updatable:
            update.update(dt)

        
        pygame.display.flip()
        dt = clock.tick(60)/1000

 #   print("Starting asteroids!")
 #   print(f"Screen width: {constants.SCREEN_WIDTH}")
 #   print(f"Screen height: {constants.SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()