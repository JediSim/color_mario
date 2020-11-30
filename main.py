import pygame
from menu import*
 
pygame.init()
pygame.font.init()
 
RUNNING = True
 
ecran = pygame.display.set_mode((500,500)) # ecran de dimenssion 500,500
 
myfont = pygame.font.SysFont('Helvetic', 20)

if __name__ == "__main__":
    
    menu = Menu(ecran)
    menu.run()

 
