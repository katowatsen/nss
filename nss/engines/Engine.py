from multiprocessing import Pool
from functools import partial

class Engine():

    def __init__(self):
        pass

    def run(self, agent_list, env, world):

        while world.cycle <= world.totalCycles:
            env.setFood()

            while world.tick <= world.totalTicks:



                pool = Pool(4)
                result = pool.map(self.worker, ((agent, env, world, agent_list) for agent in agent_list))

                #for agent in agent_list:
                #    agent.act(env,world, agent_list)
                pool.close()
                pool.join()

                world.updateTick()


            world.resetTick()
            world.updateCycle()

        return agent_list 

    def worker(self, arg):
        agent, env, world, agent_list = arg
        return agent.act(env, world, agent_list)

    def outputToFile(self, IOfile):
        pass

