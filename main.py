import pygame
import sys
from ennemi import Ennemi

class Jeu:
    def __init__(self):
        self.ecran = pygame.display.set_mode((1100, 600))
        pygame.display.set_caption('Color mario')
        self.jeu_encours = True
        self.ennemi_x = 600
        self.ennemi_y = 200
        self.taille = [32,64]
        self.ennemi = Ennemi(self.ennemi_x,self.ennemi_y,self.taille)

    def boucle_principale(self):
        # boucle principale du jeu

        while self.jeu_encours:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #mettre ici les evenements pour bouger 

            self.ecran.fill((255,255,255))
            self.ennemi.afficher(self.ecran)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
