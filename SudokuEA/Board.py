import numpy as np
import math

class Board(object):
    
    def __init__(self, matrix, dim):
        self.matrix = matrix
        self.dim = dim

        coords = np.where(self.matrix == '0')
        self.coord_X = coords[0]
        self.coord_Y = coords[1]

    
    def fit(self):
        '''
        Sums the number of wrong number in the place of '0's
        '''
        no_zeros = len(self.coord_X)
        sum = 0
        for i in range(0, no_zeros):
            sum += self.checkXY(self.coord_X[i], self.coord_Y[i])
        return sum


    def fillWithGenes(self, list):
        '''
        Fill the '0's with the values in the list
        '''
        no_values = len(list)
        for i in range(0, no_values):
            x = self.coord_X[i]
            y = self.coord_Y[i]
            info = list[i]
            self.setXY(x, y, info)
        return self


    def setXY(self, x, y, info):
        self.matrix[x][y] = info
    

    def checkXY(self, x, y):
        '''
        returns:
            0, if the element in the matrix[x][y] is correct (does not repeat)
            1, otherwise
        '''
        value = self.matrix[x][y]

        # se va genera cate o matrice [True/False] - True daca numarul exista pe linie/coloana, False altfel 
        #row
        rowCounter = np.count_nonzero(self.matrix[x, :] == value)
        if(rowCounter > 1):
            return 1
        
        #column
        colCounter = np.count_nonzero(self.matrix[:, y] == value)
        if(colCounter > 1):
            return 1
        
        #square
        x_square = int(getSquare(x, self.dim))
        y_square = int(getSquare(y, self.dim))
        sqrtDim = int(math.sqrt(self.dim))
        countValue = 0 

        for i in range (x_square, x_square + sqrtDim):
            for j in range (y_square, y_square + sqrtDim):
                if(self.matrix[i][j] == value):
                    countValue += 1
        if(countValue > 1):
            return 1

        return 0


def getSquare(x, dim):
    '''
    get the biggest sqrtDim multiple <= x
    '''
    sqrtDim = math.sqrt(dim)
    x_square = 0
    while x_square + sqrtDim <= x:
        x_square += sqrtDim
    return x_square