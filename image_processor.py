import os
import cv2
import numpy as np

def find_horizon(path, treshhold = cv2.THRESH_BINARY + cv2.THRESH_OTSU):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Изображение не найдено: {path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 0, 255, treshhold)

    horizon_y = np.zeros(thresh.shape[1], dtype=int)
    for x in range(thresh.shape[1]):
        for y in range(thresh.shape[0]):
            if thresh[y, x] > 0:
                horizon_y[x] = y
                break

    output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for x in range(len(horizon_y)):
        y = horizon_y[x]
        if y < thresh.shape[0]:
            for dy in [-1, 0, 1]:
                y_draw = y + dy
                if 0 <= y_draw < output.shape[0]:
                    output[y_draw, x] = [0, 255, 0]

    return img, thresh, horizon_y, output