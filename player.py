import pygame

class Player:
    def __init__(self,ecran):
        self.x = 240
        self.y = 400
        self.image = pygame.transform.scale(pygame.image.load('images/player.png'),(30,30))
        self.ecran = ecran
        

    def mouvement ( self, vitesse):
        self.x+=vitesse 

    def affiche(self):
        self.ecran.blit(self.image,(self.x,self.y))
