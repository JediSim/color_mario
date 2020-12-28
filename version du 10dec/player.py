import pygame
from random import *

#variable players :
taod=pygame.transform.scale(pygame.image.load('images/player.png'),(30,30))
luigi=pygame.transform.scale(pygame.image.load('images/player1.png'),(30,30))
yochi=pygame.transform.scale(pygame.image.load('images/player2.png'),(30,30))



class Player:
    def __init__(self,ecran):
        super().__init__()
        

        self.listePlayers = [taod,luigi,yochi]

        self.x = 240
        self.y = 400
        self.image = choice(self.listePlayers)
        self.rect=self.image.get_rect()
        self.ecran = ecran

        if self.image==taod:
            self.color=(255,0,0)
        elif self.image==luigi:
            self.color=(0,255,0)
        else:
            self.color=(0,0,255)
        
        

    def mouvement ( self, vitesse):
        if self.x+vitesse<470 and self.x+vitesse>0 :
            self.x+=vitesse
        self.rect.x=self.x
        self.rect.y=self.y

    def affiche(self):
        self.rect.x=self.x
        self.rect.y=self.y
        self.ecran.blit(self.image,self.rect)

    def playerChange(self):
        imagePercede=self.image
        self.image = choice(self.listePlayers)
        #permet de pas retomber sur le meme personnage
        
        while imagePercede == self.image :
            self.image = choice(self.listePlayers)
            
        if self.image==taod:
            self.color=(255,0,0)
        elif self.image==luigi:
            self.color=(0,255,0)
        else:
            self.color=(0,0,255)
