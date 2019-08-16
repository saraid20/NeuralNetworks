from math import e
import numpy as np

def al_n(voltage):
    if (np.isclose(voltage,10)):
        return 0.1
    dividend = 0.01 * (10 - voltage)
    divisor = e**((10-voltage)/10) - 1
    return dividend/divisor

def beta_n(voltage):
    return 0.125 * e**(voltage/80)
