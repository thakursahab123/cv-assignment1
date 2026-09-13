import cv2
import numpy as np

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
shifted = np.fft.fftshift(dft)

crow, ccol = rows // 2, cols // 2
radius = min(rows, cols) // 10

mask = np.ones((rows, cols, 2), np.uint8)
y, x = np.ogrid[:rows, :cols]
circle = (x - ccol) ** 2 + (y - crow) ** 2 <= radius ** 2
mask[circle] = 0

filtered = shifted * mask
inverse_shift = np.fft.ifftshift(filtered)
result = cv2.idft(inverse_shift)
result = cv2.magnitude(result[:, :, 0], result[:, :, 1])
result = cv2.normalize(result, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

cv2.imwrite("output.png", result)
