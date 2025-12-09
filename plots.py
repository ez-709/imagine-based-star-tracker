import matplotlib.pyplot as plt
import cv2
import numpy as np

def visualize_horizon(img, thresh, horizon_points, output, circle_params=None):
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Оригинальное изображение")

    overlay = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).copy()
    angle = 0.0

    if circle_params is not None:
        cx, cy, r = circle_params
        h, w = img.shape[:2]

        def y(x):
            dx = cx - x
            disc = r**2 - dx**2
            if disc < 0:
                return cy 
            return cy - np.sqrt(disc)

        y1 = y(0)
        y2 = y(w - 1)

        angle = np.degrees(np.arctan2(y2 - y1, w - 1 - 0))

        def draw_thick_circle(canvas, cx, cy, r, color, thickness=3):
            theta = np.linspace(0, 2 * np.pi, 2000)
            x_circ = cx + r * np.cos(theta)
            y_circ = cy + r * np.sin(theta)
            for i in range(len(theta)):
                x = int(round(x_circ[i]))
                y = int(round(y_circ[i]))
                for dx in range(-thickness//2, thickness//2 + 1):
                    for dy in range(-thickness//2, thickness//2 + 1):
                        x_t = x + dx
                        y_t = y + dy
                        if 0 <= y_t < canvas.shape[0] and 0 <= x_t < canvas.shape[1]:
                            if canvas.ndim == 2:
                                canvas[y_t, x_t] = color
                            else:
                                canvas[y_t, x_t] = color

        draw_thick_circle(overlay, cx, cy, r, color=[0, 255, 0], thickness=3)

    plt.subplot(1, 2, 2)
    plt.imshow(overlay)
    plt.axis("off")
    plt.title(f"Аппроксимированная окружность\nУгол крена: {angle:.2f}")

    plt.tight_layout()
    plt.show()