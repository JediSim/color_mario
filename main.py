import pygame
import sys
from sol import Sol
from ennemi import Ennemi
from joueur import Joueur
from couleur import *
import time

imgjoueur=pygame.image.load('player.png')
class Jeu:
    def __init__(self):
        successes, failures = pygame.init()
        print("{0} successes and {1} failures".format(successes, failures))
        self.ecran = pygame.display.set_mode((1100, 600))
        pygame.display.set_caption('Color mario')
        self.jeu_encours = True
        self.taille = [32,64]
        
        #ennemi
        self.ennemi_x = 550
        self.ennemi_y = 0
        self.color = Couleur()
        self.ennemi = Ennemi(self.ennemi_x,self.ennemi_y,self.taille, self.color)
        self.gravite = (0,4) #pour impression joueur tombe
        self.resistance = (0,0)
        
        #joueur
        self.joueur_x = 550
        self.joueur_y = 550
        self.joueur_vitesse_x=0
        self.image = pygame.transform.scale(imgjoueur,(30,30))
        self.joueur = Joueur(self.joueur_x,self.joueur_y,self.image)
        
        #Sol
        self.sol=Sol()

    def boucle_principale(self):
        # boucle principale du jeu
        clock = pygame.time.Clock()
        FPS = 60 #frame par sec


        while self.jeu_encours:
            clock.tick(FPS)

            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    self.jeu_encours=False
                    
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.joueur_vitesse_x= -2     #deplacement touchent pressée 
                    if event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 2       
                if event.type==pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 0                # touche relachée 
                    if event.key==pygame.K_LEFT:
                        self.joueur_vitesse_x= 0
            if self.sol.rect.colliderect(self.ennemi.rect):
                self.ennemi.rect.y = 0
                self.ennemi.color.couleur()
            if self.joueur.rect.colliderect(self.ennemi.rect):
                print("collision")

            self.joueur.mouvement(self.joueur_vitesse_x)
            self.ecran.fill((255,255,255))
            self.ennemi.afficher(self.ecran)
            self.sol.afficher(self.ecran)
            self.gravite_jeu()
            self.joueur.afficher(self.ecran)
            
            pygame.display.flip()
            
    def gravite_jeu(self):
        self.ennemi.rect.y += self.gravite[1] + self.resistance[1]

if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()
