import win
import math
win_class = win.win()

class Minimax:
    def __init__(self,board):
        self.__board = board
        self.__boardString = []
    
    
    
    
    def __pre_minimax(self):
        for i in range (0,len(self.__board)):
            if self.__board[i] == 1:
                self.__boardString.append("X")
            if  self.__board[i] == 0:
                self.__boardString.append("")
            if self.__board[i] == -1:
                self.__boardString.append("O")
                
    def __after_minimax(self):
        for i in range(len(self.__boardString)):
            if self.__boardString[i] == "X":
                self.__board[i] = 1
            if self.__boardString[i] == "":
                self.__board[i] = 0
            if self.__boardString[i] == "O":
                self.__board[i] = -1
        return self.__board


    def __make_move(self,index):
        self.__boardString[index] = "O"
    
    def __make_move_player(self, index,isPlayer):
        if isPlayer:
            self.__boardString[index] = "X"
        else:
            self.__boardString[index] = "O"
    
    
    def  __undo_move(self,index):
        self.__boardString[index] = ""
    
    def __get_possible_move(self):
       final = self.__boardString
       return final
    def  __isFull(self):
        cmpt =0
        for i in range(len(self.__get_possible_move())):
            if self.__get_possible_move()[i] == "":
                cmpt += 1
                
        if cmpt == 0:
            return False
        else:
            return True         
    def __minimax_recursion(self,isMax):
        who_win = win_class.win_string(self.__boardString)
        if who_win =="end":
            if  win_class.get_winBot() == "draw":
                return 0
            if win_class.get_winBot() == "bot":
                return 1
            if win_class.get_winBot() == "player":
                return -1
        scores = []
        for move in range(len(self.__get_possible_move())):
            if self.__get_possible_move()[move] == "":
                if isMax:
                    self.__make_move_player(move,isMax)
                else:
                    self.__make_move_player(move, not isMax)
                scores.append(self.__minimax_recursion(not isMax))
                self.__undo_move(move)
                print(scores)
                return max(scores) if isMax else min(scores)
            
        
            

    def __best_move(self):
        
        bestScore = -math.inf
        bestMove = None
        if  self.__isFull():
            for move in range(len(self.__get_possible_move())):
                if self.__get_possible_move()[move] == "":
                    self.__make_move(move)
                    score = self.__minimax_recursion(False)
                    self.__undo_move(move)
                    if score > bestScore:
                        bestScore = score
                        bestMove = move
            
            self.__make_move(bestMove)
            

    def all_in(self):
        self.__pre_minimax()
        self.__best_move()
        
        return self.__after_minimax()
