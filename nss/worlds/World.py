import numpy as np

class World():

    def __init__(self, totalCycles, totalTicks):
        self.cycle = 1 
        self.tick = 1
        self.totalCycles = totalCycles
        self.totalTicks = totalTicks
        self.removeAgentsList = []
        self.rep_mean = None 
        self.rep_deviation = None
        self.rep_threshold = -1

    def resetTick(self):
        self.tick = 1

    def updateTick(self):
        self.tick += 1

    def updateCycle(self):
        self.cycle += 1

    def removeAgents(self, agent_list):

        #removes duplicate agents from agentList 
        self.removeAgentsList = list(set(self.removeAgentsList))

        for agent in self.removeAgentsList:
            agent_list.remove(agent)

        self.removeAgentsList.clear()

        return agent_list 

    def calcStats(self, agent_list):
        reputation = [agent.reputation for agent in agent_list]
        if len(agent_list) == 1:
            self.rep_deviation = 1
            self.rep_mean = reputation[0] - 0.01

        else:
            self.rep_deviation = np.std(reputation)
            self.rep_mean = np.mean(reputation)



