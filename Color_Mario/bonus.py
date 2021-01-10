import pygame
from random import *

#variable bonus :
piece=pygame.transform.scale(pygame.image.load('images/piece.png'),(30,30))
etoile=pygame.transform.scale(pygame.image.load('images/etoile.png'),(30,30))

class Bonus:
    def __init__(self,ecran,x,y):
        super().__init__()
        

        self.listeBonus = [piece,etoile]
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

    def effet(self,surface):
        if self.image == piece:
            return "piece"
        else :
            return "etoile"
    # cette fonction nous permet quand elle est appelé de change aleatoirement de bonus(etoile/ piece) 
    def bonusChange(self):
        self.image=choice(self.listeBonus)
