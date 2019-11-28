from ..nss.enviroments.Enviroment import Enviroment as env
import numpy as np

def test_setFood():
    test_enviroment = env([2,2], 2)
    test_enviroment.setFood()
    assert np.array_equal(test_enviroment.env,  np.array([[0,1],[1,0]]))

def test_removeAllFood():
    test_enviroment = env([2,2], 2)
    assert np.array_equal(test_enviroment.env,  np.array([[0,0],[0,0]]))

