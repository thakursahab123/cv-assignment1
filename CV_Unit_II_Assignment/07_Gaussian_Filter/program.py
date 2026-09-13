import cv2

image = cv2.imread("input.jpg")
# 5x5 is an odd-sized kernel and gives balanced Gaussian smoothing.
result = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imwrite("output.png", result)
