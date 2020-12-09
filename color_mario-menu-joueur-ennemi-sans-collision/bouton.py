import pygame

class Bouton:
    def __init__(self,abs,ord,long,large,ecran,texte,couleurTexte):
        self.rect = pygame.Rect(abs, ord, long, large)
        self.ecran = ecran

        font=pygame.font.Font(None, 24)
        self.champs = font.render(texte,1,couleurTexte)

        corpsBouton = pygame.draw.rect(self.ecran,(0,0,0),self.rect)
        ecran.blit(self.champs,(abs+3,ord+3))

        self.mouse_pos = pygame.mouse.get_pos()
        self.isClique = corpsBouton.collidepoint(self.mouse_pos)


