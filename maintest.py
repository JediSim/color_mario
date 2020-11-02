import pygame
 
pygame.init()
pygame.font.init()
 
RUNNING = True
 
fenetre = pygame.display.set_mode((500,500)) # fenetre de dimenssion 500,500
 
myfont = pygame.font.SysFont('Helvetic', 20)




def gerer_events_principale():
    global RUNNING
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # pouvoir quitter la fenetre 
            RUNNING = False

            
 
def menu():
    
    
    fond=pygame.Surface(fenetre.get_size())
    fond=fond.convert()
    fond.fill((250,250,250))
    fenetre.blit(fond,(0,0))

    rect = pygame.draw.rect(fenetre,(0,0,0),pygame.Rect(200, 200, 100, 50)) # afficher un rectangle dans la fenetre 
    text = myfont.render(' Jouer ', False, (255,250,250)) # text afficher en blanc
    
    fenetre.blit(text, (225,215)) # modifier les pixels de la fenetre, place du texte
    
    gerer_mouse_menu(rect) # appeller la fonction gerer_mouse_menu avec comme paramêtre rect

    
     
def jeu():

    image_fond=pygame.image.load("fondmario.jpg")
    fenetre.blit(image_fond,(0,0))
    
    rect = pygame.draw.rect(fenetre,(255,0,0),pygame.Rect(10, 450, 75, 30)) # afficher un rectangle dans la fenetre 
 
    text = myfont.render('Quitter ', False, (255,255,255)) # text afficher en blanc  
    fenetre.blit(text, (20,460)) # modifier les pixels de la fenetre, place du texte  
 
    gerer_mouse_jeu(rect) # appeller la fonction gerer_mouse_jeu avec comme paramêtre rect

    
     
def gerer_mouse_jeu(rectangle):
    global afficher
     
    mouse = pygame.mouse.get_pressed()
    if mouse[0]: 
        mouse_pos = pygame.mouse.get_pos()# recuperer la position de la souris cliqué.
         
        if rectangle.collidepoint(mouse_pos): # si il y a collision avec la souris et le rectangle mis en paramêtre 
            afficher = menu # afficher la menu avec le bouton jouer

            
 
def gerer_mouse_menu(rectangle):
    global afficher
     
    mouse = pygame.mouse.get_pressed() 
    if mouse[0]: 
        mouse_pos = pygame.mouse.get_pos() # recuperer la position de la souris cliqué.
         
        if rectangle.collidepoint(mouse_pos):
            afficher = jeu # afficher la menu avec le bouton quitter

            


# Affecte la fonction menu
afficher = menu
 
def boucle_principale():
    while RUNNING:

        fenetre.fill( (0,0,0) ) # couleur du fond 
         
        gerer_events_principale()
         
        ## Exécute la fonction affecté à afficher (menu/jeu)
        afficher()
         
         
        pygame.display.update()
         
    pygame.quit()
 
 
 
boucle_principale()

    
"menu.add_button('Play', start_the_game)"
"menu.add_button('Quit', pygame_menu.events.EXIT)"
"colision"
