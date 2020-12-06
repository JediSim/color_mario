import pygame

class Player:
    def __init__(self,ecran):
        self.x = 240
        self.y = 400
        self.image = pygame.transform.scale(pygame.image.load('images/player.png'),(30,30))
        self.rect=self.image.get_rect()
        self.ecran = ecran
        

    def mouvement ( self, vitesse):
        self.x+=vitesse
        self.rect.x=self.x
        self.rect.y=self.y

    def affiche(self):
       self.rect.x=self.x
        self.rect.y=self.y
        surface.blit(self.image,self.rect)
