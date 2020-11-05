import pygame
 
pygame.init()

pygame.display.set_caption("Color mario")


 
fenetre = pygame.display.set_mode((500,500)) # fenetre de dimenssion 500,500

playerImg = pygame.image.load('player.png')
playerImSmall = pygame.transform.scale(playerImg,(30,30))
playerX = 240
playerY = 400
playerX_bouge= 0


def player(x,y):
    fenetre.blit(playerImSmall,(x,y))

    
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
                print("la touche gauche a été pressée")
                playerX_bouge= -0.1 #deplacement 
            if event.key == pygame.K_RIGHT:
                 print("la touche droite a été pressée")
                 playerX_bouge= 0.1 #deplacement
                 
        #if event.type== pygame.KEYUP:
             #if event.key== pygame.K_LEFT or pygame.K_RIGHT:
                 #print ('une touche est pressée en bas ou en haut ')
                 
    playerX += playerX_bouge   # incrémentation        
    # SORTI DE LA FENETRE
    if playerX<=0:
        playerX=0
    elif playerX>= 470:
        playerX=470
        

    player(playerX,playerY)
    pygame.display.update()

    
pygame.quit()
