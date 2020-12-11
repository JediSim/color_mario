import pygame

class Score:
    def __init__(self,ecran):
        self.ecran = ecran
        self.point = 0
        self.couleurTexte = (0,0,0)
        self.x = 450
        self.y = 5

    def afficher(self):
        font=pygame.font.Font(None, 24)
        champs = font.render(str(self.point),1,self.couleurTexte)
        self.ecran.blit(champs,(self.x,self.y))