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

        self.distanceTraveled = 0 

        #self position is a random possible coordinate on enviroment,
        #including floats
        self.position = [np.random.random_sample() * env.dim[0],
                         np.random.random_sample() * env.dim[1]]

        
    def act(self, env, world, agent_list):
        self.calcEnergy()
        if env.foodAtPosition(self.position):
            self.eatFood(env)

        self.travel(env, self.search(env))

        if world.tick == world.totalTicks:
            return self.reproduce(agent_list, 2, env, 10, 0.1)

        return agent_list

    def update(self):
        pass

    def calcEnergy(self):
        self.reqEnergy = 1/2 * self.genome["mass"] * math.pow(self.genome["travel"], 2) + self.genome["search"]

    def search(self, env):

        closestFood = None

        for food in env.map:
            distance = math.hypot(
            math.fabs(food[0] - self.position[0]),
            math.fabs(food[1] - self.position[1]))

            if distance<= self.genome["search"] and (closestFood is None or distance < closestFood[1]):
                closestFood = (food, distance)

        return closestFood

    def travel(self, env, food):
        if food == None:
            return self.wander()

        elif self.genome["travel"] >= food[1]:
            self.position = list(food[0])

            self.distanceTraveled += math.hypot(
                self.position[0]-food[0][0],
                self.position[1]-food[0][1])


        elif food[0][0] == self.position[0]:
            self.position[1] += self.genome["travel"]
            return


        else:
            distance = self.genome["travel"] 
            theta = math.atan2(
                    (food[0][1] - self.position[1]),
                    (food[0][0] - self.position[0]))

            self.position[0] += distance * math.cos(theta)
            self.position[1] += distance * math.sin(theta)

            self.distanceTraveled += distance
            
    def eatFood(self, env):
        while env.foodAtPosition(self.position):
            env.removeFoodAtPosition(self.position)
            self.curEnergy += env.foodValue

    def reproduce(self, agent_list, reproduceCost, env, MAX_mass, MAX_deviation):

        while self.curEnergy >= self.reqEnergy + reproduceCost:
            agent_list.append(self.mutateChild(Agent(env, MAX_mass), MAX_deviation))
            self.curEnergy -= reproduceCost

        return agent_list

    def mutateChild(self,child, MAX_deviation):
        child.genome = self.genome
        for k in child.genome.keys():
            child.genome[k] += np.random.choice(
            a = [-1,1]) *  np.random.random_sample() * MAX_deviation

        return child


    def wander(self):
        pass

    def cooperate(self):
        pass


    def defect(self):
        pass

    def moralize(self):
        pass
