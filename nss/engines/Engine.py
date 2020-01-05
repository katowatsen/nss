import multiprocessing as mp
from itertools import chain 
import copy
#import os
from tqdm import tqdm
from ..util.Analysis import Analysis 

class Engine():

    def __init__(self):
        pass

    def run(self, agent_list, env, world):
        print("Running nss:")

        data = []

        pool = mp.Pool(mp.cpu_count())
        
        pbar = tqdm(total = world.totalCycles)

        while world.cycle <= world.totalCycles:
            env.removeAllFood()
            env.setFood()

            avg = 0

            if len(agent_list) != 0:

                avg_genome = agent_list[0].genome.fromkeys(agent_list[0].genome, 0)

            for agent in agent_list:
                agent.curEnergy = 0
                avg += agent.reqEnergy
                for k in agent.genome.keys():

                    avg_genome[k] += agent.genome[k]

            if len(agent_list) != 0:
                avg = avg / len(agent_list)
                for k in agent.genome.keys():

                    avg_genome[k] += agent.genome[k] 

            else:
                avg = "N/A"

            for key in avg_genome.keys():
                avg_genome[key] = avg_genome[key] / len(agent_list)
                

            data.append({"cycle": world.cycle,
                         "length": len(agent_list), 
                         "reqEnergy": avg,
                         "avgSearch": avg_genome['search'],
                         "avgSpeed": avg_genome['speed'],
                         "avgMass": avg_genome['mass'],
                         "avgAltruism": avg_genome['altruism']
                         }) 

            #pairs interaction partners
            i = 1
            for agent in agent_list:
                #tests for last agent in agent list 
                if i == len(agent_list):
                    agent.partner = agent_list[0]

                else:
                    agent.partner = agent_list[i]

                i += 1

            while world.tick <= world.totalTicks:

                agent_list = pool.map(self.worker_determine_next, ((agent, env, world, agent_list) for agent in agent_list))

                #update 
                compiled_list = []
                for agent in agent_list:
                    compiled_list.append(agent.update_strat(env, world, agent_list))


                #tests if complied list has multiple dimentions
                if len(compiled_list) > 0 and isinstance(
                       compiled_list[0], list):

                    #flattens compiled list and assigns it to agent_list
                    agent_list = list(chain.from_iterable(compiled_list))

                else:
                    #creates a shallow copy of compiled_list
                    agent_list = compiled_list.copy()

                world.updateTick()



            world.resetTick()
            pbar.update(1)
            world.updateCycle()

        pool.close()
        pool.join()
        pbar.close()


        analyze = Analysis()

        analyze.write(data)
        analyze.read()

        return agent_list

    def worker_determine_next(self, arg):
        agent, env, world, agent_list = arg
        return agent.determine_next(env, world, agent_list)


