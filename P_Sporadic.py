"""Pathing Function: Random XY path"""

# Imports
import random
rng = random.Random()

type = 0  # Information about conversion 1 = polar > cartesian
start = [0, 0, 0.01, 0, 0, 0]  # State Vector Initial Conditions, XY displacements, velocities, and accelerations


def func(z):
    # Displacement and Amplitude
    z[0] = z[0] + z[2]
    z[1] = z[1] + z[3]

    # Velocities: Displacement and Amplitude
    z[2] = rng.randrange(-1, 2)/10
    z[3] = rng.randrange(-1, 2)/10

    # Acceleration: Displacement and Amplitude
    z[4] = 0
    z[5] = 0

    return z