import numpy as np
from Repo import Repo
from Board import Board
from Chromozome import Chromozome
from PopStuff import EA
import winsound
from HillClimbing import *

repo = Repo("data\data3.txt")
b = Board(repo.getBoard(), repo.getDim())

NoGener = 500
PopSize = 100

#res = EA(NoGener, PopSize, b)
res2 = Hill(PopSize, b, 6)

#print(res.genes)
print(res2.genes)

for i in range(0, len(b.coord_X)):
#    b.setXY(b.coord_X[i], b.coord_Y[i], res.genes[i])
    b.setXY(b.coord_X[i], b.coord_Y[i], res2.genes[i])

#print(res.fitness)
print(res2.fitness)

print(b.matrix)

duration = 1000  # milliseconds
freq = 550  # Hz 
winsound.Beep(freq, duration)

#o sa las astea aici ca sa ma asigur ca nu le uit

#sunet de alerta
#print ("\a")

#de cate ori apare '2' pe linia 3
#print(np.count_nonzero(b.board[3, :] == '2'))

#creez un vector
#values = ['1', '2', '3', '4']
#se creeaza un vector boolean care scrie True/False pe pozitia elementelor din values daca apar sau nu in al doilea array
#print(np.in1d(values, np.array((repo.board[0,:]))))

#afiseaza matricea
#print(repo.board)

#afiseaza linia 0
#print(repo.board[0,:])

#afiseaza 2 vectori de coordonate X si Y
#print(np.where(repo.board == '0'))