class World():

    def __init__(self, totalCycles, totalTicks):
        self.cycle = 1 
        self.tick = 1
        self.totalCycles = totalCycles
        self.totalTicks = totalTicks
        self.removeAgentsList = []

    def resetTick(self):
        self.tick = 1

    def updateTick(self):
        self.tick += 1

    def updateCycle(self):
        self.cycle += 1

    def removeAgents(self, agentList):

        #removes duplicate agents from agentList 
        self.removeAgentsList = list(set(self.removeAgentsList))

        for agent in self.removeAgentsList:
            agentList.remove(agent)

        self.removeAgentsList.clear()

        return agentList
