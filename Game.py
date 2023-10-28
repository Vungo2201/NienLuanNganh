import pygame as pg
import sys

class Game:
    def __init__(self):
        screen_width = 900
        screen_heigh = 600
        pg.init()
        pg.display.set_caption("Pixel Adventure")
        self.screen = pg.display.set_mode((screen_width,screen_heigh))
        self.clock = pg.time.Clock()
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            pg.display.update()
            self.clock.tick(60)

Game().run()