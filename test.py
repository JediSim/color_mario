import pygame
import math
import time
pygame.init()


#playerX += 0.09
# a gauche -=
# pour monter ou descendre payerY-= ou +=
#disque teste inf rayon , barre

#if event.type== pygame.KEYUP:
#if event.key== pygame.K_LEFT or pygame.K_RIGHT:
#print ('une touche est pressée en bas ou en haut ')
               



pygame.display.set_caption("Color mario")


lgfenetre = 500
largfenetre = 500
fenetre = pygame.display.set_mode((lgfenetre,largfenetre)) # fenetre de dimenssion 500,500

#-----------------------------JOUEUR-------------------------------

playerImg = pygame.image.load('player.png')
playerImSmall = pygame.transform.scale(playerImg,(30,30))
playerX = 240
playerY = 400
playerX_bouge=0
couleurperso=(250,0,0)


def player(x,y):
    fenetre.blit(playerImSmall,(x,y))


#-----------------------------VARIABLE COULEUR-------------------------------

BLANC = (255, 255, 255)

#-----------------------------ENNEMI-------------------------------

    
ennemiImg = pygame.image.load("ennemi.jpg")
ennemiImg.set_colorkey(BLANC) #pour enlever le fond blanc de l'image
tailleennemi = 50
ennemiImSmall = pygame.transform.scale(ennemiImg,(tailleennemi,tailleennemi))
ennemiX = 250   #si jamais on veut bouger horizontalement
ennemiY = 0     # pour faire descendre l'ennemi
couleur=(250,0,0)

def ennemi(x,y):
    fenetre.blit(ennemiImSmall, (x,y))



def isCollision(x,y,playerX,playerY):
    distance=math.sqrt((math.pow(x-playerX,2))+(math.pow(y-playerY,2)))
    if distance<1:
        return True
    else:
        return False
    

# -------------------------------LE JEU ------------------------------------

vitesse=0.1
RUNNING = True
collision=False
while RUNNING:

    fenetre.fill( (0,0,0) )
            
    
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            RUNNING = False



                
        if event.type== pygame.KEYDOWN:
            print("une touche est presse")
            if event.key == pygame.K_LEFT:
                playerX_bouge= -vitesse       #deplacement 
            if event.key == pygame.K_RIGHT:
                playerX_bouge= vitesse       #deplacement
        # SORTI DE LA FENETRE JOUEUR 
        if playerX<=0:
            playerX=0
        elif playerX>= 470:
            playerX=470
              

        # COLLISION
        collision=isCollision(ennemiX,ennemiY,playerX,playerY)
            
        if collision and not couleur==couleurperso:
            print("une collision")
            fenetre.blit(fenetre,(playerX,playerY)) 
              
                
        elif collision and couleur==couleurperso:
            print(" bonne couleur bien jouer")
            playerX += playerX_bouge
        else:
            playerX += playerX_bouge     # incrémentation

        player(playerX,playerY)
        pygame.display.update()

        
        print("ennemi")
        time.sleep(0.2)
        fenetre.blit(fenetre, (ennemiX,ennemiY))
        ennemiY += 10
        ennemi(ennemiX,ennemiY)    
        pygame.display.update()


         
        # SORTI DE LA FENETRE ENNEMI
        if ennemiY<=0:
            ennemiY=0
        elif ennemiY>= 470:
            ennemiY=0


    
pygame.quit()
