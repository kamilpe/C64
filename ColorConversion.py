import math

# Reference: 2° Daylight, sRGB, Adobe-RGB
# Source: http://www.easyrgb.com/en/math.php
REFERENCE_X = 95.047
REFERENCE_Y = 100.0
REFERENCE_Z = 108.883

def rgb_to_xyz(rgb=[]):
    r = rgb[0] / 255
    g = rgb[1] / 255
    b = rgb[2] / 255

    if (r > 0.04045): r = math.pow(((r+0.055) / 1.055), 2.4)
    else:             r = r / 12.92
    if (g > 0.04045): g = math.pow(((g+0.055) / 1.055), 2.4)
    else:             g = g / 12.92
    if (b > 0.04045): b = math.pow(((b+0.055) / 1.055), 2.4)
    else:             b = b / 12.92

    r = r * 100
    g = g * 100
    b = b * 100

    x = r * 0.4124 + g * 0.3576 + b * 0.1805
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    z = r * 0.0193 + g * 0.1192 + b * 0.9505
    return [x,y,z]

def xyz_to_lab(xyz=[]):    
    x = xyz[0] / REFERENCE_X
    y = xyz[1] / REFERENCE_Y
    z = xyz[2] / REFERENCE_Z

    if (x > 0.008856): x = math.pow(x, (1/3))
    else:              x = (7.787 * x) + (16 / 116)
    if (y > 0.008856): y = math.pow(y, (1/3))
    else:              y = (7.787 * y) + (16 / 116)
    if (z > 0.008856): z = math.pow(z, (1/3))
    else:              z = ( 7.787 * z) + (16 / 116)

    l = ( 116 * y) - 16
    a = 500 * (x - y)
    b = 200 * (y - z)
    return [l,a,b]

def lab_to_xyz(lab=[]):
    l = lab[0]
    a = lab[1]
    b = lab[2]

    y = (l + 16 ) / 116
    x = a / 500 + y
    z = y - b / 200

    if (math.pow(y, 3) > 0.008856): y = math.pow(y, 3)
    else:                           y = (y - 16 / 116) / 7.787
    if (math.pow(x, 3) > 0.008856): x = math.pow(x, 3)
    else:                           x = (x - 16 / 116) / 7.787
    if (math.pow(z, 3) > 0.008856): z = math.pow(z, 3)
    else:                           z = (z - 16 / 116) / 7.787

    x = x * REFERENCE_X
    y = y * REFERENCE_Y
    z = z * REFERENCE_Z
    return [x,y,z]

def xyz_to_rgb(xyz=[]):
    x = xyz[0] / 100
    y = xyz[1] / 100
    z = xyz[2] / 100

    r = x *  3.2406 + y * -1.5372 + z * -0.4986
    g = x * -0.9689 + y *  1.8758 + z *  0.0415
    b = x *  0.0557 + y * -0.2040 + z *  1.0570

    if (r > 0.0031308):  r = 1.055 * math.pow(r, (1 / 2.4)) - 0.055
    else:                r = 12.92 * r
    if (g > 0.0031308 ): g = 1.055 * math.pow(g, (1 / 2.4)) - 0.055
    else:                g = 12.92 * g
    if (b > 0.0031308 ): b = 1.055 * math.pow(b, (1 / 2.4)) - 0.055
    else:                b = 12.92 * b

    r = math.floor(r * 255)
    g = math.floor(g * 255)
    b = math.floor(b * 255)
    return [r,g,b]
