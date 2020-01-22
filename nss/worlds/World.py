import numpy as np
import scipy.stats as st


class World():

    def __init__(self, totalCycles, totalTicks):
        self.cycle = 1 
        self.tick = 1
        self.totalCycles = totalCycles
        self.totalTicks = totalTicks
        self.removeAgentsList = []
        self.rep_mean = None 
        self.rep_deviation = None
        self.rep_threshold = None 

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

    def calcThreshold(self, agent_list):
        total_tolerance = 0
        for agent in agent_list:
            total_tolerance += agent.genome["tolerance"]

        avg_tolerance = total_tolerance / len(agent_list) 
        self.rep_threshold = st.norm.ppf(avg_tolerance)

    def calcStats(self, agent_list):
        self.calcThreshold(agent_list)

        reputation = [agent.reputation for agent in agent_list]
        if len(agent_list) == 1:
            self.rep_deviation = 1
            self.rep_mean = reputation[0] - 0.01

        else:
            self.rep_deviation = np.std(reputation)
            self.rep_mean = np.mean(reputation)





