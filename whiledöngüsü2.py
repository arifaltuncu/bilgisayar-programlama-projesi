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