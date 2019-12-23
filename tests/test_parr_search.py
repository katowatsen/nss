from ..nss.enviroments import Enviroment 
from ..nss.agents import Agent
from ..nss.worlds import World

import multiprocessing as mp
import numpy as np
from time import time

def test_search_timing():
    np.random.seed(0)

    world = World.World(100,100)
    env = Enviroment.Enviroment((1000,1000), 2000)

    env.foodValue = 100 
    env.setFood()

    agent_list = [Agent.Agent(env,world, 10) for i in range(0,10000)]

    start_reg = time()
    for agent in agent_list:
        agent.determine_next(env, world, agent_list)

    end_reg = time()

    pool = mp.Pool(mp.cpu_count())

    start_multi = time()
    pool.map(detr, ((agent, env, world, agent_list) for agent in agent_list))
    end_multi = time()

    reg_time = end_reg - start_reg 
    multi_time = end_multi - start_multi 

    assert reg_time > multi_time

def detr(arg):
    agent, env, world, agent_list = arg
    return agent.determine_next(env, world, agent_list)

