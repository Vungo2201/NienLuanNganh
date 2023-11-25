from os import walk
from setting import tile_size
from csv import reader
import pygame as PyGame
def Import_Images(path):
    image_list = []
    for _,__,imgages in walk(path):
        for imgage in imgages:
            imgage_path = path + '/' + imgage
            imgage_load = PyGame.image.load(imgage_path).convert_alpha()
            image_list.append(imgage_load)
    return image_list

def load_csv_map(path):
    loaded_map = []
    with open(path) as map:
        level = reader(map,delimiter= ',')
        for row in level:
            loaded_map.append(list(row))
            
        return loaded_map

def image_load(path):
    tiles = []
    image = PyGame.image.load(path).convert_alpha()
    number_tile_x = int(image.get_size()[0]/ tile_size)
    number_tile_y = int(image.get_size()[1]/ tile_size)
  
    for row in range(number_tile_y):
        for col in range(number_tile_x):
            x = col * tile_size
            y = row * tile_size
            new_image =  PyGame.Surface((tile_size,tile_size))
            new_image.blit(image,(0,0),PyGame.Rect(x,y,tile_size,tile_size))
            tiles.append(new_image)

    return tiles

        
        
