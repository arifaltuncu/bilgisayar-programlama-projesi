# Gerekli kütüphaneler
import button
import pygame 
import sys

en= 1600
boy = 1000


pygame.init()

# ekran tanımlama
screen = pygame.display.set_mode((en, boy))

# Choose Font
font = pygame.font.SysFont("arial", 20)

# butonlar
dünya_resmi = pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fizik_proje\earth_button.png")
ay_resmi = pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fizik_proje\\moon_button.png")
cikis_resmi = pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fizik_proje\\quit_button.png")

dünya_butonu = button.Button(400, 150, dünya_resmi, 1)
ay_butonu = button.Button(800, 150, ay_resmi, 1)
cikis_butonu = button.Button(600, 500, cikis_resmi, 1)

# States
moving = False
game_paused = True
run = True
menu_state = "main"

# objeler
# object1 = pygame.Rect(20, 50, 20, 50)
object2 = pygame.Rect(20, 50, 20, 50)
object3 = pygame.Rect(20, 50, 20, 50)
object4 = pygame.Rect(20, 50, 20, 50)
obstacle = pygame.Rect(350, 500, 800, 50)

# Event Loop
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

    if game_paused:
        if menu_state == "main":
            screen.fill((255, 255, 255))
            if dünya_butonu.draw(screen):
                menu_state = "earth"
                game_paused = False
            if ay_butonu.draw(screen):
                menu_state = "moon"
                game_paused = False
            if cikis_butonu.draw(screen):
                run = False
    else:
        if menu_state == "earth":
            # background
            background = pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fp\\images\\earthbackgorund.jpg") 
            screen.blit(background, (0,0))
            # create planet text
            planet_text = font.render("Welcome to the Earth", True, (0, 0, 0))
            tahterevalli=pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fizik_proje\\images\\tahta1.PNG")
            destek=pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fizik_proje\\images\\destek.png")
            screen.blit(destek,(600,620))
            screen.blit(tahterevalli,(400,600))
            screen.blit(planet_text, (700, 200))
        elif menu_state == "moon":
            # background
            background = pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fp\\images\\moonbackground.jpg")
            screen.blit(background, (0, 0))
            # create planet text
            planet_text = font.render("Welcome to the Moon", True, (0,0,0))
            tahterevalli=pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fizik_proje\\images\\tahta1.PNG")
            destek=pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\fizik_proje\\images\\destek.png")
            screen.blit(destek,(600,620))
            screen.blit(tahterevalli,(400,600))
            screen.blit(planet_text, (700, 200))

        pygame.draw.rect(screen, (0, 0, 0), object1)

        if object1.colliderect(obstacle):
            moving = False

    # update screen
    pygame.display.update()
