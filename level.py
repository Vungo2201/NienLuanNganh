import pygame 
from Load import *
from tiles import *
from enemies import Enimies
from setting import  tile_size, screen_width
# from player import Player
class Level:
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
        
        self.enemies_block_colloision()
    def __init__(self,level_data,surface):
        self.display_surface = surface

        enemies = load_csv_map(level_data['enemies'])
        box = load_csv_map(level_data['box'])
        terrain = load_csv_map(level_data['terrain'])
        apple = load_csv_map(level_data['apple'])
        block_enemies = load_csv_map(level_data['block_enemies'])
        
        self.terrain_sprites = self.set_level(terrain,'terrain')
        self.apple_sprites = self.set_level(apple,'apple')
        self.box_sprites = self.set_level(box,'item')
        self.enemies_sprites = self.set_level(enemies,'enemies')
        self.block_enemies_sprites = self.set_level(block_enemies,'block_enemies')
       
        self.world_shift = -1
    #     self.current_x = 0
        
    def set_level(self,layout,type):
        sprites_group =  pygame.sprite.Group()
    #     self.tiles = pygame.sprite.Group()
    #     self.player = pygame.sprite.GroupSingle()

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
                        tile = tile = StaticTile(tile_size,x,y,tile_surface)
                    if type == 'block_enemies':
                        tile = Tile(tile_size,x,y)
                        
                    sprites_group.add(tile)
    #             if cell == 'P':
    #                 player_sprite = Player((x,y))
    #                 self.player.add(player_sprite)
        return sprites_group
    
    def enemies_block_colloision(self):
        for enemie in self.enemies_sprites.sprites():
            if pygame.sprite.spritecollide(enemie,self.block_enemies_sprites,False):
                enemie.turn_reverse()
    
    # def scroll_x(self):
    #     player = self.player.sprite
    #     player_x = player.rect.centerx
    #     direction_x = player.direction.x
        
    #     if player_x < screen_width / 6 and direction_x < 0:
    #         self.world_shift = 8
    #         player.speed = 0
    #     elif player_x > screen_width - (screen_width / 6) and direction_x > 0:
    #         self.world_shift = -8
    #         player.speed = 0
    #     else:
    #         self.world_shift = 0
    #         player.speed = 8
    
    # def horizontal_collision(self):
    #     player = self.player.sprite
    #     player.rect.x += player.direction.x * player.speed
    #     for sprite in self.tiles.sprites():
    #         if sprite.rect.colliderect(player.rect):
    #             if player.direction.x < 0: 
    #                 player.rect.left = sprite.rect.right
    #                 player.on_left = True
    #                 self.current_x = player.rect.left
    #             elif player.direction.x > 0:
    #                 player.rect.right = sprite.rect.left
    #                 player.on_right = True
    #                 self.current_x  = player.rect.right
        
    #     if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0 ):    
    #         player.on_left = False
    #     if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
    #         player.on_right = False
        	
    # def vertical_collision(self):
    #     player = self.player.sprite
    #     player.player_gravity()
    #     for sprite in self.tiles.sprites():
    #         if sprite.rect.colliderect(player.rect):
    #             if player.direction.y > 0: 
    #                 player.rect.bottom = sprite.rect.top
    #                 player.direction.y = 0
    #                 player.on_bottom = True
    #             elif player.direction.y < 0:
    #                 player.rect.top = sprite.rect.bottom
    #                 player.direction.y = 0
    #                 player.on_top = True
        
    #     if player.on_bottom and player.direction.y < 0 or player.direction.y > 1:
    #         player.on_bottom = False
    #     if player.on_top and player.direction.y > 0:
    #         player.on_top = False
            
    # def run(self):
    #     self.tiles.update(self.world_shift)
    #     self.tiles.draw(self.display_surface)
    #     self.horizontal_collision()
    #     self.vertical_collision()
    #     self.player.update()
    #     self.player.draw(self.display_surface)
    #     self.scroll_x() '''