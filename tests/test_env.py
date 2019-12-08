import numpy as np
from ..nss.enviroments.Enviroment import Enviroment as env

def test_setFood():
    np.random.seed(0)
    test_enviroment = env([2,2], 2)
    test_enviroment.setFood()
    assert test_enviroment.map == {(0,1) : 1,
                                   (1,0) : 1 }

def test_removeAllFood():
    np.random.seed(0)
    test_enviroment = env([2,2], 2)
    assert bool(test_enviroment.map) == False
