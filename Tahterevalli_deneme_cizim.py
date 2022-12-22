import pygame


pygame.init()
display = pygame.display.set_mode((800, 600))
run = True
siyah = 0 , 0 , 0 # RGB 0- 255
beyaz = 255 , 255 , 255
turuncu= 252 , 186 , 3
yesil= 90 , 180 , 90
kirmizi = 255,0,0


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.draw.rect(display, (kirmizi), pygame.Rect(200, 430, 520, 20),3)
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.draw.polygon(display, (turuncu), [(460,450),(650,550),(300,550)],5)
        pygame.display.flip()


pygame.quit()