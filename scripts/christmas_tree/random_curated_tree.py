from tree import RGBXmasTree
from time import sleep
import random
from colorzero import Color
import argparse

# pulling user-input variables from command line
# note that the default timeout = 10 and default username = 'plugcamera' for SSH connections
parser = argparse.ArgumentParser(description='RPi Christmas Tree script, argument = whether to print output')
parser.add_argument('-o', '--output', dest='output', action='store', type=bool, default=True, help='Print output?')

# ingesting user-input arguments
args = parser.parse_args()
output = args.output

# initialise the tree
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

                # print the color of each LED if output=True
                if (output):
                    print(f'{choice}LED{pixel}')

    except KeyboardInterrupt:
        tree.color = (0,0,0)
        tree.close()

colors = [Color('red'), 
            Color('green'), 
            Color('blue'), 
            Color('yellow'), 
            Color('orange'), 
            Color('purple')]

random_curated_color_run(colors=colors)