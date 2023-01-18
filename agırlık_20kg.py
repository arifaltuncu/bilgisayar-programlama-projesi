import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ağırlık")

done = False
clock = pygame.time.Clock()


ağırlık_3 = 20

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)


    pygame.draw.rect(screen, BLACK, [20, 20, 50, ağırlık_3 * 10], 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()