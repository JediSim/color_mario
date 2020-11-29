import pygame
import math 
from joueur import Joueur

class Cercle (pygame.sprite.Sprite):
    def __init__(self,x,y,rayon):
        super().__init__()
        # x et y les coordonné du centre du cercle
        self.x=x 
        self.y=y
        self.rayon=rayon

    def etreDansCercle(self,xj,yj):
        
        d=math.sqrt((math.pow(self.x-xj,2))+(math.pow(self.y-yj,2)))
        if self.rayon+1>d:
            res=True
        else :
            res=False
        return res
    
    def afficherCercle (self,surface):
        pygame.draw.circle(surface,(255,0,0),(self.x,self.y),self.rayon)
    


    
