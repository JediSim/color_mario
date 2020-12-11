import pygame
from bouton import*
from menu import*
from player import*
from ennemi import*
from sol import*
from random import*
from score import*

class Jeu:
    def __init__(self,ecran,menu):
        self.image_fond = pygame.image.load("images/fondmario.jpg")
        self.ecran = ecran
        self.FPS = 30
        self.clock = pygame.time.Clock()
        self.menu = menu
        self.score = Score(ecran)

        #----------joueur------------
        self.joueur_vitesse_x = 0
        self.player = Player(ecran)

        #----------ennemi------------
        self.ennemi_vitesse_y = 2
        self.ennemi = Ennemi(randint(50,450),0,[32,64])
        self.gravite = (0,4) #pour impression joueur tombe
        self.resistance = (0,0)

        #--------------Sol-----------
        self.sol=Sol()

        #self.bouton_quit = Bouton(10,450,75,30,ecran)
        
    def run(self):
        self.ecran.blit(self.image_fond,(0,0))
        self.player.affiche()
        quitter = False
        while not quitter:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pouvoir quitter la ecran 
                    RUNNING = False
                    quitter = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.joueur_vitesse_x= -5
                    elif event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 5
                elif event.type==pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.joueur_vitesse_x= 0                # touche relachée 
                    elif event.key==pygame.K_LEFT:
                        self.joueur_vitesse_x= 0

            if self.sol.rect.colliderect(self.ennemi.rect):
                self.ennemi.rect.y = 0
                self.ennemi.color.couleur()
                self.ennemi.rect.x = randint(50,450)
                self.score.point += 1
            if self.player.rect.colliderect(self.ennemi.rect):    # collision entre l'ennemi et le joueur 
                self.menu.run()


            self.player.mouvement(self.joueur_vitesse_x)
            self.ennemi.mouvement(self.ennemi_vitesse_y)
            self.ecran.blit(self.image_fond,(0,0))
            #self.ecran.fill((255,255,255))

            self.score.afficher()

            self.ennemi.afficher(self.ecran)
            self.sol.afficher(self.ecran)
            self.gravite_jeu()

            self.player.affiche()

            pygame.display.update()

    def gravite_jeu(self):
        self.ennemi.rect.y += self.gravite[1] + self.resistance[1]

