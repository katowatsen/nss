from ..nss.agents.Agent import Agent
from ..nss.enviroments.EnviromentDict import Enviroment as dEnv
from ..nss.enviroments.Enviroment import Enviroment as aEnv
import time
import numpy as np


def test_time_agent_search_dict():

    np.random.seed(0)

    dictEnv = dEnv((10000,10000), 1000)
    arrEnv = aEnv((10000, 10000), 1000)

    dictEnv.setFood()
    arrEnv.setFood()

    dictAgent = Agent(dictEnv, 0)
    dictAgent.position = [500, 5000]

    arrAgent = Agent(arrEnv, 0)
    dictAgent.position = [500, 5000]


    dictStart = time.time()
    dictFood = dictAgent.dictSearch(dictEnv)
    dictEnd = time.time()

    arrStart = time.time()
    arrFood = arrAgent.parr_search(arrEnv)
    arrEnd = time.time()

    dictTime = dictEnd - dictStart
    arrTime = arrEnd - arrStart

    assert dictTime < arrTime 

