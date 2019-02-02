"""XY conversion from angle/radii plot"""

# Imports
import math

def XYconvert(theta, radius):
    rad = theta*math.pi/180  # degs > rads
    x = radius*math.cos(rad)
    y = radius*math.sin(rad)
    return [x, y]
