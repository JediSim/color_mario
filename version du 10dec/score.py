import pygame

class Score:
    def __init__(self,ecran):
        self.ecran = ecran
        self.point = 0
        self.couleurTexte = (0,0,0)
        self.x = 450
        self.y = 5
        self.xBestScore = 5
        self.yBestScore = 5
        self.nomFichier = "best_score.txt"

    def afficher(self):
        font=pygame.font.Font(None, 24)
        champs = font.render(str(self.point),1,self.couleurTexte)
        self.ecran.blit(champs,(self.x,self.y))

    def isBestScore(self):
        fichier = open(self.nomFichier,'r')
        if int(fichier.read())<self.point:
            res = True
        else:
            res = False
        return res

    def ajouterBestScore(self):
        fichier = open(self.nomFichier,'w')
        fichier.write(str(self.point))
        fichier.close()

    def afficherBestScore(self):
        fichier = open(self.nomFichier,'r')
        font=pygame.font.Font(None, 24)
        champs = font.render("Best : "+fichier.read(),1,self.couleurTexte)
        self.ecran.blit(champs,(self.xBestScore,self.yBestScore))
        fichier.close()

    def afficherBestScoreGameOver(self,abs,ord):
        fichier = open(self.nomFichier,'r')
        font=pygame.font.Font(None, 50)
        champs = font.render("Best Score : "+fichier.read(),1,self.couleurTexte)
        self.ecran.blit(champs,(abs,ord))
        fichier.close()
