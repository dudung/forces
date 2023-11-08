import numpy as np

def zero():
    return np.array([0, 0, 0])

def value(force):
    if isinstance(force, list):
        if len(force) == 3:
            return np.array(force)
        else:
            return np.array(force + [0])
    else:
        return np.array([force, 0, 0])
