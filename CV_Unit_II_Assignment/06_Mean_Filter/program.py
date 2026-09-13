import cv2

image = cv2.imread("input.jpg")
# Tested with 3x3 and 7x7; the larger 7x7 kernel is used for final output.
result = cv2.blur(image, (7, 7))

cv2.imwrite("output.png", result)
