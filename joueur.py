import pygame

class Joueur (pygame.sprite.Sprite):
    def __init__ (self,x,y,image):

        super().__init__()
        self.x=x
        self.y=y
        self.image=image
        self.rect=self.image.get_rect()
        #self.rect=pygame.Rect(self.x,self.y,self.taille[0],self.taille[1])

    def afficher(self,surface):
        #pygame.draw.rect(surface,(255,0,0),self.rect)
        surface.blit(self.image,self.rect)
        
    def mouvement ( self, vitesse):
        self.rect.x+=vitesse
        
