import cv2
import numpy as np

image = cv2.imread("input.jpg")
brightness = 60

# Convert to a wider type so pixel values can be safely clipped.
result = np.clip(image.astype(np.int16) + brightness, 0, 255).astype(np.uint8)

y, x = 100, 100
print("Pixel before:", image[y, x])
print("Pixel after :", result[y, x])

cv2.imwrite("output.png", result)
