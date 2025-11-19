import os

from image_processor import *
from plots import *

cd = os.getcwd()
path_image = os.path.join(cd, 'data', 'earth-1.png')

img, thresh, horizon_y, output = find_horizon(path_image)

visualize_horizon(img, thresh, horizon_y, output)