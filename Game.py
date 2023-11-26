import pygame as pg
import sys
from setting import *
from All_level import All_level
from game_data import *
from level import Level

class Game:
    def __init__(self):
        self.unlock_level = 1
        self.All_level = All_level(0,self.unlock_level,screen)
    def run(self):
        self.All_level.run()
       
pg.init()
pg.display.set_caption("Pixel Adventure")
screen = pg.display.set_mode((screen_width,screen_height))
clock = pg.time.Clock()
game = Game()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
                    
        screen.fill((214, 234, 248))
        game.run()
        # self.level.run()
        pg.display.update()
        clock.tick(60)