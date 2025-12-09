import os
import numpy as np

from image_processor import *
from plots import *
from math_fitten import fit_circle

cd = os.getcwd()
path_image = os.path.join(cd, 'data', 'earth-8.jpg')

img, thresh, horizon, output = find_horizon(path_image)
fitted_circle = fit_circle(horizon)

visualize_horizon(img, thresh, horizon, output, circle_params=fitted_circle)
