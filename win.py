import pygame
import GameState as gm

gameState = gm.GameState()

#Win or Loose screen
    #Load the images of win/loose/draw screen
winScreen = pygame.image.load('Images/EndWin.png')
looseScreen = pygame.image.load('Images/EndLoose.png')
drawScreen =pygame.image.load('Images/EndDraw.png')

#Class for the win/loose screen
class win:
    
    def playerWin(self,screen):
        #TODO: Button to retry
        #TODO: Button to quit
        screen.blit(winScreen,(0,0))
        #Display the image of the win screen
    def botWin(self,screen):
        #TODO: Button to retry
        #TODO: Button to quit
        screen.blit(looseScreen,(0,0))
        
    def draw(self,screen):
        #TODO: Button to retry
        #TODO: Button to quit
        screen.blit(drawScreen,(0,0))
    
        #Function => verified if someone win
    def winCond(self,grilleC,pScore,winner,isWin = False):
        if (grilleC[0] == 1 and grilleC[1] == 1 and grilleC[2] == 1) or (grilleC[3] == 1 and grilleC[4] == 1 and grilleC[5] == 1) or (grilleC[6] == 1 and grilleC[7] == 1 and grilleC[8] == 1) or (grilleC[0] == 1 and grilleC[4] == 1 and grilleC[8] == 1) or (grilleC[2] == 1 and grilleC[4] == 1 and grilleC[6] == 1) or (grilleC[0] == 1 and grilleC[3] == 1 and grilleC[6] == 1)or (grilleC[1] == 1 and grilleC[4] == 1 and grilleC[7] == 1) or (grilleC[2] == 1 and grilleC[5] == 1 and grilleC[8] == 1):        
            pScore +=1
            isWin = True
            winner = "player"
            
            return  winner,"end"
        if (grilleC[0] == -1 and grilleC[1] == -1 and grilleC[2] == -1) or (grilleC[3] == -1 and grilleC[4] == -1 and grilleC[5] == -1) or (grilleC[6] == -1 and grilleC[7] == -1 and grilleC[8] == -1) or (grilleC[0] == -1 and grilleC[4] == -1 and grilleC[8] == -1) or (grilleC[2] == -1 and grilleC[4] == -1 and grilleC[6] == -1) or (grilleC[0] == -1 and grilleC[3] == -1 and grilleC[6] == -1)or (grilleC[1] == -1 and grilleC[4] == -1 and grilleC[7] == -1) or (grilleC[2] == -1 and grilleC[5] == -1 and grilleC[8] == -1):
            winner = "bot"
            isWin = True
            return winner,"end"
            #We are checking if its a draw or not
        if isWin == False:
            compt = 0
            for i in range (0,len(grilleC)):
                if grilleC[i] !=0:
                    compt +=1
            if compt == len(grilleC):
                winner = "draw"
                return winner,"end"
            else:
                winner = "nobody"
                return winner,""
            
        