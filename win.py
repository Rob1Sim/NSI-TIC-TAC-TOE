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
        self.__winBot = "null"
        self.__scoreB = 0
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
    
    def get_winBot(self):
        return self.__winBot
    
    def set_winBot(self,winner):
        self.__winBot = winner
    
    def get_scoreB(self):
        return self.__scoreB

    def set_scoreB(self, score):
        self.__scoreB = score
    
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
            
        
    def win_string(self, grilleC):
            
        if (grilleC[0] == "X" and grilleC[1] == "X" and grilleC[2] == "X") or (grilleC[3] == "X" and grilleC[4] == "X" and grilleC[5] == "X") or (grilleC[6] == "X" and grilleC[7] == "X" and grilleC[8] == "X") or (grilleC[0] == "X" and grilleC[4] == "X" and grilleC[8] == "X") or (grilleC[2] == "X" and grilleC[4] == "X" and grilleC[6] == "X") or (grilleC[0] == "X" and grilleC[3] == "X" and grilleC[6] == "X") or (grilleC[1] == "X" and grilleC[4] == "X" and grilleC[7] == "X") or (grilleC[2] == "X" and grilleC[5] == "X" and grilleC[8] == "X"):
                self.__isWin = True
                self.set_winBot("player")
                self.set_scoreB(1)
                return "end"
        if (grilleC[0] == "O" and grilleC[1] == "O" and grilleC[2] == "O") or (grilleC[3] == "O" and grilleC[4] == "O" and grilleC[5] == "O") or (grilleC[6] == "O" and grilleC[7] == "O" and grilleC[8] == "O") or (grilleC[0] == "O" and grilleC[4] == "O" and grilleC[8] == "O") or (grilleC[2] == "O" and grilleC[4] == "O" and grilleC[6] == "O") or (grilleC[0] == "O" and grilleC[3] == "O" and grilleC[6] == "O") or (grilleC[1] == "O" and grilleC[4] == "O" and grilleC[7] == "O") or (grilleC[2] == "O" and grilleC[5] == "O" and grilleC[8] == "O"):
                self.__isWin = True
                self.set_winBot("bot")
                self.set_scoreB(-1)
                return "end"
                #We are checking if its a draw or not
        if self.__isWin == False:
                compt = 0
                for i in range(0, len(grilleC)):
                    if grilleC[i] != "":
                        compt += 1
                if compt == len(grilleC):
                    self.set_winBot("draw")
                    return "end"
                else:
                    
                    return "nobody"
