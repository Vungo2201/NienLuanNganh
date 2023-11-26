import pygame
from game_data import levels

class Level_node(pygame.sprite.Sprite):
    def __init__(self,position,status):
        super().__init__()
        self.image = pygame.Surface((150,100))
        if status == 'unlock':
            self.image.fill('red')
        else: self.image.fill('black')
        self.rect = self.image.get_rect(center = position) 
        
class Level_pointed(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.Surface((25,25))
        self.image.fill('yellow')
        self.rect = self.image.get_rect(center = position)

class All_level:
    def __init__(self,start_level,unlock_level,surface):
        
        self.display_surface = surface
        self.current_level = start_level
        self.unlock_level =  unlock_level
        
        self.setup_level_nodes()
        self.setup_level_pointer()
    
    def setup_level_nodes(self):
        self.level_nodes = pygame.sprite.Group()
        
        for index,level_node in enumerate(levels.values()):
            if index <= self.unlock_level:
                level = Level_node(level_node['position'],'unlock')
            else:
                level = Level_node(level_node['position'],'lock')
            
            self.level_nodes.add(level)
            
    def setup_level_pointer(self):
        self.pointer = pygame.sprite.GroupSingle()
        pointer_sprite = Level_pointed(self.level_nodes.sprites()[self.current_level].rect.center)
        self.pointer.add(pointer_sprite)        
    
    def key_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT] and self.current_level < self.unlock_level:
            self.current_level += 1
        if keys[pygame.K_LEFT] and self.current_level > 0:
            self.current_level -= 1
    
    def update_level_pointer(self):
        self.pointer.sprite.rect.center = self.level_nodes.sprites()[self.current_level].rect.center
        
    
    def run(self):
        self.key_input()
        self.level_nodes.draw(self.display_surface)
        self.update_level_pointer()
        self.pointer.draw(self.display_surface)

       