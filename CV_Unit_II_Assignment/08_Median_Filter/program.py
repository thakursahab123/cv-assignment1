import cv2

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
result = cv2.medianBlur(image, 5)

cv2.imwrite("output.png", result)
