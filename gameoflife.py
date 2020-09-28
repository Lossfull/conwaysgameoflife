import numpy as np
class gameoflife():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.gameboard = np.zeros([height,width], dtype="int8")

    def nearbySum(self,i,j):
        return self.gameboard[(i-1)%self.height][(j-1)%self.width]+self.gameboard[(i-1)%self.height][(j)%self.width]+self.gameboard[(i-1)%self.height][(j+1)%self.width]+self.gameboard[(i)%self.height][(j-1)%self.width]+self.gameboard[(i)%self.height][(j+1)%self.width]+self.gameboard[(i+1)%self.height][(j-1)%self.width]+self.gameboard[(i+1)%self.height][(j)%self.width]+self.gameboard[(i+1)%self.height][(j+1)%self.width]

    def turn(self):
        newgameboard = self.gameboard.copy()
        for i in range(self.height):
            for j in range(self.width):
                if self.nearbySum(i, j) == 3:
                    newgameboard[i][j] = 1
                elif self.nearbySum(i, j) > 3 or self.nearbySum(i, j) < 2:
                    newgameboard[i][j] = 0
        self.gameboard = newgameboard


