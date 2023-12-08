from tree import RGBXmasTree
from time import sleep
import random
from colorzero import Color

tree = RGBXmasTree()
tree.brightness = 0.05

# curated collection of colours
def random_curated_color_run(colors):
    try:
        while True:
            tree_pixels = list(range(0,25))
            color_iter = colors.copy()
            for i in range(len(tree_pixels)):
                pixel = random.choice(tree_pixels)
                tree_pixels.remove(pixel)
                
                # select one curated color, remove it from the list
                if(len(color_iter)==0): color_iter = colors.copy()
                choice = random.choice(color_iter)
                tree[pixel].color = choice
                color_iter.remove(choice)

    except KeyboardInterrupt:
        tree.color = (0,0,0)
        tree.close()

colors = [Color('red'), Color('red'), Color('green'), Color('blue'), Color('yellow'), Color('yellow'), Color('purple'), Color('white')]
random_curated_color_run(colors=colors)