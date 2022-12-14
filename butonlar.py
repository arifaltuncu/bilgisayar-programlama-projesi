# butonlar
import pygame
import button

dünya_resmi = pygame.image.load("dünyabutonu.png")
ay_resmi = pygame.image.load("aybutonu.png")
cikis_resmi = pygame.image.load("cikisbutonu.png")

dünya_butonu = button.Button(400, 150, dünya_resmi, 1)
ay_butonu = button.Button(800, 150, ay_resmi, 1)
cikis_butonu = button.Button(600, 500, cikis_resmi, 1)