import numpy as np

class Enviroment:

    def __init__(self, dimensions, foodAmount):
        self.dim = dimensions
        self.foodAmount = foodAmount
        self.env = np.array(np.zeros(self.dim))

    def setFood(self):
        i = 0
        self.removeAllFood()

        while(i < self.foodAmount):
            randCoord = self.getRandomCoord()
            self.env[randCoord[0], randCoord[1]] += 1
            i+= 1


    def getRandomCoord(self): 
        return (np.random.randint(0, self.dim[0]),
                np.random.randint(0, self.dim[1]))

    def removeFoodAtAgent(self, agent):
        pass

    def removeAllFood(self):
        self.env = np.array(np.zeros(self.dim))


