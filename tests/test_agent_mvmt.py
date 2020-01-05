import numpy as np
import math
from ..nss.agents import Agent
from ..nss.enviroments import Enviroment
from ..nss.worlds.World import World 


def test_position():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((10,10),2)
    test_agent = Agent.Agent(env,world, 0)
    assert test_agent.position == [0.4236547993389047 *10,0.6458941130666561*10]

def test_eatFood():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((2,2),2)
    env.setFood()

    test_agent = Agent.Agent(env,world, 0)
    test_agent.position = [0,0]

    if env.foodAtPosition(test_agent.position):
        test_agent.eatFood(env)

    test_agent.position = [1,0]

    if env.foodAtPosition(test_agent.position):
        test_agent.eatFood(env)

    test_agent.position = [0,1]

    if env.foodAtPosition(test_agent.position):
        test_agent.eatFood(env)

    test_agent.position = [1,1]

    if env.foodAtPosition(test_agent.position):
        test_agent.eatFood(env)

    assert bool(env.map) == False

def test_search_square_far():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((3,3),0)
    env.map[(0, 0)] = 1

    t_agent = Agent.Agent(env,world, 0)
    t_agent.genome["search"] = 5 
    t_agent.position = [3,3]

    assert t_agent.search(env)[0] == (0,0)

def test_search_square_mid():
    world = World(10,10)

    np.random.seed(0)
    env = Enviroment.Enviroment((3,3),0)
    env.map[(2, 2)] = 1 

    t_agent = Agent.Agent(env,world, 0)
    t_agent.genome["search"] = 3 
    t_agent.position = (0,0)

    assert t_agent.search(env)[0] == (2,2)

def test_search_square_fail():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((3,3),0)
    env.map[(0,0)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["search"] = 0
    t_agent.position = (3,3)

    assert t_agent.search(env) == None 

def test_search_rect_far():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((5,3),0)
    env.map[(0,0)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["search"] = 6 
    t_agent.position = (5,3)

    assert t_agent.search(env)[0] == (0,0)

def test_search_rect_mid():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((5,3),0)
    env.map[(3,1)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["search"] = 6 
    t_agent.position = (5,3)

    assert t_agent.search(env)[0] == (3,1)

def test_search_rect_multi():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((10,5),0)
    env.map[(0,0)] = 1
    env.map[(5,4)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["search"] = 100
    t_agent.position = [5,3]

    assert t_agent.search(env)[0] == (5,4)


def test_search_rect_fail():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((5,3),0)
    env.map[(0,0)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["search"] = 0 
    t_agent.position = [5,3]

    assert t_agent.search(env) == None

def test_search_rect_far_big():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((1000,2000),0)
    env.map[(0,0)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["search"] = 5000
    t_agent.position = [900,1900]

    assert t_agent.search(env)[0] == (0,0)

def test_search_rect_on_big():
    world = World(10,10)
    np.random.seed(0)
    env = Enviroment.Enviroment((1000,2000),0)
    env.map[(0,0)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["search"] = 3000 
    t_agent.position = [0,0]

    assert t_agent.search(env)[0] == (0,0)

def test_travel_instant():
    world = World(10,10)
    env = Enviroment.Enviroment((100,100),0)
    env.map[(0,0)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["travel"] = 10000

    t_agent.travel(((0,0),10)) 
    assert t_agent.position == [0,0]
    
def test_travel_partial():
    world = World(10,10)
    env = Enviroment.Enviroment((100,100),0)
    env.map[(0,0)] = 1

    t_agent = Agent.Agent(env, world,0)
    t_agent.genome["travel"] = 50 
    t_agent.position = [100,100]

    t_agent.travel(((0,0),70.71))
    assert [int(t_agent.position[0]),int(t_agent.position[1])] == [64,64]

def test_travel_null():
    world = World(10,10)
    env = enviroment.enviroment((2,2),1)
    env.map[(0,0)] = 1

    t_agent = agent.agent(env, world,0)
    t_agent.position = [1,1]
    t_agent.genome["travel"] = 0

    t_agent.travel(((0,0),1))
    assert t_agent.position == [1,1]

def test_wander():
    world = World(10,10)
    env = Enviroment.Enviroment((10,10),0)

    t_agent = Agent.Agent(env, world, 0)
    t_agent.position = [0,0]
    t_agent.wander(env)

    assert t_agent.position != [0,0]


