from ColorTools import find_closest

def apply_dithering(image, width, height, palette):
    for y in range(0, height):
        for x in range(0, width):
            image[y,x] = palette[find_closest(image[y,x], palette)]
            
    return image
