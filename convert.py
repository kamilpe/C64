import Palette
from ColorConversion import rgb_to_xyz, xyz_to_cielab, cielab_to_xyz, xyz_to_rgb

rgb = [128,15,100]
print ("rgb:",rgb)

xyz = rgb_to_xyz(rgb)
print ("xyz:",xyz)

lab = xyz_to_cielab(xyz)
print ("lab:", lab)

xyz = cielab_to_xyz(lab)
print ("backward xyz:", xyz)

rgb = xyz_to_rgb(xyz)
print("backward rgb", rgb)

