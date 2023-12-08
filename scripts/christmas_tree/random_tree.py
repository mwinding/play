from tree import RGBXmasTree
from time import sleep
import random
from colorzero import Color

tree = RGBXmasTree()
tree.brightness = 0.05

# defined between [0,100], converted to [0,1]
# trying to convert yrb to rgb?
def random_color(min):
    first = random.randint(min, 100)
    second = random.randint(0, 100 - first)
    third = 100 - first - second
    rand_nums = [first/100, second/100, third/100]

    y = random.choice(rand_nums)
    rand_nums.remove(y)

    r = random.choice(rand_nums)
    rand_nums.remove(r)

    b = random.choice(rand_nums)

    g = y - r
    if(g<0): g=0

    print(f'[y,r,b] = {y},{r},{b}; [r,g,b] = {r},{g},{b}')

    return (r, g, b)

def random_color_run(min_init):
    try:
        while True:
            tree_pixels = list(range(0,25))
            for i in range(len(tree_pixels)):
                pixel = random.choice(tree_pixels)
                tree_pixels.remove(pixel)

                tree[pixel].color = random_color(min=min_init)

    except KeyboardInterrupt:
        tree.color = (0,0,0)
        tree.close()

random_color_run(min_init=75)