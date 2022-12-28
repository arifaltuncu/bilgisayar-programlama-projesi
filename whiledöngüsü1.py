
import sys
import pygame

run =True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            moving = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            object1.collidepoint(event.pos)
            moving = True
        elif event.type == pygame.MOUSEMOTION and moving:
            object1.move_ip(event.rel)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu_state = "main"
                screen.fill((255, 255, 255))
                game_paused = True