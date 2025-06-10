import os
import sys
import pygame as pg

# change
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)
    
    
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_x = 0
    bg_y = 0
    image3 = pg.image.load("fig/3.png")
    image3 = pg.transform.flip(image3,True,False)

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10)
    enn.set_colorkey((0, 0, 0))
    l_bg = pg.transform.flip(bg_img,True,False)
    scrool_speed = 1
    tmr = 0
    while True:
        screen.blit(bg_img, [0,0])
        screen.blit(image3,[300,200])
        bg_x -= scrool_speed
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        screen.blit(bg_img, [bg_x, bg_y])
        screen.blit(bg_img, [bg_x + bg_img.get_width(), 0])
        screen.blit(image3,[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()