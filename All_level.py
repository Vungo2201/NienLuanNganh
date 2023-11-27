import pygame
from game_data import levels

class Level_node(pygame.sprite.Sprite):
    def __init__(self,position,status,path,pointer_speed):
        super().__init__()
        self.image = pygame.image.load(path)
        if status == 'lock':
            copy = self.image.copy()
            copy.fill('black',None,pygame.BLEND_RGB_MULT)
            self.image.blit(copy,(0,0))
        self.rect = self.image.get_rect(center = position) 
        self.zone = pygame.Rect(self.rect.centerx - (pointer_speed/2),self.rect.centery - (pointer_speed/2),pointer_speed,pointer_speed)
class Level_pointed(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.image = pygame.image.load('data/images/player/Idle/Idle_1.png')
        self.rect = self.image.get_rect(center = position)
        
    def update(self):
        self.rect.center = self.position

class All_level:
    def __init__(self,start_level,unlock_level,surface,Show_level):
        self.bg = pygame.image.load('data/images/background.jpg')
        
        self.display_surface = surface
        self.current_level = start_level
        self.unlock_level =  unlock_level
        self.Show_level = Show_level
        
        self.moving = False
        self.move_pointer_direction = pygame.math.Vector2(0,0)
        self.move_pointer_speed = 8
        
        self.start_time = pygame.time.get_ticks()
        self.inputable = False
        self.time_block = 450
        
        self.setup_level_nodes()
        self.setup_level_pointer()
    
    def setup_level_nodes(self):
        self.level_nodes = pygame.sprite.Group()
        
        for index,level_node in enumerate(levels.values()):
            if index <= self.unlock_level:
                level = Level_node(level_node['position'],'unlock',level_node['level_image'],self.move_pointer_speed)
            else:
                level = Level_node(level_node['position'],'lock',level_node['level_image'],self.move_pointer_speed)
            
            self.level_nodes.add(level)
            
    def setup_level_pointer(self):
        self.pointer = pygame.sprite.GroupSingle()
        pointer_sprite = Level_pointed(self.level_nodes.sprites()[self.current_level].rect.center)
        self.pointer.add(pointer_sprite)        
    
    def key_input(self):
        keys = pygame.key.get_pressed()
        
        if not self.moving and self.inputable:
            if keys[pygame.K_RIGHT] and self.current_level < self.unlock_level:
                self.move_pointer_direction = self.get_move_pointer('next')
                self.current_level += 1
                self.moving = True
            if keys[pygame.K_LEFT] and self.current_level > 0:
                self.move_pointer_direction = self.get_move_pointer('back')
                self.current_level -= 1
                self.moving = True
            if keys[pygame.K_SPACE]:
                self.Show_level(self.current_level)

    
    def get_move_pointer(self,type):
        start_pointer = pygame.math.Vector2(self.level_nodes.sprites()[self.current_level].rect.center)
        if type == 'next':
            end_pointer = pygame.math.Vector2(self.level_nodes.sprites()[self.current_level + 1].rect.center)
        else:  end_pointer = pygame.math.Vector2(self.level_nodes.sprites()[self.current_level - 1].rect.center)
        
        return (end_pointer - start_pointer).normalize()
    
    def update_level_pointer(self):
        if self.moving and self.move_pointer_direction:
            self.pointer.sprite.position += self.move_pointer_direction * self.move_pointer_speed
            target = self.level_nodes.sprites()[self.current_level]
            if target.zone.collidepoint(self.pointer.sprite.position):
                self.moving = False
                self.move_pointer_direction = pygame.math.Vector2(0,0)
    
    def time_input(self):
        if not self.inputable:
            cur_time = pygame.time.get_ticks()
            if cur_time - self.start_time >= self.time_block:
                self.inputable = True
    
    def run(self):
        self.display_surface.blit(self.bg,(0,0))
        self.key_input()
        self.pointer.update()
        self.level_nodes.draw(self.display_surface)
        self.update_level_pointer()
        self.pointer.draw(self.display_surface)
        self.time_input()

       