import math
import numpy as np
import copy

class Agent():

    def __init__(self, env, world, MAX_mass):
        self.MAX_mass = MAX_mass
        #initalizes a genome with random genes
        self.genome = {
                  #MAX search length is the diagonal of the enviroment
                  "search": np.random.random_sample() * math.hypot(
                                env.dim[0], env.dim[1]) / world.totalTicks,

                  #MAX travel distance is the diagonal of the enviroment
                  "travel": np.random.random_sample() * math.hypot(
                                env.dim[0], env.dim[1]) /world.totalTicks,

                  #MAX mass is a predefined constatnt
                  "mass": np.random.random_sample()* MAX_mass,


                  #altruism is a probability that one will act altrusticly
                  "altruism": np.random.random_sample() 

                  }

        self.curEnergy = 0
        self.reqEnergy = self.genome["mass"] * 0.5 *math.pow(self.genome["travel"], 2) + self.genome["search"]

        self.fitness = None #might remove
        self.distanceTraveled = 0 


        '''self position is a random possible coordinate on enviroment,
        including floats'''
        self.position = [np.random.random_sample() * env.dim[0],
                         np.random.random_sample() * env.dim[1]]

    def determine_next(self, env, world, agent_list):
        '''tasks should be parralizable'''
        #moralize
        self.travel(self.search(env)) 

        return self



    def update_strat(self, env, world, agent_list):

        if env.foodAtPosition(self.position):
            #make sure another agent isn't at this position
            #if another agent is at this position:
            #do altrustic/selfish behavior
            self.eatFood(env)

        if world.tick == world.totalTicks:
            sub_agent_list = self.reproduce(env,world, 10, self.MAX_mass, 5)
            '''kills current agent if it does not have
            required energy at the end of cycle'''
            
            if self.curEnergy >= self.reqEnergy and self.reqEnergy > 0:
                sub_agent_list.insert(0, self)

            return sub_agent_list

        return [self]

    def search(self, env):

        closestFood = None

        #calculates closest food to agent
        for food in env.map:
            distance = math.hypot(
            math.fabs(food[0] - self.position[0]),
            math.fabs(food[1] - self.position[1]))

            if distance<= self.genome["search"] and (closestFood is None or distance < closestFood[1]):
                closestFood = (food, distance)

        return closestFood

    def travel(self, nextPosition):
        if nextPosition == None:
            return self.wander()

        elif self.genome["travel"] >= nextPosition[1]:
            self.position = list(nextPosition[0])

            self.distanceTraveled += math.hypot(
                self.position[0]-nextPosition[0][0],
                self.position[1]-nextPosition[0][1])

        elif nextPosition[0][0] == self.position[0]:
            self.position[1] += self.genome["travel"]

        else:
            distance = self.genome["travel"] 
            theta = math.atan2(
                    (nextPosition[0][1] - self.position[1]),
                    (nextPosition[0][0] - self.position[0]))

            self.position[0] += distance * math.cos(theta)
            self.position[1] += distance * math.sin(theta)

            self.distanceTraveled += distance
            
    def eatFood(self, env):
        while env.foodAtPosition(self.position):
            env.removeFoodAtPosition(self.position)
            self.curEnergy += env.foodValue

    def reproduce(self, env, world, reproduceCost, MAX_mass, MAX_deviation):
        sub_agent_list = []

        while self.curEnergy >= self.reqEnergy + reproduceCost and self.reqEnergy > 0:
            child = Agent(env,world, MAX_mass)
            sub_agent_list.append(self.mutateChild(child, MAX_deviation))

            self.curEnergy -= reproduceCost

        return sub_agent_list

    def mutateChild(self, child, MAX_deviation):

        child.genome.clear()
        child.genome = copy.deepcopy(self.genome)
        for k in child.genome.keys():

            child.genome[k] += np.random.choice(
            a = [-1,1]) * np.random.random_sample() * MAX_deviation

            if child.genome[k] < 0:
                child.genome[k] = np.random.random_sample()*MAX_deviation

        child.reqEnergy = child.genome["mass"] * 0.5 *math.pow(child.genome["travel"], 2) + child.genome["search"]

        return child


    def wander(self):
        pass

    def cooperate(self):
        pass


    def defect(self):
        pass

    def moralize(self):
        pass
