import pygame
from drawing_util import Shape
from vector2_class import Vector2
def main():
    pygame.init()

    SCREEN = pygame.display.set_mode((1920, 970)) #Sets the screen size
    SCREEN.fill((0, 25, 100)) #Sets the screen color

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

main()
