import pygame
from bouton import*
from menu import*
from score import*

class Gameover():
    def __init__(self,ecran,menu,score):
        self.ecran = ecran
        self.menu = menu
        self.score = score
        self.xGameOver = 100
        self.yGameOver = 90
        self.xBestScore = 150
        self.yBestScore = 145
        self.xYourScore = 200
        self.yYourScore = 175
        self.couleurTexte = (255,0,0)

    def afficherGameOver(self):
        font=pygame.font.Font(None, 75)
        champs = font.render("GAME OVER",1,self.couleurTexte)
        self.ecran.blit(champs,(self.xGameOver,self.yGameOver))

    def run(self):
        RUNNING = True
        while RUNNING:
            self.ecran.fill( (250,250,250) ) # couleur du fond 
            bouton_menu = Bouton(200,255,100,50,self.ecran,"menu",(255,255,255))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pouvoir quitter la ecran 
                    RUNNING = False
                elif event.type == pygame.MOUSEBUTTONDOWN and bouton_menu.isClique:
                    self.menu.run()
            
            self.afficherGameOver()
            self.score.afficherBestScoreGameOver(self.xBestScore,self.yBestScore)
            self.score.afficherScoreGameOver(self.xYourScore,self.yYourScore)
            pygame.display.update()
         
        pygame.quit()