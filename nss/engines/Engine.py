import multiprocessing as mp
from itertools import chain 
import copy
#import os
from tqdm import tqdm
from ..util.Analysis import Analysis 
import time

class Engine():

    def __init__(self):
        pass

    def run(self, agent_list, env, world):
        print("Running nss:")
        analyze = Analysis()

        data = []

        pool = mp.Pool(mp.cpu_count())
        
        pbar = tqdm(total = world.totalCycles)


        while world.cycle <= world.totalCycles:

            #does things before the cycle begins

            #prepares enviroment
            env.removeAllFood()
            env.setFood()
            env.foodPool = 0

            #averages genome attributes of the agents
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
                

            #prepares data for output 
            data.append({"cycle": world.cycle,
                         "length": len(agent_list), 
                         "reqEnergy": avg,
                         "avgSearch": avg_genome['search'],
                         "avgSpeed": avg_genome['speed'],
                         "avgMass": avg_genome['mass'],
                         "avgAltruism": avg_genome['altruism']
                         }) 

            if world.cycle == 1:
                analyze.writeHeaders(data)




            #pairs interaction partners

            i = 1
            for agent in agent_list:
                #tests for last agent in agent list 
                if i % 2 == 0:
                    agent.partner = copy.copy(
                    agent_list[i-2].communicate(
                    agent_list[i-2].determineAltruism()))

                elif i == len(agent_list):
                    agent.partner = None

                else:
                    agent.partner = copy.copy(
                    agent_list[i].communicate(
                    agent_list[i].determineAltruism()))

                i += 1

            while world.tick <= world.totalTicks:

                #agents interact with each other

                agent_list = pool.map(self.worker_determine_next, ((agent, env, world, agent_list) for agent in agent_list))
                
                if world.tick == world.totalTicks:
                    #add food to foodPool
                    for agent in agent_list:
                        agent.shareFood(env, agent.determineAltruism())

                #update 
                compiled_list = []

                for agent in agent_list:
                    compiled_list.append(agent.update_strat(env, world, agent_list))

                #tests if complied list has multiple dimentions
                if len(compiled_list) > 0 and isinstance(
                       compiled_list[0], list):

                    #flattens compiled list and assigns it to agent_list
                    if world.tick == world.totalTicks:
                        #removes agents
                        compiled_list.append(world.removeAgents(agent_list))
                        agent_list = list(chain.from_iterable(compiled_list)) 

                else:
                    compiled_list = world.removeAgents(compiled_list)
                    agent_list = copy.copy(compiled_list)

                world.updateTick()


            analyze.writeRow(data)
            data.clear()

            world.resetTick()
            world.updateCycle()
            pbar.update(1)

        pool.close()
        pool.join()
        pbar.close()



        analyze.read()

        return agent_list

    def worker_determine_next(self, arg):
        agent, env, world, agent_list = arg
        return agent.determine_next(env, world, agent_list)
