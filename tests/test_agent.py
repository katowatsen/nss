import numpy as np
import math
from ..nss.agents import Agent
from ..nss.enviroments import Enviroment

np.random.seed(0)

def test_position():
    env = Enviroment.Enviroment((10,10),2)
    test_agent = Agent.Agent(env, 10)
    assert test_agent.position == (0.4236547993389047 *10,0.6458941130666561*10)
