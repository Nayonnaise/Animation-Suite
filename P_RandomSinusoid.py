"""Pathing Function: Radius varying by sinusoid of random amplitude and frequency. These values change when the sinusoid
 is around mean value. Needs conversion from angle/radius state vector to XY vector"""

# Imports
import random
import math
rng = random.Random()

type = 1  # Information about conversion 1 = polar > cartesian
start = [0, 0.1, 1, 0, 5]  # State Vector Initial Conditions: Angle, Radius, Angular Velocity, Amp, Freq


def func(z):

    if 0.995 < z[1] < 1.005:
        z[3] = rng.randrange(0, 50)/100
        z[4] = rng.randrange(1, 12)

    # Angle, Radius
    z[0] = z[0] + z[2]
    z[1] = 1 + z[3]*math.sin((z[0]*math.pi/180)*z[4])



    return z