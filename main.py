import pygame
import constants
def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
 #   print("Starting asteroids!")
 #   print(f"Screen width: {constants.SCREEN_WIDTH}")
 #   print(f"Screen height: {constants.SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()