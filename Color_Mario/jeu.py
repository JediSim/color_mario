#importation de toutes nos classes 
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
from bonus import *


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
        self.player_vitesse_x = 0
        self.player = Player(ecran)

        #----------ennemi------------
        self.taille=140
        self.taille1=100
        self.ennemi_vitesse_y = 2
        self.ennemi = Ennemi(randint(80,410),0,[self.taille,30]) #permet de faire varier les tailles 
        self.ennemi1=Ennemi(randint(70,430),0,[self.taille1,30])  #ajouter un deuxième ennemi
        #tableau d'ennemis -------------------------------------------------------------------
        self.tabennemi=[self.ennemi, self.ennemi1]

        #variable de la gravite
        self.valeurG=7.5
        self.gravite = (0,self.valeurG)  #pour impression joueur tombe
        self.resistance = (0,0)

        #---------- malus -----------
        self.malus_vitesse_y = 4
        self.malus = Malus(ecran,randint(80,410),0)

        #----------- bonus ----------
        self.bonus_vitesse_y = 6
        self.bonus = Bonus(ecran,randint(80,410),0)
        #--------------Sol-----------
        self.sol=Sol()
        
    def run(self):
        self.ecran.blit(self.image_fond,(0,0))
        
        # ---------------variables ----------------
        
        res_score=True
        res_score1=True
        
        toucher_bomb=False
        bomb_temps=0
        
        score4=4
        
        rep=randint(0,1)
        #----affichage du joueur ------
        self.player.affiche()
        
        quitter = False
        
        while not quitter:
            self.clock.tick(self.FPS)
            rep=randint(0,1)
            
            for event in pygame.event.get():
                # -------------pouvoir quitter la ecran ---------------
                if event.type == pygame.QUIT: 
                    RUNNING = False
                    quitter = True
                #----------- les touches sont pressées  ------------------
                elif event.type == pygame.KEYDOWN: 
                # deplacement du joueur a gauche ou a droite ------------ 
                    if event.key == pygame.K_LEFT:
                        self.player_vitesse_x= - self.player.vitesseX
                    elif event.key == pygame.K_RIGHT:
                        self.player_vitesse_x= self.player.vitesseX
                 
                #-------------les touches sont relachées ----------------
                elif event.type==pygame.KEYUP: 
                    if event.key == pygame.K_RIGHT:
                        self.player_vitesse_x= 0               
                    elif event.key==pygame.K_LEFT:
                        self.player_vitesse_x= 0
                 # changement de joueur ------------------------
                    elif event.key == pygame.K_SPACE:
                        self.player.playerChange()
               

            #--------------les collisions des ennemis------------------
            for i in   self.tabennemi:
                
                # l'obstacle arrive en bas de l'ecran (collision avec le sol) 
                if self.sol.rect.colliderect(i.rect): 
                    i.rect.y = 0
                    # changement au hasard de la couleur du prochaine obstacle
                    i.color.couleur()
                    i.rect.x = randint(80,410)

                # collision entre l'ennemi et le joueur 
                if self.player.rect.colliderect(i.rect) :
                    # le joueur de meme couleur que l'ostacle/ennemi 
                    if i.color.color == self.player.color:
                        # incrementation du score---------
                        if res_score==True:
                            self.score.point +=1
                            res_score=False       
                    else:
                        res_score=True
                
                    # le joueur n'a pas le meme couleur que l'ostacle/ennemi 
                    if not i.color.color == self.player.color :
                        if self.score.isBestScore():
                            self.score.ajouterBestScore()
                        gameover = Gameover(self.ecran,self.menu,self.score)
                        gameover.run()
                        
                # superposition de sprite--------------------------------------
                if self.malus.rect.colliderect(i.rect) :
                    if rep==1:
                        #mettre hors du champs le malus----------------------- 
                        self.malus.x=600

                        
            #collision entre les 2 ennemis--------------------------------------
            if self.ennemi1.rect.colliderect(self.ennemi.rect):
               # pour evité cette collision on change l'emplacement d'un ennemis 
               self.ennemi1.rect.x=self.ennemi1.rect.x-self.taille1

                
            #collision des pieces (bonus)---------------------------------
            
                #si le bonus arrive en bas (sol)------------------------      
            if self.sol.rect.colliderect(self.bonus.rect):
                #changement du bonus (étoile ou piece)------------------
                self.bonus.bonusChange() 
                self.bonus.y=0
                self.bonus.x=randint(80,410)


            #collision entre un bonus et le joueur---------------------
            if self.player.rect.colliderect(self.bonus.rect):
                if self.bonus.effet(self.ecran)=="piece":
                    #incrementation du score ------------------------
                    if res_score1==True:
                        self.score.point +=1
                        res_score1=False
                        #hors de champs
                        self.bonus.x=600
                    else:
                        res_score1=True
                elif self.bonus.effet(self.ecran)=="etoile":
                    #changement du joueur -----------------------
                    self.player.playerChange()

                    

    
            #collisions des malus------------------------------
                #collision entre un malus et le joueur---------
            if self.player.rect.colliderect(self.malus.rect):
                # si le malus est une bomb -------------------
                if  self.malus.effet(self.ecran)=="bomb":
                    
                    toucher_bomb=True
                    bomb_temps=0
                    #hors du champs
                    self.malus.x=600
                    # diminuer la vitesse du joueur (car toucher par le malus la bomb 
                    self.player.malusChange(3)
                    
                    
                else:
                    #sinon (touche le fantome) faire l'effet avec les cercles ----------
                    self.malus.effet(self.ecran)
                    
            # cette partie permet de gerer le temps durant lequel le joueur est ralenti par la bomb qui aurai touchée       
            if toucher_bomb==True and bomb_temps==500 :
                self.player.malusChange(5)
                toucher_bomb=False 
                
                # superposition de sprite---------------------------------
            if self.malus.rect.colliderect(self.bonus.rect):
                
                if rep==1:
                        #mettre hors du champs le bonus depend du hasard de la varaible rep
                        self.bonus.x=600
                else:
                        #mettre hors du champs le malus depend du hasard de la varaible rep
                        self.malus.x=600
                
                
                #si le malus arrive en bas (en contact avec la sol : --------------

            if self.sol.rect.colliderect(self.malus.rect):
                self.malus.malusChange() 
                self.malus.y=0
                self.malus.x=randint(80,410)
          
                                 
            # augmentation de la vitesse du jeu en fonction du score 
            if self.score.point == score4 :
                # augementation de la vitesse des ennemis--------------- 
                self.valeurG=self.valeurG+1.5
                self.gravite=(0,self.valeurG)
                # augmentation de la vitesse du joueur ----------------
                self.player.vitesseX=self.player.vitesseX+1
                score4=self.score.point+4
            
            #-----------------------MOUVEMENT ---------------------
            #mouvement ennemis -----------------------------------
            for i in   self.tabennemi:
               i.mouvement(self.ennemi_vitesse_y)
           
            #mouvement malus--------------------------------------
            self.malus.mouvement(self.malus_vitesse_y)

            #mouvement bonus----------------------------------------
            self.bonus.mouvement(self.bonus_vitesse_y)

            #mouvement joueur---------------------------------------
            self.player.mouvement(self.player_vitesse_x)

            
            #-----------------------AFFICHANGE ---------------------
            #affichage de l'ecran------------------------------------
            self.ecran.blit(self.image_fond,(0,0))
            

            #affichage du score------------------------------------
            self.score.afficherBestScore()
            self.score.afficher()

            #affichage du score------------------------------------
            self.sol.afficher(self.ecran)
            self.gravite_jeu()
            self.player.affiche()

            #affichage des ennemis-------------------------------
            for i in   self.tabennemi:
                i.afficher(self.ecran)

            #affichage malus---------------------------------------
            self.malus.afficher()

            #affichage bonus--------------------------------------
            self.bonus.afficher()
            

                    
            #incrementation de la variable ------------------------
            bomb_temps+=1 
            # rafrechissement de l'ecran ------------------------
            pygame.display.update()

    def gravite_jeu(self):
        for i in self.tabennemi:
            i.rect.y += self.gravite[1] + self.resistance[1]
        self.malus.y += self.gravite[1] + self.resistance[1]
        self.bonus.y += self.gravite[1] + self.resistance[1]


