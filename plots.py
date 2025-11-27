import matplotlib.pyplot as plt
import cv2
import numpy as np

def visualize_horizon(img, thresh, horizon_points, output, circle_params=None):
    """
    Визуализирует обработку изображения.
    На 3 и 4 графиках — ТОЛЬКО аппроксимированная окружность, нарисованная толстой зелёной линией.
    
    circle_params — кортеж (cx, cy, r)
    """
    plt.figure(figsize=(10, 10))

    # 1. Оригинал
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Original Image")

    # 2. Бинаризация
    plt.subplot(2, 2, 2)
    plt.imshow(thresh, cmap="gray")
    plt.axis("off")
    plt.title("After Thresholding")

    # Вспомогательная функция для рисования толстой линии
    def draw_thick_circle(canvas, cx, cy, r, color, thickness=3):
        theta = np.linspace(0, 2 * np.pi, 500)
        x_circ = cx + r * np.cos(theta)
        y_circ = cy + r * np.sin(theta)
        for i in range(len(theta)):
            x = int(round(x_circ[i]))
            y = int(round(y_circ[i]))
            # Рисуем квадратик толщиной thickness вокруг точки
            for dx in range(-thickness//2, thickness//2 + 1):
                for dy in range(-thickness//2, thickness//2 + 1):
                    x_t = x + dx
                    y_t = y + dy
                    if 0 <= y_t < canvas.shape[0] and 0 <= x_t < canvas.shape[1]:
                        if canvas.ndim == 2:  # grayscale
                            canvas[y_t, x_t] = color
                        else:  # RGB
                            canvas[y_t, x_t] = color

    # 3. Только окружность на чёрном фоне (зелёная, толстая)
    plt.subplot(2, 2, 3)
    blank = np.zeros_like(thresh)
    if circle_params is not None:
        cx, cy, r = circle_params
        draw_thick_circle(blank, cx, cy, r, color=255, thickness=3)  # белый = 255 в grayscale
    plt.imshow(blank, cmap="gray")
    plt.axis("off")
    plt.title("Fitted Circle Only")

    # 4. Оригинал + толстая зелёная окружность
    plt.subplot(2, 2, 4)
    overlay = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).copy()
    if circle_params is not None:
        cx, cy, r = circle_params
        draw_thick_circle(overlay, cx, cy, r, color=[0, 255, 0], thickness=3)  # зелёный в RGB
    plt.imshow(overlay)
    plt.axis("off")
    plt.title("Original + Fitted Circle")

    plt.tight_layout()
    plt.show()