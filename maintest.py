import pygame
 
pygame.init()
pygame.font.init()
 
run = True
 
fenetre = pygame.display.set_mode((500,500))

myfont = pygame.font.SysFont('Helvetic', 20) # Police et taille du texte 
 
 
def gerer_events_principale():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
def menu():
    rect = pygame.draw.rect(fenetre,(255,0,0),pygame.Rect(200, 200, 100, 100)) #position et taille du rectangle 
 
    text = myfont.render('Jouer ', False, (255,255,255)) #couleur du bouton 
    fenetre.blit(text, (200,200)) # position du texte 
 
    gerer_mouse_menu(rect)
    
def jeu():
    rect = pygame.draw.rect(fenetre,(0,255,0),pygame.Rect(200, 200, 100, 100))
 
    text = myfont.render('GOOOO', False, (255,255,255))
    fenetre.blit(text, (200,200))# position du texte 
 
    gerer_mouse_jeu(rect)
     
def gerer_mouse_jeu(rectangle):
    global afficher
     
    mouse = pygame.mouse.get_pressed()
    if mouse[0]: 
        mouse_pos = pygame.mouse.get_pos()
         
        if rectangle.collidepoint(mouse_pos):
            afficher = menu
 
def gerer_mouse_menu(rectangle):
    global afficher
     
    mouse = pygame.mouse.get_pressed()
    if mouse[0]: 
        mouse_pos = pygame.mouse.get_pos()
         
        if rectangle.collidepoint(mouse_pos):
            afficher = jeu
 
## Affecte la fonction menu
afficher = menu
 
def boucle_principale():
    while run:
        fenetre.fill( (0,0,0) )
         
        gerer_events_principale()
         
        ## Exécute la fonction affecté à afficher (menu/jeu)
        afficher()
         
         
        pygame.display.update()
         
    pygame.quit()
 
 
 
boucle_principale()
    
"menu.add_button('Play', start_the_game)"
"menu.add_button('Quit', pygame_menu.events.EXIT)"
"colision"
