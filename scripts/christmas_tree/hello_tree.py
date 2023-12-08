from tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree()
tree.brightness = 0.05

colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

try:
    while True:
        for color in colors:
            tree.color = color
            sleep(1)
except KeyboardInterrupt:
    tree.color = (0,0,0)
    tree.close()