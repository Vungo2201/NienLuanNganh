import pygame 
from tiles import Tile 
from setting import  tile_size
from player import Player
class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.set_level(level_data)
        
    def set_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
				
                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
        
    def run(self):
        self.tiles.update(0)
        self.tiles.draw(self.display_surface)
        
        self.player.update()
        self.player.draw(self.display_surface)
        