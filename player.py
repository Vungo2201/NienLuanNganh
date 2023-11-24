from Load import Import_Player_Images
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.Player_assets()
        self.speed_jump = -16
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.player_image_index = 0
        self.animation_speed  = 0.2
        self.image = self.player_action['Run'][self.player_image_index]
        self.rect = self.image.get_rect(topleft = pos)
    
    def Player_assets(self):
        path = 'data/images/player'
        self.player_action = {'Fall':[],'Run':[],'Hit':[],'Jump':[],'Idle':[]}
        
        for animation in self.player_action.keys():
            image_Path = path + '/' + animation
            self.player_action[animation] = Import_Player_Images(image_Path)
            
    def player_animation(self):
        animation = self.player_action['Run']
        
        self.player_image_index += self.animation_speed
        if(self.player_image_index >= len(animation)):
            self.player_image_index = 0
        
        self.image = animation[int(self.player_image_index)]

            
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE]:
            self.player_jump()
            
    def player_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
            
    def player_jump(self):
        self.direction.y = self.speed_jump
    
    def update(self):
        self.get_input()
        self.player_animation()
    
        
   