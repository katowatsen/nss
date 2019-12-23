from ..nss.enviroments.Enviroment import Enviroment
from ..nss.agents.Agent import Agent
from ..nss.worlds.World import World 
import itertools
import time 
import copy
import numpy as np

def test_genome():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment((100,100),60)

    agent = Agent(env, world, 10)

    nrg = copy.copy(agent.reqEnergy)

    initial_genome = agent.genome.copy()

    agent.curEnergy = 1000000
    agent.reproduce(env,world, 1000, 10, 1)
    agent.determine_next(env, 1000, [agent])
    agent.eatFood(env)
    agent.curEnergy = 1000000
    reproduced = agent.reproduce(env, world, 1000, 10, 1)
    reproduced.append(agent)

    agent = reproduced[-1]

    print(agent.genome)
    print(agent.reqEnergy)

    

    assert nrg == agent.reqEnergy
