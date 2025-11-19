import matplotlib.pyplot as plt
import cv2
import numpy as np

def visualize_horizon(img, thresh, horizon_y, output):
    plt.figure(figsize=(8, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.title("Original Image")

    plt.subplot(2, 2, 2)
    plt.imshow(thresh, cmap="gray")
    plt.axis("off")
    plt.title("After Thresholding")

    plt.subplot(2, 2, 3)
    plot_img = np.zeros_like(thresh)
    for x in range(len(horizon_y)):
        y = horizon_y[x]
        if y < plot_img.shape[0]:
            for dy in [-1, 0, 1]:
                y_draw = y + dy
                if 0 <= y_draw < plot_img.shape[0]:
                    plot_img[y_draw, x] = 255
    plt.imshow(plot_img, cmap="gray")
    plt.axis("off")
    plt.title("Detected Horizon")

    plt.subplot(2, 2, 4)
    plt.imshow(output)
    plt.axis("off")
    plt.title("Horizon Overlay")

    plt.tight_layout()
    plt.show()