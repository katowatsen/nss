import math
import numpy as np
import copy

class Agent():

    def __init__(self, env, world, MAX_mass):
        self.MAX_mass = MAX_mass
        #initalizes a genome with random genes
        self.genome = {
                  #MAX search length is the diagonal of the enviroment
                  "speed": np.random.random_sample() * math.hypot(
                                env.dim[0], env.dim[1]) / world.totalTicks,

                  #MAX search distance is the diagonal of the enviroment
                  "search": np.random.random_sample() * math.hypot(
                                env.dim[0], env.dim[1]) /world.totalTicks,

                  #MAX mass is a predefined constatnt
                  "mass": np.random.random_sample()* MAX_mass,

                  #altruism is a probability that one will act altrusticly
                  "altruism": np.random.random_sample() / 10
                  

                  }

        self.curEnergy = 0
        self.reqEnergy = self.genome["mass"] * 0.5 *math.pow(self.genome["speed"], 2) + self.genome["search"] 

        self.fitness = None #might remove
        self.distanceTraveled = 0 
        self.closestFood = None
        self.partner = None
        self.reputation = None


        '''self position is a random possible coordinate on enviroment,
        including floats'''
        self.position = [np.random.random_sample() * env.dim[0],
                         np.random.random_sample() * env.dim[1]]

    def determine_next(self, env, world, agent_list):
        '''tasks should be parralizable'''
        #moralize

        self.travel(self.search(env), env)

        return self



    def update_strat(self, env, world, agent_list):

        if env.foodAtPosition(self.position):
            #make sure another agent isn't at this position
            #if another agent is at this position:
            #do altrustic/selfish behavior
            self.eatFood(env)

        if world.tick == world.totalTicks:
            self.curEnergy += env.foodPool/len(agent_list)
            sub_agent_list = self.reproduce(env,world,10,self.MAX_mass,1)
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

            if self.partner != None:

                if distance <= self.genome["search"] or distance <= self.partner.genome["search"] and (closestFood is None or distance < closestFood[1]):
                    closestFood = (food, distance)

            else:
                if distance <= self.genome["search"] and (closestFood is None or distance < closestFood[1]):
                    closestFood = (food, distance)

        return closestFood

    def travel(self, nextPosition, env):
        if nextPosition == None:
            return self.wander(env)

        elif self.genome["speed"] >= nextPosition[1]:
            self.position = list(nextPosition[0])

            self.distanceTraveled += math.hypot(
                self.position[0]-nextPosition[0][0],
                self.position[1]-nextPosition[0][1])

        elif nextPosition[0][0] == self.position[0]:
            self.position[1] += self.genome["speed"]

        else:
            distance = self.genome["speed"] 
            theta = math.atan2(
                    (nextPosition[0][1] - self.position[1]),
                    (nextPosition[0][0] - self.position[0]))

            self.position[0] += distance * math.cos(theta)
            self.position[1] += distance * math.sin(theta)

            self.distanceTraveled += distance
            
    def wander(self, env):
        circm = []

        angles = np.radians(list(range(0,360)))

        for angle in angles:
            point = [
                self.position[0] + self.genome["speed"] * math.cos(angle),
                self.position[1] + self.genome["speed"] * math.sin(angle)]

            point.append(math.hypot(point[1]-self.position[1], point[0]-self.position[0]))

            if env.dim[0] >= point[0] >= 0 and env.dim[1] >= point[1] >= 0:
                circm.append(point)


        if len(circm) != 0:
            randPoint = circm[np.random.randint(len(circm))]
            self.position = list(randPoint)

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


        child.reqEnergy = child.genome["mass"] * 0.5 *math.pow(child.genome["speed"], 2) + child.genome["search"]
        if child.genome["altruism"] > 10:
            child.genome["altruism"] = 10

        return child

    def interact(self, world, env):
        if np.random.random_sample() < self.genome["altruism"]:
            isAltrustic = True

        else:
            isAltrustic = False

        #determines whether to share food or communicate
        if world.tick == 1:

            return self.communicate(isAltrustic)

        elif world.tick == world.totalTicks:

             self.shareFood(env, isAltrustic)

    def communicate(self, isAltrustic):
        if isAltrustic == True:
            return self
        else:
            return None

    def shareFood(self, env, isAltrustic):
        if isAltrustic == True:
            self.cooperate(env)

        else:
            self.defect(env)

    def cooperate(self, env):
        if self.curEnergy >= self.reqEnergy:
            env.foodPool += (self.curEnergy - self.reqEnergy) / 2
            self.curEnergy -= (self.curEnergy - self.reqEnergy) / 2


    def defect(self, env):
        # does nothing
        pass


    def moralize(self):
        pass
