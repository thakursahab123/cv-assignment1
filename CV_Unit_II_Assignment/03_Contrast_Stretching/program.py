import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
old_min, old_max = int(image.min()), int(image.max())
print("Minimum intensity:", old_min)
print("Maximum intensity:", old_max)

if old_max > old_min:
    result = ((image.astype(np.float32) - old_min) * 255.0 /
              (old_max - old_min)).clip(0, 255).astype(np.uint8)
else:
    result = image.copy()

cv2.imwrite("output.png", result)
