import pygame

class User_Interface:
    def __init__(self,surface):
        
        self.display_surface = surface
        
        self.life = pygame.image.load('data/images/Item/life.png')
        
        self.apple = pygame.image.load('data/images/Item/apple/Apple_1.png') 
        
    def display_life(self,amount):
        self.display_surface.blit(self.life,(30,20))
        self.display_surface.blit(pygame.font.Font(None,40).render('x ' + str(amount),True,'black'),(67,24))
    
    def display_apple(self,amount):
        self.display_surface.blit(self.apple,(15,50))
        self.display_surface.blit(pygame.font.Font(None,40).render('x ' + str(amount),True,'black'),(67,65))
    
    