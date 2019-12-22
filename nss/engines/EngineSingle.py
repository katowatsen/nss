from itertools import chain
import copy

class EngineSingle():

    def __init__(self):
        pass

    def run(self, agent_list, env, world):

        while world.cycle <= world.totalCycles:

            env.removeAllFood()
            env.setFood()

            for agent in agent_list:
                agent.curEnergy = 0

            while world.tick <= world.totalTicks:


                for agent in agent_list:
                    agent.determine_next(env, world, agent_list)

                compiled_list = []

                for agent in agent_list:
                    compiled_list.append(agent.update_strat(
                                         env, world, agent_list))

                if len(compiled_list) > 0 and isinstance(compiled_list[0], list):
                    #flattens compiled list and assigns it to agen_list
                    agent_list = list(chain.from_iterable(compiled_list))

                else:
                    agent_list = copy.deepcopy(compiled_list) 
                    

                world.updateTick()

            world.resetTick()
            world.updateCycle()

        return agent_list
