import pygame
from game_data import levels

class Level_node(pygame.sprite.Sprite):
    def __init__(self,position,status,path):
        super().__init__()
        self.image = pygame.image.load(path)
        if status == 'lock':
            copy = self.image.copy()
            copy.fill('black',None,pygame.BLEND_RGB_MULT)
            self.image.blit(copy,(0,0))
        self.rect = self.image.get_rect(center = position) 
        
class Level_pointed(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.image.load('data/images/player/Idle/Idle_1.png')
        self.rect = self.image.get_rect(center = position)

class All_level:
    def __init__(self,start_level,unlock_level,surface,Show_level):
        self.bg = pygame.image.load('data/images/background.jpg')
        
        self.display_surface = surface
        self.current_level = start_level
        self.unlock_level =  unlock_level
        self.Show_level = Show_level
        
        self.setup_level_nodes()
        self.setup_level_pointer()
    
    def setup_level_nodes(self):
        self.level_nodes = pygame.sprite.Group()
        
        for index,level_node in enumerate(levels.values()):
            if index <= self.unlock_level:
                level = Level_node(level_node['position'],'unlock',level_node['level_image'])
            else:
                level = Level_node(level_node['position'],'lock',level_node['level_image'])
            
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
        if keys[pygame.K_SPACE]:
            self.Show_level(self.current_level)
    
    def update_level_pointer(self):
        self.pointer.sprite.rect.center = self.level_nodes.sprites()[self.current_level].rect.center
        
    
    def run(self):
        self.display_surface.blit(self.bg,(0,0))
        self.key_input()
        self.level_nodes.draw(self.display_surface)
        self.update_level_pointer()
        self.pointer.draw(self.display_surface)

       