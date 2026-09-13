import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([image], [0], None, [256], [0, 256]).ravel()
peak = int(np.argmax(hist))
print("Intensity with highest frequency:", peak)

plt.figure(figsize=(8, 5))
plt.plot(hist)
plt.title("Intensity Histogram")
plt.xlabel("Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])
plt.savefig("output.png", bbox_inches="tight")
plt.close()
