class World():

    def __init__(self, totalCycles, totalTicks):
        self.cycle = 0
        self.tick = 0
        self.totalCycles = totalCycles
        self.totalTicks = totalTicks

    def updateTick(self):
        self.tick += 1

    def updateCycle(self):
        self.cycle += 1
