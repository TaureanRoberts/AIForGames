import pygame

def main():   
    pygame.init()

    SCREEN = pygame.display.set_mode((1920,1080))
    SCREEN.fill((0,25,100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()

main()
