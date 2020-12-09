import pygame
from random import *

class Couleur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #variable couleur :
        noir = (0,0,0)
        blanc = (255,255,255)
        rouge = (255,0,0)
        vert = (0,255,0)
        bleu = (0,0,255)
        self.listeColor = [noir, blanc, rouge, vert, bleu]
        self.color = choice(self.listeColor)

    def couleur(self):
        self.color = choice(self.listeColor)
        
        
