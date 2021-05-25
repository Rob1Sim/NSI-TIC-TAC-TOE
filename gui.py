
import pygame
import GameState as gm
from pygame import display
from pygame import color
from pygame.sprite import groupcollide
import random

#Instantiation
pygame.init()
gameState = gm.GameState()

gameState.set_gameState("playerTurn")




#Function

    #Function => draw the grid an the screen
def renderGrid(gridImage,gridImageX,gridImageY):
    screen.blit(gridImage,(gridImageX,gridImageY))

    #Function => Draw the cercle or the cross on the screen
def drawCrossOrCerlce(image,posX,posY):
    screen.blit(image,(posX,posY))


    #Function => Draw rectangle for each clicklable component => USE FOR DEBUG
def debug_Clicker(gridPos,RED,shape):
    
    for i in range (0,len(gridPos)):
        posRec = pygame.Rect(gridPos[i][0][0],gridPos[i][0][1],shape[0],shape[1])
        pygame.draw.rect(screen,RED,posRec)
    
    #Function => Draw a Rectangle => USE FOR DEBUG
def debug_Clicker_box(posX,posY,COLOR,shape):
    
    posRec = pygame.Rect(posX,posY,shape[0],shape[1])
    pygame.draw.rect(screen,COLOR,posRec)
    

    #Function => Verified if the click of the player is good
def isClicklable(grid,cliclPos,shape,gCheck,gridImage,pion):
    isGood= 0
    
    
    
        #If the player click in a checkbox, and if the checkbox is not already checked and if its the player turn
    for i in range (0,len(grid)):
        if (cliclPos[0]>= grid[i][0][0] and cliclPos[1]>= grid[i][0][1]) and (cliclPos[0]<= grid[i][0][0]+shape[0] and cliclPos[1]<= grid[i][0][1]+shape[1]) and gCheck[i] == 0 and gameState.get_Current_State() == "playerTurn":
            gCheck[i] =1
            drawCrossOrCerlce(pion,gridImage[i][0][0],gridImage[i][0][1])
            gameState.set_gameState("botTurn")
        
            
        
    

#def botTurn():
    #TODO Algo of the bot


#Screen parameter
backColor = (31, 29, 26)
screen_shape =  [800,600]


# Set up the drawing window
screen = pygame.display.set_mode(screen_shape)
screen.fill(backColor)


#Title and logo
#Logo by : https://www.freepik.com
pygame.display.set_caption("Tic-Tac-Toe")
icon = pygame.image.load('Images/TTT.png')  
pygame.display.set_icon(icon)



#Grid image
    #grid image Load
gridImage = pygame.image.load('Images/grid.png')  
    #Grid position 
gridImageX = 125
gridImageY =23

#Cercle and Cross
CC_shape = (100,100)

gridPosCC= [[(156,78),CC_shape],[(350,78),CC_shape],[(557,78),CC_shape],
          [(156,250),CC_shape],[(350,250),CC_shape],[(557,250),CC_shape],
          [(156,448),CC_shape],[(350,418),CC_shape],[(557,448),CC_shape]]



#Tic-Tac-Toe logic
    #Choose wich (cross or cercle) the player had
whoStart = random.randrange(1,3)
if whoStart == 1:
    pion = pygame.image.load('Images/Cross.png')
else:
    pion = pygame.image.load('Images/Round.png')


    #Cube scale in pixels
shapeClick = (170,148) 
    #Debug color
COLOR = pygame.Color(255, 0, 0) 

    #Every coodinates & scale of clickable boxes 
gridPosClick= [[(104,50),shapeClick],[(315,50),shapeClick],[(526,50),shapeClick],
          [(104,234),shapeClick],[(315,234),shapeClick],[(526,234),shapeClick],
          [(104,418),shapeClick],[(315,418),shapeClick],[(526,418),shapeClick]]

    #each states for the boxes : PlayerHasPlayed = 1, nonPlayedYet = 0, BotHasPlayed = -1
gridCheck = [ 0,0,0
             ,0,0,0
             ,0,0,0
             ]


#debug_Clicker(gridPosClick,COLOR,shapeClick)


running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            c_pos = pygame.mouse.get_pos()
            isClicklable(gridPosClick,c_pos,shapeClick,gridCheck,gridPosCC,pion)
            
            #TODO: Fonction qui récupère la pos du click vérifie les coordonée, si il sont bon alors il ajoute un cercle/croix
    renderGrid(gridImage,gridImageX,gridImageY)
    
    #Update the screen every
    pygame.display.update()



print(gridCheck)

pygame.quit()