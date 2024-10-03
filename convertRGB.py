import Palette
import numpy
import math
from ColorConversion import rgb_to_xyz, xyz_to_cielab, cielab_to_xyz, xyz_to_rgb
from PIL import Image


def euclidean_distance(c1, c2):
    d1 = math.pow(c1[0]-c2[0], 2)
    d2 = math.pow(c1[1]-c2[1], 2)
    d3 = math.pow(c1[2]-c2[2], 2)
    return math.sqrt(d1+d2+d3)

def find_closest(rgb):
    color1 = rgb
    choosen = 0
    last_distance = euclidean_distance(color1, Palette.C64[choosen])

    for i in range(1, len(Palette.C64)):
        current_cielab = Palette.C64[i]
        current_distance = euclidean_distance(color1, current_cielab)
        if (current_distance < last_distance): 
            choosen = i
            last_distance = current_distance

    return Palette.C64[choosen]


with Image.open("input.jpg") as pic:
    pic = Image.open("input.jpg")
    pic_array = numpy.array(pic)#

    for y in  range(0, pic.height):
        for x in range(0, pic.width):
            pic_array[y,x] = find_closest(pic_array[y,x])

    Image.fromarray(pic_array).save("output.png")
