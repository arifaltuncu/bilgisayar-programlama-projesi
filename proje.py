import pygame       

pygame.init()   

ekran=pygame.display.set_mode((1280,720))  



pygame.display.set_caption("Tahterevalli Denge Simülasyonu")     

background=pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\pygamefoto\\arka.png.jpg")   

icon = pygame.image.load("C:\\Users\\marif\\OneDrive\\Masaüstü\\pygamefoto\\icon.png.png")   
pygame.display.set_icon(icon)


white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
black=(0,0,0)


run=True
while run:
    ekran.fill((80,50,65))  
    # ekran.blit(background(0,0))  


    for event in pygame.event.get():     
        if event.type==pygame.QUIT:
            run=False                                      

    pygame.display.update()





