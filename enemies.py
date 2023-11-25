import pygame
from random import randint
from tiles import AnimeTile
class Enimies(AnimeTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'data/images/enemies/Chicken')
        self.move_speed = randint(2,4)
        
    def move(self):
        self.rect.x += self.move_speed
        
    def reverse_enemies(self):
        if self.move_speed > 0:
            self.image = pygame.transform.flip(self.image,True,False)
    
    def turn_reverse(self):
        self.move_speed *= -1
                
    def update(self, x_shift):
        self.rect.x += x_shift
        self.aimation()
        self.reverse_enemies()
        self.move()