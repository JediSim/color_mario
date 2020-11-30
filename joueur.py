import pygame
import math

class Joueur (pygame.sprite.Sprite):
    def __init__ (self,x,y,image):

        super().__init__()
        self.x=x
        self.y=y
        self.image=image
        self.rect=image.get_rect()
        

    def afficher(self,surface):
        self.rect.x=self.x
        self.rect.y=self.y
        surface.blit(self.image,self.rect)
        
    def mouvement ( self, vitesse):
        self.x+=vitesse
        self.rect.x=self.x
        self.rect.y=self.y

       
