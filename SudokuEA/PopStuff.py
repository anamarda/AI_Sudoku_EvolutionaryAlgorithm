from Chromozome import Chromozome
from Board import Board
import numpy as np
import random
import matplotlib.pyplot as plt

def initPop(PopSize, brd):
    noGenes = len(brd.coord_X)
    dim = brd.dim
        
    Pop = []
    for i in range(0, PopSize):
        ch = Chromozome(noGenes, dim, brd)
        Pop.append(ch)
    return Pop

def evalPop(Pop):
    for ch in Pop:
        ch.eval()

def sumProbabilities(Pop):
    sum = 0
    for ch in Pop:
        sum += ch.fitness

    sumProbabilities = 0
    for ch in Pop:
        sumProbabilities += sum / ch.fitness

    return sum, sumProbabilities


def select2(Pop, sum, sumProbabilities):
    number = random.uniform(0, sumProbabilities)
    for ch in Pop:
        number -= (sum / ch.fitness)
        if(number < 0):
            return ch     
    return Pop[-1]

def select(Pop):
    noSamples = random.randint(1, len(Pop))
    samples = []
    for i in range(0, noSamples):
        samples.append(random.randrange(0, len(Pop)))
    pos = min(samples, key = lambda x : Pop[x].fitness)
    return Pop[pos]

def crossOver(M, F, brd):
    genes = []
    dim = len(M.genes)
    for i in range(0, dim):        
        r = np.random.random_sample()
        if(r < 0.5):    
            genes.append(M.genes[i])
        else:
            genes.append(F.genes[i])
    ch = Chromozome(len(genes), brd.dim, brd)
    ch.setGenes(genes)
    return ch


def crossOver2(M, F, brd):
    r = np.random.random_sample()
    if(r < 0.5):
        M, F = F, M
    dim = len(M.genes)
    genes = []
    for i in range(0, dim//2):
        genes.append(M.genes[i])
    for i in range(dim//2, dim):
        genes.append(F.genes[i])
    #create and return a child Chromozome
    ch = Chromozome(len(genes), brd.dim, brd)
    ch.setGenes(genes)
    return ch


def mutation(ch, noZeros, dim):
    
    r = np.random.random_sample()
    if(r < 0.7):
        x1 = random.randint(0, noZeros - 1)
        x2 = random.randint(0, noZeros - 1)
        x3 = random.randint(0, noZeros - 1)
        x4 = random.randint(0, noZeros - 1)
        ch.genes[x1] = str(random.randint(1, dim))
        ch.genes[x2] = str(random.randint(1, dim))
        ch.genes[x3] = str(random.randint(1, dim))
        ch.genes[x4] = str(random.randint(1, dim))
    return ch
    

def best(Pop):
    return min(Pop, key = lambda ch : ch.fitness)

def selectNewPop(Pop, Pop2):
    pop = sorted(Pop, key = lambda x: x.fitness)
    pop2 = sorted(Pop2, key = lambda x: x.fitness)

    newPop = []
    for i in range(0, len(Pop)//2):
        newPop.append(pop[i])
    for i in range(0, len(Pop2)//2):
        newPop.append(pop2[i])
    return newPop

def EA(noGen, size, brd):
    Pop = initPop(size, brd)
    plotGener = []
    plotFitness = []

    for gens in range(0, noGen):
        evalPop(Pop)
        newPop = []
        
        if(gens % 2 == 0):
            ch = best(Pop)
            print("Generation: ", gens, ", fit: ", ch.fitness)
            plotGener.append(gens)
            plotFitness.append(ch.fitness)
            if(ch.fitness == 0):
                return ch

        #sum, sumProb = sumProbabilities(Pop)
        for i in range(0, size):
            #M = select(Pop, sum, sumProb)
            #F = select(Pop, sum, sumProb)
            M = select(Pop)
            F = select(Pop)
            child = crossOver(M, F, brd)
            child = mutation(child, len(brd.coord_X), brd.dim)
            newPop.append(child)

        Pop = selectNewPop(Pop, newPop)
    evalPop(Pop)
    plt.plot(plotGener, plotFitness)
    plt.show()

    return best(Pop)

