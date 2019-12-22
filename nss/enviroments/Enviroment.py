import numpy as np

class Enviroment:

    def __init__(self, dim, foodAmount):

        self.dim = dim #should be in (x, y) format
        self.foodAmount = foodAmount
        self.map = {}
        self.foodValue = 50


    def setFood(self):
        
        self.removeAllFood()

        for i in range(0, self.foodAmount):
            randCoord = self.getRandomCoord()

            if randCoord in self.map:
                self.map[randCoord] += 1
            else:
                self.map[randCoord] = 1


    def getRandomCoord(self):
        """Calculates a random coordinate based on self.dim 
        dimensions and returns a tuple of the random coordinate"""

        return (np.random.randint(0, self.dim[0]),
                np.random.randint(0, self.dim[1]))

    def foodAtPosition(self, position):

        if tuple(position) in self.map:
            return True
        else:
            return False

    def removeFoodAtPosition(self, position):
        
        if self.map.get(tuple(position)) == 0:
            del self.map[tuple(position)]

        else:
            self.map[tuple(position)] -= 1

    def removeAllFood(self):

        self.map.clear()


