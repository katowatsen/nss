import math
import numpy as np

class Agent():

    def __init__(self, env, MAX_mass):
        #initalizes a genome with random genes
        self.genome = {
                  #MAX search length is the diagonal of the enviroment
                  "search": np.random.random_sample() *
                           math.hypot(env.dim[0], env.dim[1]),

                  #MAX travel distance is the diagonal of the enviroment
                  "travel": np.random.random_sample() *
                           math.hypot(env.dim[0], env.dim[1]),

                  #MAX mass is a predefined constatnt
                  "mass": np.random.random_sample()* MAX_mass,

                  #altruism is a probability that one will act altrusticly
                  "altruism": np.random.random_sample() 
                  }

        self.curEnergy = 0
        self.reqEnergy = None
        self.fitness = None #might remove

        #self position is a random possible coordinate on enviroment,
        #including floats
        self.position = [np.random.random_sample() * env.dim[0],
                         np.random.random_sample() * env.dim[1]]

    def calcEnergy(self):
        pass

    def act(self, env):
        if env.foodAtAgent(self):
            self.eatFood(env)

        self.search()


    def search(self, env):
        #should be performed if food pos != agent pos
        seenFood = []
        for row in range(0, env.dim[0]):
            for col in range(0, env.dim[1]):
                if env.map[row][col] >= 1: 
                    distance = math.hypot(
                    math.fabs(row - self.position[0]),
                    math.fabs(col - self.position[1]))

                    if self.genome["search"] >= distance:
                        seenFood.append(((row,col), distance))

        if len(seenFood) > 0:
            return sorted(seenFood, key = lambda e: e[1])[0]
        else:
            return None
            
    def travel(self, env, food):
        if self.genome["speed"] >= food[1]:
            self.position = food[0]

        else:
            dis = self.genome["speed"] 
            theta = math.atan(
                    (food[0][1] - self.position[1])/
                    (food[0][0] - self.position[0]))

            self.position[0] = math.fabs(dis * math.cos(theta) + food[0][0] - self.position[0])
            self.position[1] = math.fabs(dis * math.cos(theta) + food[0][1] - self.position[1])
            
    def eatFood(self, env):
        while env.map[agent.position[0], agent.position[1]] != 0:
            env.removeFoodAtAgent(self)

    def reproduce(self):
        pass

    def mutateChild(self):
        pass

    def cooperate(self):
        pass

    def defect(self):
        pass

    def moralize(self):
        pass
