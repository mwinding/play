from tree import RGBXmasTree
from time import sleep
import argparse

# default values
max_light = 10
sleep_time = 0

# pulling user-input variables from command line
parser = argparse.ArgumentParser(description='RPi Christmas Tree script')
parser.add_argument('-m', '--max-light', dest='max_light', action='store', type=int, default=max_light, help='maximum light')
parser.add_argument('-s', '--sleep-time', dest='sleep_time', action='store', type=float, default=sleep_time, help='sleep time between light intervals')

# ingesting user-input arguments
args = parser.parse_args()
max_light = args.max_light
sleep_time = args.sleep_time

colors = [(1, 0, 0), (0, 1, 0), (1, 0.8, 0), (0, 0, 1), (1, 0, 1)]

# initialise the tree
tree = RGBXmasTree()
tree.brightness = max_light/100
tree.color = (0,0,0)

while True:
    for color in colors:
        for pixel in tree:
            pixel.color = color
            sleep(sleep_time)
