import cv2

image = cv2.imread("input.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Original image shape:", image.shape)
print("Grayscale image shape:", gray.shape)
print("Height:", gray.shape[0])
print("Width:", gray.shape[1])

cv2.imwrite("output.png", gray)
