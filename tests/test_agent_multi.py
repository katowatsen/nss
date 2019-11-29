from ..nss.enviroments.Enviroment import Enviroment
from ..nss.agents.Agent import Agent
import numpy as np

def test_reproduce():
    env = Enviroment((5,5),2)
    agent_list = [Agent(env, 2) for i in range(0,1)]
    agent_list[0].curEnergy = 10
    agent_list[0].reqEnergy = 2
    agent_list[0].reproduce(agent_list, 2, env, 2, 0.01)

    assert (agent_list[0].curEnergy == agent_list[0].reqEnergy) == (len(agent_list) == 5)

def test_mutateChild():
    env = Enviroment((5,5),2)
    np.random.seed(0)
    t_agent = Agent(env, 2)

    assert t_agent.genome != t_agent.mutateChild(t_agent, 0.1) 
