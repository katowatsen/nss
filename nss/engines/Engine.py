class Engine():

    def __init__(self):
        pass

    def run(self, agent_list, env, world):

        while world.cycle <= world.totalCycles:
            while world.tick <= world.totalTicks:
                for agent in agent_list:
                    agent.act(env,world, agent_list)

                world.updateTick()


            world.tick = 0
            world.updateCycle()

        return agent_list 

    def outputToFile(self, IOfile):
        pass

