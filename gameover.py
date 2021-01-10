import pygame
from bouton import*
from menu import*
from score import*

class Gameover():
    def __init__(self,ecran,menu,score):
        self.ecran = ecran
        self.menu = menu
        self.score = score
        self.xGameOver = 0
        self.yGameOver = 0
        self.xBestScore = 15
        self.yBestScore = 160
        self.xYourScore = 65
        self.yYourScore = 190

    def afficherGameOver(self):
        font=pygame.font.Font(None, 75)
        self.ecran.blit(pygame.image.load("images/gameover.jpg"),(self.xGameOver,self.yGameOver))

    def run(self):
        RUNNING = True
        while RUNNING:
            self.ecran.fill( (250,250,250) ) # couleur du fond 
            bouton_menu = Bouton(40,400,100,50,self.ecran,"MENU",(255,255,255))
            
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
