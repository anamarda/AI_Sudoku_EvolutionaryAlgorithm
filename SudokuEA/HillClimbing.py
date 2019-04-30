from PopStuff import *
from Chromozome import Chromozome
import numpy as np

def Hill(size, brd, minValue):
    Pop = initPop(size, brd)
    evalPop(Pop)

    plotIter = []
    plotFitness = []

    xStar = best(Pop)
    x = best(Pop)
    #Tabu = []
    iter = 0

    noGenes = len(brd.coord_X)
    dim = brd.dim

    while(True):
        plotIter.append(iter)
        plotFitness.append(x.fitness)

        iter += 1

        if(iter % 10 == 0):
            print("Iteration: ", iter, " - fitness: ", x.fitness)
            if(iter % 100 == 0):
                print(x.genes)

        subset = []
        for i in range(0, size):
            pos1 = random.randint(0, len(brd.coord_X) - 1) 
            pos2 = random.randint(0, len(brd.coord_X) - 1) 
            ch = Chromozome(noGenes, dim, brd)
            ch.genes = np.array(x.genes)
            ch.genes[pos1] = str(random.randint(1, brd.dim))
            ch.genes[pos2] = str(random.randint(1, brd.dim))
            #if(ch not in tabu):
            subset.append(ch)

        evalPop(subset)
        s = best(subset)
        if(s.fitness < x.fitness):
            x = s
        elif(np.random.random_sample() < 0.4):
            x = s
        
        if(x.fitness < minValue):
            plt.plot(plotIter, plotFitness)
            plt.show()
            return x