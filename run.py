from nss.enviroments import Enviroment 
from nss.agents import Agent
from nss.engines import Engine
from nss.engines import EngineSingle
from nss.worlds import World
import numpy as np
from time import time
import copy

def run():
    np.random.seed(100)

    engine = Engine.Engine()
    world = World.World(10000,5)

    env = Enviroment.Enviroment((100,100), 60)
    env.foodValue = 90 
    env.setFood()

    agent_list = [Agent.Agent(env, world, 100) for i in range(0,100)]
    pre_agent_list_len = len(agent_list)

    agent_list = engine.run(agent_list, env, world)

run()
