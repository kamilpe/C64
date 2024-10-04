import math
from ColorTools import find_closest

def apply_dithering(image, width, height, palette, dithering = True):
    info_step = height/16
    next_info_step = 0

    for y in range(0, height):
        for x in range(0, width):
            old = image[y, x]
            new = palette[find_closest(old, palette)]

            if (dithering):
                error = old - new
                if (x + 1 < width):
                    image[y, x + 1] += error * 0.4375 # right, 7 / 16
                if (y + 1 < height) and (x + 1 < width):
                    image[y + 1, x + 1] += error * 0.0625 # right, down, 1 / 16
                if (y + 1 < height):
                    image[y + 1, x] += error * 0.3125 # down, 5 / 16
                if (x - 1 >= 0) and (y + 1 < height): 
                    image[y + 1, x - 1] += error * 0.1875 # left, down, 3 / 16

            image[y,x] = new
        
        if ((y+1) >= next_info_step):
            next_info_step += info_step
            print(str(math.floor((y+1)*100/height)) + '%')

    return image
