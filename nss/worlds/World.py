class World():

    def __init__(self, totalCycles, totalTicks):
        self.cycle = 1 
        self.tick = 1
        self.totalCycles = totalCycles
        self.totalTicks = totalTicks

    def resetTick(self):
        self.tick = 1

    def updateTick(self):
        self.tick += 1

    def updateCycle(self):
        self.cycle += 1
