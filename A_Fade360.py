"""Animation Function: Plots the last 360 points with fade around the origin"""

# Imports
import pygame


def Animate(resX, resY, path, i, win ,radius, colour, background):
    win.fill(background)
    n = 360  # Tail length

    if i < n:  # When len(path) is less than the value of n
        for k in range(i):
            # Determines the colour of the point based on the position in the path vector
            r = int((colour[0] - background[0]) * (k / i) + background[0])
            g = int((colour[1] - background[1]) * (k / i) + background[1])
            b = int((colour[2] - background[2]) * (k / i) + background[2])

            # Draws the Point
            pygame.draw.circle(win, (r, g, b), [int((resX / 2) + (resY / 4 * path[k, 0])), int((resY / 2) + (resY / 4 * path[k, 1]))], radius)
    else:
        for k in range(n):
            r = int((colour[0] - background[0]) * (k / n) + background[0])
            g = int((colour[1] - background[1]) * (k / n) + background[1])
            b = int((colour[2] - background[2]) * (k / n) + background[2])
            pygame.draw.circle(win, (r, g, b), [int((resX / 2) + (resY / 4 * path[i-(n-k), 0])), int((resY / 2) + (resY / 4 * path[i-(n-k), 1]))], radius)

    pygame.display.update()