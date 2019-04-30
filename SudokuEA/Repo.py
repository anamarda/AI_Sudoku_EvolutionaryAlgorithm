import numpy

class Repo(object):

    def readAllFromFile(self):
        with open(self.fileName,"r") as f:
            self.dim = int(f.readline().strip())

            line = f.readline()
            line = line.strip()
            nr = line.split(",")

            self.board = numpy.array(nr)
            for line in f.readlines():
                line = line.strip()

                if len(line) > 0:
                    numbers = line.split(",")
                    a = self.board
                    b = numpy.array(numbers)
                    self.board = numpy.vstack((a, b))

    def __init__(self, fileName):
        self.dim = 0
        self.board = []
        self.fileName = fileName
        self.readAllFromFile()

    def getBoard(self):
        return self.board[:]

    def getDim(self):
        return self.dim