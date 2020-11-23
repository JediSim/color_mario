import pygame
import math
pygame.init()



#disque teste inf rayon , barre


pygame.display.set_caption("Color mario")


 
fenetre = pygame.display.set_mode((500,500)) # fenetre de dimenssion 500,500

playerImg = pygame.image.load('player.png')
playerImSmall = pygame.transform.scale(playerImg,(30,30))





playerX = 240
playerY = 400
playerX_bouge=0
couleurperso=(250,0,0)

obstacleX=150
obstacleY=400
couleur=(250,250,0)

def isCollision(obstacleX,obstacleY,playerX,playerY):
    distance=math.sqrt((math.pow(obstacleX-playerX,2))+(math.pow(obstacleY-playerY,2)))
    if distance<1:
        return True
    else:
        return False
    
def obstacle(x,y):
    pygame.draw.rect(fenetre,couleur,(x,y,50,50)) 
    

def player(x,y):
    fenetre.blit(playerImSmall,(x,y))

vitesse=0.1 
RUNNING = True
while RUNNING:

    fenetre.fill( (0,0,0) )
            
    #playerX += 0.09
    # a gauche -=
    # pour monter ou descendre payerY-= ou += 
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            RUNNING = False
            
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                    playerX_bouge= -vitesse       #deplacement 
            if event.key == pygame.K_RIGHT:
                    playerX_bouge= vitesse       #deplacement
                    
        #if event.type== pygame.KEYUP:
            #if event.key== pygame.K_LEFT or pygame.K_RIGHT:
                #print ('une touche est pressée en bas ou en haut ')
               


    # COLLISION
    collision=isCollision(obstacleX,obstacleY,playerX,playerY)
    
    if collision and not couleur==couleurperso:
        fenetre.blit(fenetre,(playerX,playerY)) 
      
        
    elif collision and couleur==couleurperso:
        print(" bonne couleur bien jouer")
        playerX += playerX_bouge
    else:
         playerX += playerX_bouge     # incrémentation

    
    # SORTI DE LA FENETRE
    if playerX<=0:
        playerX=0
    elif playerX>= 470:
        playerX=470
      

    player(playerX,playerY)
    obstacle(obstacleX,obstacleY)


        
    pygame.display.update()

    
pygame.quit()



