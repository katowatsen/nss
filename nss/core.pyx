
import json
import numpy as np
from worlds.World import World
from engines.Engine import Engine
from enviroments.Enviroment import Enviroment 
from agents.Agent import Agent

def start():
    parms = getParameters()
    world = setWorld(parms)
    engine = setEngine()
    env = setEnv(parms)
    print(env.foodValue)
    agent_list = setAgentList(parms, env, world)

    engine.run(agent_list, env, world)

def getParameters():
    with open("../model_parameters.json", "r") as read_file:
            parms = json.load(read_file)

    return parms

def setWorld(parms):
    return World(parms["worldCycles"],
                 parms["worldTicks"])

def setEnv(parms):
    return Enviroment(parms["envDim"],
           parms["foodPerCycle"],
           parms["foodValue"])

def setAgentList(parms, env, world):
    return [Agent(env, world, parms["agentMaxMass"])\
            for i in range(0,parms["initalAgentAmount"])]

def setEngine():
    return Engine()
