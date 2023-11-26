import pygame
from game_data import levels
from Load import *
from tiles import *
from enemies import Enimies
from setting import  tile_size, screen_width,screen_height
from player import Player
class Level:
    def __init__(self,current_level,surface,New_All_level,pick_apple):
        self.display_surface = surface
        self.current_level = current_level
        level_data = levels[current_level]
        self.new_max_level = level_data['unlock_level']
        self.New_All_level = New_All_level
        
        enemies = load_csv_map(level_data['enemies'])
        box = load_csv_map(level_data['box'])
        terrain = load_csv_map(level_data['terrain'])
        apple = load_csv_map(level_data['apple'])
        block_enemies = load_csv_map(level_data['block_enemies'])
        cloud = load_csv_map(level_data['cloud'])
        player = load_csv_map(level_data['start'])
        goal = load_csv_map(level_data['end'])
        
        self.terrain_sprites = self.set_level(terrain,'terrain')
        self.apple_sprites = self.set_level(apple,'apple')
        self.box_sprites = self.set_level(box,'item')
        self.enemies_sprites = self.set_level(enemies,'enemies')
        self.block_enemies_sprites = self.set_level(block_enemies,'block_enemies')
        self.cloud = self.set_level(cloud,'cloud')
        self.goal_sprites = self.set_object(goal,'goal')
        self.player = self.set_object(player,'player')
        
        self.pick_apple = pick_apple
       
        self.world_shift = 0
        self.current_x = 0
    
    def set_level(self,layout,type):
        sprites_group =  pygame.sprite.Group()
   
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    if type == 'terrain':
                        tile_list_terrain = image_load('data/images/Terrain/Terrain (16x16).png')
                        tile_surface = tile_list_terrain[int(cell)]
                        tile = StaticTile(tile_size,x,y,tile_surface)
                    if type == 'enemies':
                        tile = Enimies(tile_size,x,y)
                    if type == 'apple':
                        tile = AnimeTile(tile_size,x,y,'data/images/Item/apple')
                    if type == 'item':
                        tile_surface = PyGame.image.load('data/images/Item/box.png').convert_alpha()
                        tile = StaticTile(tile_size,x,y,tile_surface)
                    if type == 'cloud':
                        tile_surface = PyGame.image.load('data/images/Item/cloud.png').convert_alpha()
                        tile = StaticTile(tile_size,x,y,tile_surface)
                    if type == 'block_enemies':
                        tile = Tile(tile_size,x,y)
                        
                    sprites_group.add(tile)
  
        return sprites_group
 
    def set_object(self,layout,type):
        sprite =  pygame.sprite.GroupSingle()
        
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                if cell != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    if type == 'goal':
                        goal = pygame.image.load('data/images/Item/End (Idle).png')
                        tile = StaticTile(tile_size,x,y,goal)
                    if type == 'player':
                        tile = Player((x,y))
                    sprite.add(tile)
                    
        return sprite    
    
     
    def enemies_block_colloision(self):
        for enemie in self.enemies_sprites.sprites():
            if pygame.sprite.spritecollide(enemie,self.block_enemies_sprites,False):
                enemie.turn_reverse()
    
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < screen_width / 6 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 6) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
    
    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x  = player.rect.right
        
        for sprite in self.box_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0: 
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x  = player.rect.right
        
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0 ):    
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False
        	
    def vertical_collision(self):
        player = self.player.sprite
        player.player_gravity()
        for sprite in self.box_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_bottom = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_top = True

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0: 
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_bottom = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_top = True
        
        if player.on_bottom and player.direction.y < 0 or player.direction.y > 1:
            player.on_bottom = False
        if player.on_top and player.direction.y > 0:
            player.on_top = False
            
    def check_pick_apple(self):
        pick_apples = pygame.sprite.spritecollide(self.player.sprite,self.apple_sprites,True)
        if pick_apples:
            for apple in pick_apples:
                self.pick_apple()
    
    def death(self):
        if self.player.sprite.rect.top > screen_height:
             self.New_All_level(self.current_level,self.current_level)
            
    def win(self):
        if pygame.sprite.spritecollide(self.player.sprite,self.goal_sprites,False):
             self.New_All_level(self.current_level,self.new_max_level)
            
            
        
    def run(self):
        self.apple_sprites.draw(self.display_surface)
        self.apple_sprites.update(self.world_shift)
        
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.world_shift)
        
        self.box_sprites.draw(self.display_surface)
        self.box_sprites.update(self.world_shift)
        
        self.enemies_sprites.draw(self.display_surface)
        self.enemies_sprites.update(self.world_shift)
        
        self.block_enemies_sprites.draw(self.display_surface)
        self.block_enemies_sprites.update(self.world_shift)
        
        self.goal_sprites.draw(self.display_surface)
        self.goal_sprites.update(self.world_shift)
        
        self.cloud.draw(self.display_surface)
        self.cloud.update(self.world_shift)
        
        self.player.update()
        self.player.draw(self.display_surface)
        
        self.scroll_x()
        self.enemies_block_colloision()
        self.horizontal_collision()
        self.vertical_collision()
        self.check_pick_apple()
        self.death()
        self.win()
   
                    
                    
        
   
            
   