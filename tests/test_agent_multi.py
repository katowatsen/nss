from ..nss.enviroments.Enviroment import Enviroment
from ..nss.agents.Agent import Agent
from ..nss.worlds.World import World 
import time 
from itertools import chain

import numpy as np

def test_reproduce():
    env = Enviroment((5,5),2)
    agent_list = [Agent(env, 2) for i in range(0,1)]
    agent_list[0].curEnergy = 10
    agent_list[0].reqEnergy = 2
    reproduced = agent_list[0].reproduce(env,2, 2, 0.01)

    for agent in reproduced:
        agent_list.append(agent)

    assert agent_list[0].curEnergy == agent_list[0].reqEnergy and (len(agent_list) == 5) and id(agent.genome) != id(agent_list[1].genome)

def test_mutateChild():
    env = Enviroment((5,5),2)
    np.random.seed(10)
    t_agent = Agent(env, 2)

    assert t_agent.genome != t_agent.mutateChild(Agent(env, 2), 0.1)

def test_timings():
    np.random.seed(0)

    env = Enviroment((100,100), 1)
    env.setFood()
    world = World(10,10)
    agent = Agent(env, 2)

    agent_list = [agent]


    start_search = time.time()
    agent.determine_next(env, world, agent_list)
    end_search = time.time()

    start_travel = time.time()
    agent.update_strat(env, world, agent_list)
    end_travel = time.time()

    start2 = time.time()
    agent.search(env)
    end2 = time.time()


    search_time = end_search - start_search
    travel_time = end_travel - start_travel
    time2 = end2-start2


    assert search_time != travel_time 


