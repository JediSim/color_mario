import pygame
import sys
from ennemi import Ennemi
from joueur import Joueur

class Jeu:
    def __init__(self):
        self.ecran = pygame.display.set_mode((1100, 600))
        pygame.display.set_caption('Color mario')
        self.jeu_encours = True
        self.ennemi_x = 600
        self.ennemi_y = 200
        self.taille = [32,64]
        self.ennemi = Ennemi(self.ennemi_x,self.ennemi_y,self.taille)
        #joueur
        self.joueur_x = 600
        self.joueur_y = 200
        self.joueur_vitesse_x=0
        self.taille = [32,64]
        self.joueur = Joueur(self.joueur_x,self.joueur_y,self.taille)

    def boucle_principale(self):
        # boucle principale du jeu

        while self.jeu_encours:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.joueur_vitesse_x= -1      #deplacement touchent pressée 
                    if event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 1       
                if event.type==pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 0                # touche relachée 
                    if event.key==pygame.K_LEFT:
                        self.joueur_vitesse_x= 0
                        

            self.joueur.mouvement(self.joueur_vitesse_x)
            self.ecran.fill((255,255,255))
            self.joueur.afficher(self.ecran)
            
            self.ennemi.afficher(self.ecran)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()


