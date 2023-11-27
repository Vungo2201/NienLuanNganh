import pygame as pg
import sys
from setting import *
from All_level import All_level
from game_data import *
from level import Level
from User_interface import User_Interface

class Game:
    def __init__(self):
        self.unlock_level = 0
        self.max_life = 3
        self.current_life = 3
        self.apple = 0
        self.All_level = All_level(0,self.unlock_level,screen,self.Show_level)
        self.status = 'All_level'
        self.UI = User_Interface(screen)
        self.die_sound = pg.mixer.Sound('data/sound/die.wav')
        self.All_level_music = pg.mixer.Sound('data/sound/All_level.mp3')
        self.level_music = pg.mixer.Sound('data/sound/level.mp3')
        self.All_level_music.set_volume(0.5)
        self.level_music.set_volume(0.5)
        self.All_level_music.play(loops = -1)

        
    def Show_level(self,current_level):
        self.level = Level(current_level,screen,self.New_All_level,self.pick_apple,self.resert_apple,self.change_life,self.resert_life)
        self.status = 'level'
        self.All_level_music.stop()
        self.level_music.play(loops= -1)
        
    def New_All_level(self,current_level,new_unlock_level):
        if new_unlock_level > self.unlock_level:
            self.unlock_level = new_unlock_level
        self.All_level = All_level(current_level,self.unlock_level,screen,self.Show_level)
        self.status = 'All_level'
        self.level_music.stop()
        self.All_level_music.play(loops= -1)
        
    def pick_apple(self):
        self.apple += 1
    
    def resert_apple(self):
        self.apple = 0
    
    def change_life(self):
        self.current_life -= 1
        
    def resert_life(self):
        self.current_life = self.max_life
    
    def game_over(self):
        if self.current_life == 0:
            self.die_sound.play()
            self.resert_life()
            self.resert_apple()
            self.New_All_level(0,self.unlock_level)
            
    def run(self):
        if self.status ==  'All_level':
            self.All_level.run()
        else:
            self.level.run()
            self.UI.display_life(self.current_life)
            self.UI.display_apple(self.apple)
            self.game_over()
       
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