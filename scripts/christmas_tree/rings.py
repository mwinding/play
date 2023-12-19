
from tree import RGBXmasTree
from time import sleep
import argparse

# default values
max_light = 10

# pulling user-input variables from command line
parser = argparse.ArgumentParser(description='RPi Christmas Tree script')
parser.add_argument('-m', '--max-light', dest='max_light', action='store', type=int, default=20, help='maximum light')

# ingesting user-input arguments
args = parser.parse_args()
max_light = args.max_light

def pixel_brightness(reduction, original_color):

    adjusted_color = (int(max(original_color[0] - reduction, 0)),
                        int(max(original_color[1] - reduction, 0)),
                        int(max(original_color[2] - reduction, 0)))
    
    return(adjusted_color)

colors = [(1, 0, 0), (0, 1, 0), (1, 0.8, 0), (0, 0, 1), (1, 0, 1)]

# initialise the tree
tree = RGBXmasTree()
tree.brightness = max_light/100
tree.color = (0,0,0)

try:
    
    while True:
        for color in colors:
            for i in range(0,28):

                if i<25:
                    tree[i].color = color

                if i>2:
                    #for j in range(0, i):
                        #reduction = 255*0.2
                        #tree[j].color = pixel_brightness(reduction, tree[j].color)

                    if((i-1)<25):
                        tree[i-1].color = (color[0]*0.5, color[1]*0.5, color[2]*0.5)
                    if((i-2)<25):
                        tree[i-2].color = (color[0]*0.1, color[1]*0.1, color[2]*0.1)
                    if((i-3)<25):
                        tree[i-3].color = (0,0,0)

    '''
    while True:
        for color in colors:
            for pixel in tree:
                pixel.color = color
    '''
except KeyboardInterrupt:
    tree.color = (0,0,0)
    tree.close()

