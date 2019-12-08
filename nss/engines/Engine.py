from multiprocessing import Pool
from itertools import chain 

class Engine():

    def __init__(self):
        pass

    def run(self, agent_list, env, world):
        pool = Pool(4)

        while world.cycle <= world.totalCycles:
            env.setFood()

            while world.tick <= world.totalTicks:

                result = pool.map(self.worker, ((agent, env, world, agent_list) for agent in agent_list))
                if isinstance(result[0], list):
                    agent_list = list(chain.from_iterable(result))

                else:
                    agent_list = result 
                #print(agent_list)


                #for agent in agent_list:
                #    agent.act(env,world, agent_list)

                world.updateTick()


            world.resetTick()
            world.updateCycle()

        pool.close()
        pool.join()
        return agent_list

    def worker(self, arg):
        agent, env, world, agent_list = arg
        return agent.act(env, world, agent_list)

    def outputToFile(self, IOfile):
        pass

