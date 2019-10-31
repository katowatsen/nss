import numpy as np

class Enviroment:

    def __init__(self, dimensions):
        self.foodAmount = None
        self.env = np.array(np.zeros(dimensions))

    def setFood(self):

        self.removeAllFood()
        i = 0

        while(i < self.foodAmount):
            randCoord = getRandomCoord()
            self.env[randCoord[0], randCoord[1]] += 1
            i+= 1


    def getRandomCoord(self) 
        return (np.random(0, self.env.shape[0]),
                np.random(0, self.env.shape[1]))

    def removeFoodAtAgent(self, position):
        pass

    def removeAllFood(self):
        self.env = np.array(np.zeros(dimensions))


