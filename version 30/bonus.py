import pygame
from random import *

#variable players :
piece=pygame.transform.scale(pygame.image.load('images/piece.png'),(30,30))

class Bonus:
    def __init__(self,ecran,x,y):
        super().__init__()
        

        self.listeBonus = [piece]
        self.x = x
        self.y=y
        self.image = choice(self.listeBonus)
        self.rect=self.image.get_rect()
        self.ecran = ecran
        
        

    def mouvement(self,vitesse):
        self.rect.y += vitesse

    def afficher(self):
        self.rect.x=self.x
        self.rect.y=self.y
        self.ecran.blit(self.image,self.rect)
