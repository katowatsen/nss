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
        self.position = (np.random.random_sample() * env.dim[0],
                         np.random.random_sample() * env.dim[1])

    def calcEnergy(self):
        pass

    def act(self):
        #evaluate decissions based on genome and probability
        pass

    def search(self):
        pass

    def travel(self):
        pass

    def eatFood(self):
        pass

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
