import numpy as np

def fit_circle(data_points: np.array):
    x = data_points[:, 0]
    y = data_points[:, 1]

    X = np.column_stack([x, y, np.ones_like(x)])
    Y = -(x**2 + y**2)
    Z = np.linalg.inv(X.T @ X) @ X.T @ Y

    a, b, c = Z[0], Z[1], Z[2]
    cx = -a / 2
    cy = -b / 2
    r = np.sqrt(cx**2 + cy**2 - c)

    return cx, cy, r
 

