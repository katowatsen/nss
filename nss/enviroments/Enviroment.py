import numpy as np

class Enviroment:

    def __init__(self, dim, foodAmount):

        self.dim = dim #dim should be in row, col format
        self.foodAmount = foodAmount
        self.map = np.array(np.zeros(self.dim))
        self.foodValue = 500 #temp


    def setFood(self):
        '''Clears present food and sets food in the enviroment.'''
        i = 0
        self.removeAllFood()

        while(i < self.foodAmount):
            randCoord = self.getRandomCoord()
            self.map[randCoord[0], randCoord[1]] += 1
            i+= 1


    def getRandomCoord(self): 
        """Calculates a random coordinate based on the array's dimensions
        and returns a tuple of the random coordinate"""

        return (np.random.randint(0, self.dim[0]),
np.random.randint(0, self.dim[1]))
                
    def foodAtAgent(self, agent):
        '''Determins if food is located at the agent.'''

        if self.map[int(agent.position[0]), int(agent.position[1])]:
            return True
        else:
            return False

    def removeFoodAtAgent(self, agent):
        '''Removes food at the agent's position'''

        self.map[agent.position[0],agent.position[1]] -= 1

    def removeAllFood(self):
        '''Removes all food in the enviroment.'''

        self.map = np.array(np.zeros(self.dim))






