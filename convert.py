import C64Palette
import numpy
import math
from FloydSteinbergDithering import apply_dithering
from ColorTools import xyz_to_lab, rgb_to_xyz, xyz_to_rgb, lab_to_xyz
from PIL import Image

C64Palette.init_palettes()

img_input_file = "IMG_4323.jpeg"
img_output_file = "output.png"
print('Reading', img_input_file)
with Image.open(img_input_file) as pic:
    pic_array = numpy.array(pic)
    palette = C64Palette.LAB

    print('Creating color space...')
    pic_cs = numpy.empty((pic.height, pic.width, 3), dtype=numpy.float32)
    for y in  range(0, pic.height):
        for x in range(0, pic.width):
            if (palette == C64Palette.RGB):
                pic_cs[y,x] = pic_array[y,x]
            else:
                pic_cs[y,x] = xyz_to_lab(rgb_to_xyz(pic_array[y,x]))
            
    print('Applying dithering...')
    apply_dithering(pic_cs, pic.width, pic.height, palette, True)

    print('Converting color space to the 32bit RGB')
    for y in  range(0, pic.height):
        for x in range(0, pic.width):
            if (palette == C64Palette.RGB):
                pic_array[y,x] = pic_cs[y,x]
            else:
                pic_array[y,x] = xyz_to_rgb(lab_to_xyz(pic_cs[y,x]))

    print('Saving', img_output_file)
    Image.fromarray(pic_array).save(img_output_file)
    print('Done')
