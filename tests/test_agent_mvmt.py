import numpy as np
import math
from ..nss.agents import Agent
from ..nss.enviroments import Enviroment


def test_position():
    np.random.seed(0)
    env = Enviroment.Enviroment((10,10),2)
    test_agent = Agent.Agent(env, 0)
    assert test_agent.position == [0.4236547993389047 *10,0.6458941130666561*10]

def test_eatFood():
    np.random.seed(0)
    env = Enviroment.Enviroment((2,2),2)
    test_agent = Agent.Agent(env, 0)
    test_agent.position = [0,0]

    if env.foodAtAgent(test_agent):
        test_agent.eatFood()
    else:
        test_agent.position = [1,0]

        if env.foodAtAgent(test_agent):
            test_agent.eatFood()
        else:
            test_agent.position = [0,1]

            if env.foodAtAgent(test_agent):
                test_agent.eatFood()
            else:
                test_agent.position = [1,1]

                if env.foodAtAgent(test_agent):
                    test_agent.eatFood()

    assert np.array_equal(env.map, np.array([[0,0],[0,0]]))

def test_search_square_far():
    np.random.seed(0)
    env = Enviroment.Enviroment((3,3),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 5 
    t_agent.position = (3,3)

    assert t_agent.parr_search(env)[0] == (0,0)

def test_search_square_mid():
    np.random.seed(0)
    env = Enviroment.Enviroment((3,3),1)
    env.map[2][2] = 1 

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 3 
    t_agent.position = (0,0)

    assert t_agent.parr_search(env)[0] == (2,2)

def test_search_square_fail():
    np.random.seed(0)
    env = Enviroment.Enviroment((3,3),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 0
    t_agent.position = (3,3)

    assert t_agent.parr_search(env) == None 

def test_search_rect_far():
    np.random.seed(0)
    env = Enviroment.Enviroment((5,3),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 6 
    t_agent.position = (5,3)

    assert t_agent.parr_search(env)[0] == (0,0)

def test_search_rect_mid():
    np.random.seed(0)
    env = Enviroment.Enviroment((5,3),1)
    env.map[3][1] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 6 
    t_agent.position = (5,3)

    assert t_agent.parr_search(env)[0] == (3,1)

def test_search_rect_multi():
    np.random.seed(0)
    env = Enviroment.Enviroment((10,5),1)
    env.map[0][0] = 1
    env.map[5][4] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 100
    t_agent.position = (5,3)

    assert t_agent.parr_search(env)[0] == (5,4)


def test_search_rect_fail():
    np.random.seed(0)
    env = Enviroment.Enviroment((5,3),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 0 
    t_agent.position = (5,3)

    assert t_agent.parr_search(env) == None

def test_search_rect_far_big():
    np.random.seed(0)
    env = Enviroment.Enviroment((1000,2000),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 5000
    t_agent.position = (900,1900)

    assert t_agent.parr_search(env)[0] == (0,0)

def test_search_rect_on_big():
    np.random.seed(0)
    env = Enviroment.Enviroment((1000,2000),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["search"] = 3000 
    t_agent.position = (0,0)

    assert t_agent.parr_search(env)[0] == (0,0)

def test_travel_instant():
    env = Enviroment.Enviroment((100,100),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["travel"] = 10000

    t_agent.travel(env, ([0,0],50))
    assert t_agent.position == [0,0]
    
def test_travel_partial():
    env = Enviroment.Enviroment((100,100),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.genome["travel"] = 50 
    t_agent.position = [100,100]

    t_agent.travel(env, ([0,0],70.71))
    assert [int(t_agent.position[0]),int(t_agent.position[1])] == [64,64]

def test_travel_null():
    env = Enviroment.Enviroment((2,2),1)
    env.map[0][0] = 1

    t_agent = Agent.Agent(env, 0)
    t_agent.position = [1,1]
    t_agent.genome["travel"] = 0

    t_agent.travel(env, ([0,0],2))
    assert t_agent.position == [1,1]
