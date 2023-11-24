from os import walk
import pygame as PyGame
def Import_Player_Images(path):
    image_list = []
    for _,__,imgages in walk(path):
        for imgage in imgages:
            imgage_path = path + '/' + imgage
            imgage_load = PyGame.image.load(imgage_path).convert_alpha()
            image_list.append(imgage_load)
    return image_list

