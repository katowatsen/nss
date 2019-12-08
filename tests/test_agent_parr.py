from ..nss.agents.Agent import Agent
from ..nss.enviroments.Enviroment import Enviroment
import time
import numpy as np


def test_time_agent_search():
     
    np.random.seed(0)

    env = Enviroment((1000,1000),100)
    env.setFood()
    agent = Agent(env,10)
    agent.position = [500,500]

    start1 = time.time()
    food1 = agent.search(env)
    end1 = time.time()

    start2 = time.time()
    food2 = agent.parr_search(env)
    end2 = time.time()

    dif1 = end1 - start1
    dif2 = end2 - start2


    assert dif2 < dif1 and food2[1] == food1[1] 



