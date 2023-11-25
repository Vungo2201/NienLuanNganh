from typing import Any
from Load import Import_Images
import pygame 

class Tile(pygame.sprite.Sprite):
	def __init__(self,size,x,y):
		super().__init__()
		self.image = pygame.Surface((size,size))
		self.image.fill('grey')
		self.rect = self.image.get_rect(topleft = (x,y))

	def update(self,x_shift):
		self.rect.x += x_shift

class StaticTile(Tile):
	def __init__(self, size, x, y, surface):
		super().__init__(size, x, y)
		self.image = surface

class AnimeTile(Tile):
	def __init__(self,size, x, y, path):
		super().__init__(size, x, y)
		self.frames = Import_Images(path)
		self.frames_index = 0
		self.image = self.frames[self.frames_index]
  
	def aimation(self):
		self.frames_index += 0.2
		if self.frames_index >= len(self.frames):
			self.frames_index = 0
		self.image = self.frames[int(self.frames_index)]
  
	def update(self, x_shift):
		self.aimation()
		self.rect.x += x_shift
