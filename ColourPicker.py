# Imports
import random
rng = random.Random()

# Palette list - Hexadecimals for background and path respectively
style1 = ["#000000", "#ffffff"]
style2 = ["#ffdac9", "#f16f84"]
style3 = ['#ffecf5', '#ff86c2']
style4 = ['#44bdd5', '#c9eaf3']
palettes = [style1, style2, style3, style4]


# Uses RNG to decide on colours
def ColourPicker():
    num = rng.randrange(0, len(palettes))
    return palettes[num]


ColourPicker()