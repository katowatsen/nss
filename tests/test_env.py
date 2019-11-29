import numpy as np
from ..nss.enviroments.Enviroment import Enviroment as env

def test_setFood():
    np.random.seed(0)
    test_enviroment = env([2,2], 2)
    test_enviroment.setFood()
    assert np.array_equal(test_enviroment.map,  np.array([[0,1],[1,0]]))

def test_removeAllFood():
    np.random.seed(0)
    test_enviroment = env([2,2], 2)
    assert np.array_equal(test_enviroment.map,  np.array([[0,0],[0,0]]))
