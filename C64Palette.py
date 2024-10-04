from ColorConversion import *

RGB = [
    [0.0 ,0,0],
    [255,255,255],
    [136,0,0],
    [170,255,238],
    [204,68,204],
    [0,204,85],
    [0,0,170],
    [238,238,119],
    [221,136,85],
    [102,68,0],
    [255,119,119],
    [51,51,51],
    [119,119,119],
    [170,255,102],
    [0,136,255],
    [187,187,187]
]

XYZ = []
LAB = []

def init_palettes():
    for i in range(0,len(RGB)):
        xyz = rgb_to_xyz(RGB[i])
        lab = xyz_to_cielab(xyz)
        XYZ.append(xyz)
        LAB.append(lab)
