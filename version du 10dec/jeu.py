import pygame
from bouton import*
from menu import*
from player import*
from ennemi import*
from sol import*
from random import*
from score import*
from gameover import*
from malus import *

class Jeu:
    def __init__(self,ecran,menu):
        self.image_fond = pygame.image.load("images/fondmario.jpg")
        self.ecran = ecran
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.menu = menu
        #-----------affichage du score-----------
        self.score = Score(ecran)

        #----------joueur------------
        self.joueur_vitesse_x = 0
        self.player = Player(ecran)

        #----------ennemi------------
        self.ennemi_vitesse_y = 2
        self.ennemi = Ennemi(randint(80,410),0,[90,30]) #permet de faire varier les tailles 
        self.ennemi1=Ennemi(randint(70,430),0,[70,20])  #ajouter un deuxième ennemi
        self.tabennemi=[self.ennemi, self.ennemi1]

        #variable de la gravite 
        self.gravite = (0,7.5)                          #pour impression joueur tombe
        self.resistance = (0,0)

        #---------- malus -----------
        self.malus_vitesse_y = 4
        self.malus = Malus(ecran,randint(80,410),0)
    
        #--------------Sol-----------
        self.sol=Sol()

        #self.bouton_quit = Bouton(10,450,75,30,ecran)
        
    def run(self):
        self.ecran.blit(self.image_fond,(0,0))
        #----affichage du joueur ------
        self.player.affiche()
        score5 = self.score.point + 5
        quitter = False
        while not quitter:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pouvoir quitter la ecran 
                    RUNNING = False
                    quitter = True
                elif event.type == pygame.KEYDOWN: # touches presse 
                    if event.key == pygame.K_LEFT:
                        self.joueur_vitesse_x= -5
                    elif event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 5
                    
                elif event.type==pygame.KEYUP:  # touche relachée 
                    if event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 0               
                    elif event.key==pygame.K_LEFT:
                        self.joueur_vitesse_x= 0
                    elif event.key == pygame.K_SPACE:
                        self.player.playerChange()
               

            #les collisions des ennemis
            for i in   self.tabennemi:
                

                # l'obstacle arrive en bas de l'ecran
                if self.sol.rect.colliderect(i.rect): 
                    i.rect.y = 0
                    i.color.couleur()
                    i.rect.x = randint(80,410)
                    self.score.point += 0.5

                # collision entre l'ennemi et le joueur 
                if self.player.rect.colliderect(i.rect) :    
                    if not i.color.color == self.player.color :
                        if self.score.isBestScore():
                            self.score.ajouterBestScore()
                        gameover = Gameover(self.ecran,self.menu,self.score)
                        gameover.run()

            #collisions des malus
                #si le malus arrive en bas :

            if self.sol.rect.colliderect(self.malus.rect):
                    self.malus = Malus(ecran,randint(80,410),0)

                #collision entre un malus et le joueur
            if self.player.rect.colliderect(self.malus.rect):
                    self.malus.effet()


            #gestion changement joueur 
            if self.score.point == score5:
                self.player.playerChange()
                score5 = self.score.point + 5

            #mouvement ennemi
            for i in   self.tabennemi:
               i.mouvement(self.ennemi_vitesse_y)
           
            #mouvement malus
            self.malus.mouvement(self.malus_vitesse_y)

            #mouvement joueur
            self.player.mouvement(self.joueur_vitesse_x)

            #affichage de l'ecran
            self.ecran.blit(self.image_fond,(0,0))
            #self.ecran.fill((255,255,255))

            #affichage du score
            self.score.afficherBestScore()
            self.score.afficher()

            #affichage du score
            self.sol.afficher(self.ecran)
            self.gravite_jeu()
            self.player.affiche()

            #affichage des ennemis
            for i in   self.tabennemi:
                i.afficher(self.ecran)

            #affichage malus
            self.malus.afficher()

                                 
            pygame.display.update()

    def gravite_jeu(self):
        for i in self.tabennemi:
            i.rect.y += self.gravite[1] + self.resistance[1]
        self.malus.rect.y += self.gravite[1] + self.resistance[1]


