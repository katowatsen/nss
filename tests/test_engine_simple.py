from ..nss.enviroments import Enviroment 
from ..nss.agents import Agent
from ..nss.engines import Engine
from ..nss.worlds import World
import numpy as np


def test_run():
    np.random.seed(0)

    engine = Engine.Engine()
    world = World.World(3,3)

    env = Enviroment.Enviroment((100,100), 100)
    env.foodValue = 50 
    env.setFood()

    agent_list = [Agent.Agent(env, 10) for i in range(0,100)]
    pre_agent_list_len = len(agent_list)

    agent_list = engine.run(agent_list, env, world)

    assert pre_agent_list_len != len(agent_list) and world.cycle-1 == world.totalCycles

