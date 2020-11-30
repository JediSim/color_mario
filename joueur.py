import pygame

class Joueur (pygame.sprite.Sprite):
    def __init__ (self,x,y,image):

        super().__init__()
        self.x=x
        self.y=y
        self.image=image

    def afficher(self,surface):

        surface.blit(self.image,(self.x,self.y))
        
    def mouvement ( self, vitesse):
        self.x+=vitesse  
        
