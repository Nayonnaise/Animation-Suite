"""Master Animation File. Combines a Pathing Function (P_) and an Animating Function (A_) to Create an Animation  """

# Imports
import pygame
import numpy as np
pygame.init()

# In Folder Imports
from P_RandomSinusoid import func, type, start  # Pathing Function - Creates the path for animation
from A_EndStabilize import Animate  # Animating Function - Tells the script how to animate the path
from ColourPicker import ColourPicker  # Chooses the colours for the animation from a selection of presets
from XYconversion import XYconvert  # A function to convert Polar plots to Cartesian, type 1 = Polar

# Initial Variable
resX = 1000  # Window resolution X and Y respectively
resY = 1000  # Animations scale off this value
path = np.array([0, 0])  # Starting path value - 'path' is the animated XY coordinates
z = start  # z is the internal path vector - differs from 'path'. Z used to calculate the next point
n = 3600  # number of points plotted

# Colour Selection
palette = ColourPicker()  # Selects the preset to be used
background = pygame.Color(palette[0])  # Background colour
colour = pygame.Color(palette[1])  # Path Colour

win = pygame.display.set_mode((resX, resY))  # Creates window
radius = int(resY/60)  # Determines the size of the points plotted - Scaled from the Y resolution

# Pathing and Animation Loop
i = 0  # Counter initialised
s = 3 # Speed constant 1-10 recommended
while i <= n:
        pygame.time.delay(10*s)
        z = func(z)  # Calculates next step
        # Uses Z to get XY coordinates of point
        if type == 1:
            [x, y] = XYconvert(z[0], z[1])
        else:
            [x, y] = [z[0], z[1]]

        path = np.vstack([path, [x, y]])  # Stores point in Array
        Animate(resX, resY, path, i, win, radius, colour, background)  # Animates next point
        i += 1  # Increases counter

        # Use of close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                i = n+1


# Quits on completion
pygame.quit()
