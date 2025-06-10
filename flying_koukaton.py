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
    koukaton = image3.get_rect()
    koukaton.center=300,200 
    scrool_speed = 1
    tmr = 0
    while True:
        x = tmr%3200
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        key_lst = pg.key.get_pressed()
        bg_x -= scrool_speed
        move_x, move_y = 0, 0
        if key_lst[pg.K_UP]:
            move_y -= 1
        if key_lst[pg.K_DOWN]:
            move_y += 1
        if key_lst[pg.K_LEFT]:
            move_x -= 1
        if key_lst[pg.K_RIGHT]:
            move_x += 3
        koukaton.move_ip(move_x-scrool_speed,move_y)
        screen.blit(bg_img, [bg_x, bg_y])
        screen.blit(l_bg, [-x+1600,bg_y])
        
        screen.blit(bg_img, [-x+3200,0])
        screen.blit(bg_img, [-x,0])
        screen.blit(image3, koukaton)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()