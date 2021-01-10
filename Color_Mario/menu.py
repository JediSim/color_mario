import pygame
from bouton import*
from jeu import*

class Menu:
    def __init__(self,ecran):
        self.ecran = ecran
        self.RUNNING = True
    
    def run(self):
        while self.RUNNING:
            self.ecran.blit(pygame.image.load("images/fondmenu.jpg"),(0,0)) # couleur du fond 
            start = Bouton(200,350,100,50,self.ecran,"     JOUER",(255, 255, 255))
            quit_bouton = Bouton(200,410,100,50,self.ecran,"   QUITTER",(255, 255, 255))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # pouvoir quitter la ecran 
                    self.RUNNING = False
                elif event.type == pygame.MOUSEBUTTONDOWN and start.isClique:
                    jeu = Jeu(self.ecran,self)
                    jeu.run()
                elif event.type == pygame.MOUSEBUTTONDOWN and quit_bouton.isClique:
                    self.RUNNING = False
            
            pygame.display.update()
         
        pygame.quit()

