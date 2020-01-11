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
                  "altruism": np.random.random_sample(),

                
                  #probability that agent will sense defection in sharing food to an individual agent

                  "senseSharing": np.random.random_sample(),

                  #probability that agent will sense defection in sharing food to the entire group

                  "senseDonation": np.random.random_sample(),
                  #probability that agent will sense defection in communication 
                  "senseCommunication": np.random.random_sample(),

                  }

        self.curEnergy = 0
        self.reqEnergy = self.genome["mass"] * 0.5 *math.pow(self.genome["speed"], 2) + self.genome["search"]

        self.fitness = None #might remove
        self.distanceTraveled = 0 
        self.closestFood = None
        self.partner = None
        self.reputation = 0 


        '''self position is a random possible coordinate on enviroment,
        including floats'''
        self.position = [np.random.random_sample() * env.dim[0],
                         np.random.random_sample() * env.dim[1]]

    def determine_next(self, env, world, agent_list):
        '''tasks should be parralizable'''

        self.travel(self.search(env), env)

        return self



    def update_strat(self, env, world, agent_list):

        if env.foodAtPosition(self.position):
            #make sure another agent isn't at this position
            #if another agent is at this position-
            #do altrustic/selfish behavior

            for other_agent in agent_list:
                if other_agent.position == self.position and id(other_agent) != id(self):
                    self.negotiate(other_agent, world, env)

            self.eatFood(env)
        self.senseCommunication(agent_list)

        #agent reproduces and if conditions are not satisified, is removed from model
        if world.tick == world.totalTicks:
            self.curEnergy += env.foodPool/len(agent_list)
            reproducedAgents = self.reproduce(env,world,10,0.5)
            '''kills current agent if it does not have
            required energy at the end of cycle'''
            
            if self.curEnergy < self.reqEnergy:
                Agent.removeAgent(self, world)

            return reproducedAgents
        return self

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

    def reproduce(self, env, world, reproduceCost, MAX_deviation):
        reproduced = []

        while self.curEnergy >= self.reqEnergy + reproduceCost and self.reqEnergy > 0:
            child = Agent(env,world, self.MAX_mass)
            reproduced.append(self.mutateChild(child, MAX_deviation))

            self.curEnergy -= reproduceCost

        return reproduced 

    def mutateChild(self, child, MAX_deviation):

        child.genome.clear()
        child.genome = copy.deepcopy(self.genome)
        for k in child.genome.keys():

            child.genome[k] += np.random.choice(
            a = [-1,1]) * np.random.random_sample() * MAX_deviation

            if child.genome[k] < 0:
                child.genome[k] = 0.00001


        if child.genome["altruism"] > 1:
            child.genome["altruism"] = 1

        if child.genome["mass"] > child.MAX_mass:
            child.genome["mass"] = child.MAX_mass

        child.reqEnergy = child.genome["mass"] * 0.5 *math.pow(child.genome["speed"], 2) + child.genome["search"]

        return child

    def negotiate(self, other_agent, world, env):
        thisAction = self.determineAltruism()
        otherAction = other_agent.determineAltruism()

        if thisAction == otherAction and thisAction == True:
            #split food
            self.splitFood(other_agent,  env)

        elif thisAction == False and otherAction == True:
            self.eatFood
            #this agent takes food

        elif thisAction == True and otherAction == False:
            #the other agent takes food
            other_agent.eatFood(env)

        else:
            #fights over food
            if self.genome["mass"] > other_agent.genome["mass"]:
                self.eatFood(env)
                #remove agent from list
                self.eatAgent(world, other_agent)

            elif self.genome["mass"] < other_agent.genome["mass"]:
                other_agent.eatFood(env)
                #remove agent from list
                other_agent.eatAgent(world, self)

            else:
                #split food
                multiplier = self.splitFood(other_agent,  env)

                #removes energy from each agent as toll for fighting...
                #results in each agent getting only 1/4 of the food value
                self.curEnergy -= env.foodValue/4 * multiplier
                other_agent.curEnergy -= env.foodValue/4 * multiplier

    def splitFood(self, other_agent, env):
        #accounts for multiple instances of food in one location
        
        multiplier = 0 
        preFood = self.curEnergy
        while(env.foodAtPosition(self.position)):

            self.eatFood(env)
            foodValue = self.curEnergy - preFood

            self.curEnergy -= foodValue/2
            other_agent.curEnergy += foodValue/2
            multiplier += 1

        return multiplier

    def eatAgent(self, world, other_agent):
        self.curEnergy += other_agent.curEnergy
        Agent.removeAgent(other_agent, world)

    def removeAgent(agent, world):
        world.removeAgentsList.append(agent)

    def determineAltruism(self):

        if np.random.random_sample() <= self.genome["altruism"]:
            return True
        else:
            return False 

    def communicate(self, isAltrustic):
        if isAltrustic == True:
            self.didCommunicate = True
            return self
            
        else:
            self.didCommunicate = False
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

        self.reputation += 1


    def defect(self, env):
        self.reputation -= 1

    def senseCommunication(self, agent_list):
        if self.partner == None:
            if np.random.random_sample() <= self.genome["senseCommunication"]:
                for agent in agent_list:
                    if agent.partner != None and self.genome == agent.partner.genome:
                        #lowers reputation of defecting agent
                        agent.reputation -=1
        else:
            if np.random.random_sample() <= self.genome["senseCommunication"]:
                for agent in agent_list:
                    if agent.partner != None and self.genome == agent.partner.genome:
                        #raises reputation of defecting agent
                        agent.reputation +=1

        return agent_list
