import C64Palette
import numpy
import math
from ColorConversion import rgb_to_xyz, xyz_to_lab, lab_to_xyz, xyz_to_rgb
from PIL import Image

C64Palette.init_palettes()

def euclidean_distance(c1, c2):
    d1 = math.pow(c1[0]-c2[0], 2)
    d2 = math.pow(c1[1]-c2[1], 2)
    d3 = math.pow(c1[2]-c2[2], 2)
    return math.sqrt(d1+d2+d3)

def find_closest(color, palette):
    choosen_index = 0
    last_distance = euclidean_distance(color, palette[0])

    for i in range(1, len(palette)):
        distance = euclidean_distance(color, palette[i])
        if (distance < last_distance): 
            choosen_index = i
            last_distance = distance

    return choosen_index

img_input_file = "input.jpg"
img_output_file = "output.png"
print('Reading', img_input_file)
with Image.open(img_input_file) as pic:
    pic_array = numpy.array(pic)
    palette = C64Palette.LAB

    print('Creating color space...')
    pic_cs = numpy.empty((pic.height, pic.width, 3), dtype=numpy.float32)
    for y in  range(0, pic.height):
        for x in range(0, pic.width):
            pic_cs[y,x] = xyz_to_lab(rgb_to_xyz(pic_array[y,x]))

    print('Applying palette...')
    for y in  range(0, pic.height):
        for x in range(0, pic.width):
            pic_cs[y,x] = palette[find_closest(pic_cs[y,x], palette)]

    print('Converting to 32bit RGB')
    for y in  range(0, pic.height):
        for x in range(0, pic.width):
            pic_array[y,x] = xyz_to_rgb(lab_to_xyz(pic_cs[y,x]))

    print('Saving', img_output_file)
    Image.fromarray(pic_array).save(img_output_file)
    print('Done')
