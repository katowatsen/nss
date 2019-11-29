import numpy as np

class Enviroment:

    def __init__(self, dimensions, foodAmount):
        self.dim = dimensions
        self.foodAmount = foodAmount
        self.map = np.array(np.zeros(self.dim))
        self.foodValue = 500 #temp

    def setFood(self):
        i = 0
        self.removeAllFood()

        while(i < self.foodAmount):
            randCoord = self.getRandomCoord()
            self.map[randCoord[0], randCoord[1]] += 1
            i+= 1


    def getRandomCoord(self): 
        return (np.random.randint(0, self.dim[0]),
                np.random.randint(0, self.dim[1]))

    def foodAtAgent(self, agent):
        if self.map[int(agent.position[0]), int(agent.position[1])]:
            return True
        else:
            return False

    def removeFoodAtAgent(self, agent):
        self.map[agent.position[0],agent.position[1]] -= 1

    def removeAllFood(self):
        self.map = np.array(np.zeros(self.dim))


