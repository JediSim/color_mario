import pygame
from random import *
from pygame.locals import*


#variables malus :
bomb=pygame.transform.scale(pygame.image.load('images/bomb.webp'),(30,30))
pieuvre=pygame.transform.scale(pygame.image.load('images/pieuvre.png'),(30,30))

class Malus(pygame.sprite.Sprite):

    def __init__(self,ecran,x,y):
        super().__init__()
        self.listeMalus = [bomb, pieuvre]
        self.x = x
        self.y=y
        self.image=choice(self.listeMalus)
        self.rect=self.image.get_rect()
        self.ecran=ecran

        
    def mouvement(self,vitesse):
        self.rect.y += vitesse

    def afficher(self):
        self.rect.x=self.x
        self.rect.y=self.y
        self.ecran.blit(self.image,self.rect)

    def effet(self):
        #si c'est la pieuvre on affiche des cercles noirs pour cacher le jeu 
        if self.image == pieuvre:
            for i in (1,10):
                pygame.draw.circle(ecran, (0,0,0),(randint(0,410),randint(0,410)),randint(5,20))

                


                
        
