class Engine():

    def __init__(self):
        pass

    def run(self, agent_list, env, world):
        while world.cycle <= world.totalCycles:
            while world.tick <= word.totalTicks:
                for agent in agent_list:
                    agent.act()

                agent.update()
                env.update()
                world.tick += 1
            world.cycle += 1

    def outputToFile(self, IOfile):
        pass

