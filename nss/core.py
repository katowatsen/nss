
import json
import numpy as np
from nss.worlds.World import World
from nss.engines.Engine import Engine
from nss.enviroments.Enviroment import Enviroment 
from nss.agents.Agent import Agent
from nss.util.Analysis import Analysis

def start():
    parms = getParameters()
    world = setWorld(parms)
    engine = setEngine()
    env = setEnv(parms)
    agent_list = setAgentList(parms, env, world)
    analysis = setAnalysis(parms)

    engine.run(agent_list, env, world, analysis)

def getParameters():
    with open("model_parameters.json", "r") as read_file:
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
    return [Agent(env, world, parms["agentMaxMass"], parms["agentMaxDev"], parms["agentReproduceCost"])\
            for i in range(0,parms["initalAgentAmount"])]

def setEngine():
    return Engine()

def setAnalysis(parms):
    return Analysis(parms["graph_varibles"])
