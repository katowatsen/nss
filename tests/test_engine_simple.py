from ..nss.enviroments import Enviroment 
from ..nss.agents import Agent
from ..nss.engines import Engine
from ..nss.engines import EngineSingle
from ..nss.worlds import World
import numpy as np
from time import time
import copy

def test_run():
    np.random.seed(0)

    engine = Engine.Engine()
    world = World.World(10,5)

    env = Enviroment.Enviroment((100,100), 40)
    env.foodValue = 100 
    env.setFood()

    agent_list = [Agent.Agent(env, world, 2) for i in range(0,100)]
    pre_agent_list_len = len(agent_list)

    agent_list = engine.run(agent_list, env, world)

    assert pre_agent_list_len != len(agent_list) and world.cycle-1 == world.totalCycles 

def test_timed_run():
    np.random.seed(100)
    world = World.World(10,5)

    single_engine = EngineSingle.EngineSingle()
    multi_engine = Engine.Engine()

    env = Enviroment.Enviroment((1000,1000), 100)
    env.foodValue = 100 

    agent_list = [Agent.Agent(env, world, 2) for i in range(0,100)]

    startA = time()
    np.random.seed(10)
    resultsA = multi_engine.run(copy.deepcopy(agent_list), copy.copy(env), copy.copy(world)).copy()
    stopA = time()

    startB = time()
    np.random.seed(10)
    resultsB = single_engine.run(copy.deepcopy(agent_list), copy.copy(env), copy.copy(world)).copy()
    stopB = time()

    engineruntimeA = stopA - startA 
    engineruntimeB = stopB - startA 


    agentA = resultsA[0]
    agentB = resultsB[0]

    a = agentA.genome


    '''tests that the multiprocessed engine runs faster than the single
    processed engine. Also, both engines should return the same things,
    and the returned agent's genomes shouldn't be modified throughout
    the running of the engine.'''
    assert engineruntimeA < engineruntimeB and len(resultsA) == len(resultsB ) and agentA.genome == agentB.genome
