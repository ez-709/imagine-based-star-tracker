import os
import cv2
import numpy as np

def find_horizon(path, threshold=cv2.THRESH_BINARY + cv2.THRESH_OTSU, denoise=True):
    img = cv2.imread(path)
    if img is None:
        raise FileNotFoundError(f"Изображение не найдено: {path}")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 🔹 Добавляем медианное сглаживание для удаления звёзд (единичных точек)
    if denoise:
        gray = cv2.medianBlur(gray, ksize=3)  # ksize=3 — достаточно для звёзд, не смажет горизонт

    _, thresh = cv2.threshold(gray, 0, 255, threshold)

    horizon_points = []
    for x in range(thresh.shape[1]):
        for y in range(thresh.shape[0]):
            if thresh[y, x] > 0:
                horizon_points.append([x, y])
                break

    horizon_points = np.array(horizon_points)

    output = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for point in horizon_points:
        x, y = point
        for dy in [-1, 0, 1]:
            y_draw = y + dy
            if 0 <= y_draw < output.shape[0] and 0 <= x < output.shape[1]:
                output[y_draw, x] = [0, 255, 0]

    return img, thresh, horizon_points, output