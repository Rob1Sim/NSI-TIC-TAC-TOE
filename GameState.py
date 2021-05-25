#Game state class 
#Define the game statement
class GameState:
    def __init__(self) :
        self.__sAllgameState = ["begin","playerTurn","botTurn","end"]
        self.__currentState = "begin"

    def get_Current_State(self):
        return self.__currentState
    
    def set_gameState(self,state):
        if state == "begin" or state =="playerTurn"  or state == "botTurn" or state =="end":
            self.__currentState = state
        else :
            print("This is not a valid GameState")