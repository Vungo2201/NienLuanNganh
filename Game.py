import pygame as pg
import sys
from setting import *
from game_data import *
from level import Level

class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Pixel Adventure")
        self.screen = pg.display.set_mode((screen_width,screen_height))
        self.clock = pg.time.Clock()
        self.level = Level(level1,self.screen)
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    
            self.screen.fill((214, 234, 248))
            self.level.run()
            pg.display.update()
            self.clock.tick(60)

Game().run()