import cv2
import numpy as np

image = cv2.imread("input.jpg")

# Custom sharpening kernel: emphasizes the center and subtracts neighbours.
kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], dtype=np.float32)

result = cv2.filter2D(image, -1, kernel)
cv2.imwrite("output.png", result)
