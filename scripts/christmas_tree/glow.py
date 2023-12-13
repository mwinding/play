from tree import RGBXmasTree
from time import sleep
import argparse

# default values
max_light = 20
min_light = 0
interval = 2
sleep_time = 0.05

# pulling user-input variables from command line
# note that the default timeout = 10 and default username = 'plugcamera' for SSH connections
parser = argparse.ArgumentParser(description='RPi Christmas Tree script')
parser.add_argument('-m', '--max-light', dest='max_light', action='store', type=int, default=20, help='maximum light')
parser.add_argument('-l', '--min-light', dest='min_light', action='store', type=int, default=0, help='minimal light')
parser.add_argument('-i', '--interval-light', dest='interval', action='store', type=int, default=2, help='range interval')
parser.add_argument('-s', '--sleep-time', dest='sleep_time', action='store', type=float, default=2, help='sleep time between light intervals')

# ingesting user-input arguments
args = parser.parse_args()
max_light = args.max_light
min_light = args.min_light
interval = args.interval
sleep_time = args.sleep_time

# initialise the tree
tree = RGBXmasTree()
tree.brightness = 0.05

colors = [(1, 0, 0), (0, 1, 0), (1, 0.8, 0), (0, 0, 1), (1, 0, 1)]

def glow(tree, max_light, min_light, interval, sleep_time):
    light_ascending = list(range(0, max_light, interval))
    light_descending = list(range(max_light, 0, -interval))

    light_ranges = light_ascending + light_descending
    light_ranges = [x/100 for x in light_ranges]

    for light in light_ranges:
        sleep(sleep_time)
        tree.brightness=light

try:
    while True:
        for color in colors:
            tree.color = color
            glow(tree, max_light, min_light, interval)
except KeyboardInterrupt:
    tree.color = (0,0,0)
    tree.close()

