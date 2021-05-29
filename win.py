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
    def __init__(self):
        self.__isWin = False
        self.__winner = "nobody"
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
    
    def get_is_win(self):
        return self.__isWin

    def get_is_win_winner(self):
        return self.__winner

    def get_is_win_winner_point(self):
        if self.__winner == "nobody" or self.__winner == "draw":
            return 0
        if self.__winner == "player":
            return 1
        if self.__winner == "bot":
            return -1
    
        #Function => verified if someone win
    def winCond(self,grilleC,winner):
        self.__winner = winner
        if (grilleC[0] == 1 and grilleC[1] == 1 and grilleC[2] == 1) or (grilleC[3] == 1 and grilleC[4] == 1 and grilleC[5] == 1) or (grilleC[6] == 1 and grilleC[7] == 1 and grilleC[8] == 1) or (grilleC[0] == 1 and grilleC[4] == 1 and grilleC[8] == 1) or (grilleC[2] == 1 and grilleC[4] == 1 and grilleC[6] == 1) or (grilleC[0] == 1 and grilleC[3] == 1 and grilleC[6] == 1)or (grilleC[1] == 1 and grilleC[4] == 1 and grilleC[7] == 1) or (grilleC[2] == 1 and grilleC[5] == 1 and grilleC[8] == 1):        
            
            self.__isWin = True
            self.__winner = "player"
            
            return self.__winner, "end"
        if (grilleC[0] == -1 and grilleC[1] == -1 and grilleC[2] == -1) or (grilleC[3] == -1 and grilleC[4] == -1 and grilleC[5] == -1) or (grilleC[6] == -1 and grilleC[7] == -1 and grilleC[8] == -1) or (grilleC[0] == -1 and grilleC[4] == -1 and grilleC[8] == -1) or (grilleC[2] == -1 and grilleC[4] == -1 and grilleC[6] == -1) or (grilleC[0] == -1 and grilleC[3] == -1 and grilleC[6] == -1)or (grilleC[1] == -1 and grilleC[4] == -1 and grilleC[7] == -1) or (grilleC[2] == -1 and grilleC[5] == -1 and grilleC[8] == -1):
            self.__winner = "bot"
            self.__isWin = True
            return self.__winner, "end"
            #We are checking if its a draw or not
        if self.__isWin == False:
            compt = 0
            for i in range (0,len(grilleC)):
                if grilleC[i] !=0:
                    compt +=1
            if compt == len(grilleC):
                self.__winner = "draw"
                return self.__winner, "end"
            else:
                self.__winner = "nobody"
                return self.__winner, ""
            
        
    def winCondBot(self, grilleC):
            
            if (grilleC[0] == 1 and grilleC[1] == 1 and grilleC[2] == 1) or (grilleC[3] == 1 and grilleC[4] == 1 and grilleC[5] == 1) or (grilleC[6] == 1 and grilleC[7] == 1 and grilleC[8] == 1) or (grilleC[0] == 1 and grilleC[4] == 1 and grilleC[8] == 1) or (grilleC[2] == 1 and grilleC[4] == 1 and grilleC[6] == 1) or (grilleC[0] == 1 and grilleC[3] == 1 and grilleC[6] == 1) or (grilleC[1] == 1 and grilleC[4] == 1 and grilleC[7] == 1) or (grilleC[2] == 1 and grilleC[5] == 1 and grilleC[8] == 1):

                return "end",1
            if (grilleC[0] == -1 and grilleC[1] == -1 and grilleC[2] == -1) or (grilleC[3] == -1 and grilleC[4] == -1 and grilleC[5] == -1) or (grilleC[6] == -1 and grilleC[7] == -1 and grilleC[8] == -1) or (grilleC[0] == -1 and grilleC[4] == -1 and grilleC[8] == -1) or (grilleC[2] == -1 and grilleC[4] == -1 and grilleC[6] == -1) or (grilleC[0] == -1 and grilleC[3] == -1 and grilleC[6] == -1) or (grilleC[1] == -1 and grilleC[4] == -1 and grilleC[7] == -1) or (grilleC[2] == -1 and grilleC[5] == -1 and grilleC[8] == -1):

                return "end",-1
                #We are checking if its a draw or not
            if self.__isWin == False:
                compt = 0
                for i in range(0, len(grilleC)):
                    if grilleC[i] != 0:
                        compt += 1
                if compt == len(grilleC):
                    
                    return "end",0
                else:
                    
                    return "nobody",0
