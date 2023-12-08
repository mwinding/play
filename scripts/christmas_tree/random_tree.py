from tree import RGBXmasTree
from time import sleep
import random

tree = RGBXmasTree()
tree.brightness = 0.05

def random_color(max_intensity):
    first = random.randint(0, max_intensity)
    second = random.randint(0, max_intensity - first)
    third = max_intensity - first - second
    rand_nums = [first, second, third]

    r = random.choice(rand_nums)
    rand_nums.remove(r)

    g = random.choice(rand_nums)
    rand_nums.remove(g)

    b = random.choice(rand_nums)
    print([r,g,b])

    return (r, g, b)

max_intensity = 255

try:
    while True:
        pixel = random.choice(tree)
        pixel.color = random_color(max_intensity=max_intensity)

except KeyboardInterrupt:
    tree.color = (0,0,0)
    tree.close()