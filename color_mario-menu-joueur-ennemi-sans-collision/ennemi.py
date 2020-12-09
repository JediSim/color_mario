import pygame
from pygame.locals import*
from couleur import*


class Ennemi(pygame.sprite.Sprite):
    def __init__(self, x, y, taille):

        super().__init__()
        self.x = x
        self.y = y
        self.taille = taille
        self.rect = pygame.Rect(self.x, self.y, self.taille[0], self.taille[1])
        self.color = Couleur()


    def mouvement(self, vitesse):
        self.rect.y += vitesse
        
    def afficher(self, surface):
        pygame.draw.rect(surface, self.color.color, self.rect)
        
