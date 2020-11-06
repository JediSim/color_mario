import pygame
from pygame.locals import*
import time

pygame.init()

#-----------------------------mettre image en fond-------------------------------

#def image():
    #image = pygame.image.load("fond.png").convert()
    #ecran.blit(image, (50,0))

#fonction à appeler dans la partie jeu 
#-----------------------------FENETRE-------------------------------

lgfenetre = 500
largfenetre = 500
fenetre = pygame.display.set_mode((lgfenetre,largfenetre))
fenetre.fill(0x99EE90) #couleur de fond uniforme


pygame.display.set_caption("Color Mario") # titre de la page

#-----------------------------VARIABLE COULEUR-------------------------------
BLANC = (255, 255, 255)

#-----------------------------ENNEMI-------------------------------

    
ennemiImg = pygame.image.load("ennemi.jpg")
ennemiImg.set_colorkey(BLANC) #pour enlever le fond blanc de l'image
tailleennemi = 50
ennemiImSmall = pygame.transform.scale(ennemiImg,(tailleennemi,tailleennemi))
ennemiX = 240   #si jamais on veut bouger horizontalement
ennemiY = 0     # pour faire descendre l'ennemi

def ennemi(x,y):
    fenetre.blit(ennemiImSmall, (x,y))

# -------------------------------LE JEU ------------------------------------


continuer = True

while continuer:
    
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            continuer = False

        for i in range(0 , lgfenetre-tailleennemi):
            print(i)
            time.sleep(0.2)
            ennemiY += i
            if ennemiY<=0:
                ennemiY=0            #on verifie que l'ennemi soit bien dans la fenetre
            elif ennemiY>=470:
                ennemiY=0           #permet de revenir en haut

            ennemi(ennemiX,ennemiY)
            pygame.display.update()

    pygame.display.flip()



pygame.quit()


