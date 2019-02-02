"""Pathing Function: Radius varying by sinusoid of amplitude and frequency of 0.1 units and 5Hz.
Needs conversion from angle/radius state vector to XY vector"""

# Imports
import random
import math
rng = random.Random()

type = 1  # Information about conversion 1 = polar > cartesian
start = [0, 1, 1, 0.1, 5]  # State Vector Initial Conditions: Angle, Radius, Angular Velocity, Amp, Freq


def func(z):
    # Angle, Radius
    z[0] = z[0] + z[2]
    z[1] = 1 + z[3]*math.sin((z[0]*math.pi/180)*z[4])

    return z
