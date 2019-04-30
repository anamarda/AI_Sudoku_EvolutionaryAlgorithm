import numpy as np
from Board import Board

class Chromozome(object):

    def __init__(self, noGenes, dim, brd):
        '''
        noGenes - number of 0s
        dim - dimension of the board
        brd - the board of Sudoku
        '''
        
        self.genes = np.random.random_integers(dim, size=noGenes)
        self.genes = [str(i) for i in self.genes]
        self.fitness = 0
        self.brd = brd

    def eval(self):
        '''
        evaluate the chromozome
        '''
        self.brd = self.brd.fillWithGenes(self.genes)
        self.fitness = self.brd.fit()

    def setGenes(self, genes):
        self.genes = genes