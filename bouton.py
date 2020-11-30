import pygame

class Bouton:
    def __init__(self,abs,ord,long,large,ecran):
        self.rect = pygame.Rect(abs, ord, long, large)
        self.ecran = ecran

        corpsBouton = pygame.draw.rect(self.ecran,(0,0,0),self.rect)

        self.mouse_pos = pygame.mouse.get_pos()
        self.isClique = corpsBouton.collidepoint(self.mouse_pos)


