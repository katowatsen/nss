class World():

    def __init__(self, totalCycles, totalTicks):
        self.tick = 0
        self.cycle = 0
        self.totalTicks = totalTicks
        self.totalCycles = totalCycles

    def updateTick(self):
        self.tick += 1

    def updateCycle(self):
        self.cycle = 0
