from ColorTools import *

RGB = [
    [0.0,   0.0,   0.0],
    [255.0, 255.0, 255.0],
    [136.0, 0.0,   0.0],
    [170.0, 255.0, 238.0],
    [204.0, 68.0,  204.0],
    [0.0,   204.0, 85.0],
    [0.0,   0.0,   170.0],
    [238.0, 238.0, 119.0],
    [221.0, 136.0, 85.0],
    [102.0, 68.0,  0.0],
    [255.0, 119.0, 119.0],
    [51.0,  51.0,  51.0],
    [119.0, 119.0, 119.0],
    [170.0, 255.0, 102.0],
    [0.0,   136.0, 255.0],
    [187.0, 187.0, 187.0]
]

XYZ = []
LAB = []

def init_palettes():
    for i in range(0,len(RGB)):
        xyz = rgb_to_xyz(RGB[i])
        lab = xyz_to_lab(xyz)
        XYZ.append(xyz)
        LAB.append(lab)
