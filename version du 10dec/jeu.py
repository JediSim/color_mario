import pygame
from bouton import*
from menu import*
from player import*
from ennemi import*
from sol import*
from random import*
from score import*
from gameover import*

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
        self.ennemi = Ennemi(randint(80,410),0,[90,30])
        self.ennemi1=Ennemi(randint(70,430),0,[70,20])
        self.tabennemi=[self.ennemi, self.ennemi1]
        self.gravite = (0,7.5)                          #pour impression joueur tombe
        self.resistance = (0,0)

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
               
               
            for i in   self.tabennemi:

                if self.sol.rect.colliderect(i.rect): # detecter que l'obstacle arrive en bas de l'ecran
                    i.rect.y = 0
                    i.color.couleur()
                    i.rect.x = randint(80,410)
                    self.score.point += 0.5
                if self.player.rect.colliderect(i.rect) :    # collision entre l'ennemi et le joueur 
                    if not i.color.color == self.player.color :
                        if self.score.isBestScore():
                            self.score.ajouterBestScore()
                        gameover = Gameover(self.ecran,self.menu,self.score)
                        gameover.run()
                        
                
            if self.score.point == score5:
                self.player.playerChange()
                score5 = self.score.point + 5
                
            for i in   self.tabennemi:
               i.mouvement(self.ennemi_vitesse_y)
           

            self.player.mouvement(self.joueur_vitesse_x)
           
            self.ecran.blit(self.image_fond,(0,0))
            #self.ecran.fill((255,255,255))
            
            self.score.afficherBestScore()
            self.score.afficher()

           
            self.sol.afficher(self.ecran)
            self.gravite_jeu()
            self.player.affiche()
            
            for i in   self.tabennemi:
                i.afficher(self.ecran)

            pygame.display.update()

    def gravite_jeu(self):
        for i in self.tabennemi:
            i.rect.y += self.gravite[1] + self.resistance[1]


