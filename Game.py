import pygame as pg
import sys
from setting import *
from All_level import All_level
from game_data import *
from level import Level

class Game:
    def __init__(self):
        self.unlock_level = 0
        self.All_level = All_level(0,self.unlock_level,screen,self.Show_level)
        self.status = 'All_level'
    
    def Show_level(self,current_level):
        self.level = Level(current_level,screen,self.New_All_level)
        self.status = 'level'
        
    def New_All_level(self,current_level,new_unlock_level):
        if new_unlock_level > self.unlock_level:
            self.unlock_level = new_unlock_level
        self.All_level = All_level(current_level,new_unlock_level,screen,self.Show_level)
        self.status = 'All_level'
    
    def run(self):
        if self.status ==  'All_level':
            self.All_level.run()
        else:
            self.level.run()
       
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
  
    pg.display.update()
    clock.tick(60)