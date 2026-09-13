import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
float_image = np.float32(image)

dft = cv2.dft(float_image, flags=cv2.DFT_COMPLEX_OUTPUT)
shifted = np.fft.fftshift(dft)

print("Original image shape:", image.shape)
print("DFT result shape:", dft.shape)
print("Shifted DFT shape:", shifted.shape)

magnitude = cv2.magnitude(shifted[:, :, 0], shifted[:, :, 1])
magnitude = np.log1p(magnitude)
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
cv2.imwrite("output.png", magnitude)
