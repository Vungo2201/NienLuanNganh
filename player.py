from Load import Import_Images
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        #player di chuyen
        self.speed_jump = -16
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.current_x = 0
        
        #hoat anh player
        self.player_right = True
        self.player_current_action = 'Idle'
        self.player_image_index = 0
        self.animation_speed  = 0.1
        self.on_top = False
        self.on_bottom = False
        self.on_left = False
        self.on_right = False
        
        #hinh anh player
        self.Player_assets()
        self.image = self.player_action['Idle'][self.player_image_index]
        self.rect = self.image.get_rect(topleft = pos)
    
    def Player_assets(self):
        path = 'data/images/player'
        self.player_action = {'Fall':[],'Run':[],'Hit':[],'Jump':[],'Idle':[]}
        
        for animation in self.player_action.keys():
            image_Path = path + '/' + animation
            self.player_action[animation] = Import_Images(image_Path)
            
    def player_animation(self):
        animation = self.player_action[self.player_current_action]
        
        self.player_image_index += self.animation_speed
        if(self.player_image_index >= len(animation)):
            self.player_image_index = 0
        
        image = animation[int(self.player_image_index)]
        if self.player_right:
            self.image = image
        else:
            left_image = pygame.transform.flip(image,True,False)
            self.image = left_image
       
        #can chinh rect
        if self.on_bottom  and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_bottom  and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_bottom:
            self.rect =  self.image.get_rect(midbottom = self.rect.midbottom) 
        elif self.on_top and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_top and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_top:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)
        
    def get_current_action(self):
        if self.direction.y < 0:
            self.player_current_action = 'Jump'
        elif self.direction.y > 1:
            self.player_current_action = 'Fall'
        else:
            if self.direction.x != 0:
                self.player_current_action = 'Run'
            else:
                self.player_current_action = 'Idle'
            
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.player_right = True
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.player_right = False
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE] and self.on_bottom:
            self.player_jump()
            
    def player_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
            
    def player_jump(self):
        self.direction.y = self.speed_jump
    
    def update(self):
        self.get_current_action()
        self.get_input()
        self.player_animation()
    
        
   