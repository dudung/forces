import numpy as np

def gravity(m, g):
    return m * g

def electric(q, E):
    return q * E

def drag(b, v):
    return -b*v
