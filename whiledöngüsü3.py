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