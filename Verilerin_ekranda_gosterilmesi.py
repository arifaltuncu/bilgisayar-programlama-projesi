import pygame as pg
import sys
pg.init()
clock = pg.time.Clock()

pg.display.set_caption('Test aşamalı kurumsal deneme tahtası')


en , boy = 800 , 600
siyah =  0 , 0 , 0 # RGB 0- 255
beyaz = 255 ,255, 255


beyaz=(255,255,255)
mavi=(0,0,255)
yesil=(34,139,34)
turuncu=(255,69,0)
kırmızı=(255,0,0)
ekran = pg.display.set_mode( (en,boy))

font = pg.font.SysFont('timesnewroman', 32)

def yazi_yaz(ekran,metin,x,y,renk=(255,255,255)):
    global font
    text = font.render(metin, True , renk)
    textRect = text.get_rect()
    textRect.left = x
    textRect.top = y
    ekran.blit(text , textRect)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(yesil)
    yazi_yaz (ekran,"kütlenin ismi          kütlesi                 3. bir değişken",50,40)
    yazi_yaz(ekran,"    dünya                350 kg                 3. değişken ", 70 ,80)
    pg.display.flip()
    clock.tick(30)