import cv2
import numpy as np

# Load image
img = cv2.imread('logo_warrior.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Reshape image for clustering
pixel_values = img.reshape((-1, 3))
pixel_values = np.float32(pixel_values)

# Define criteria and apply KMeans
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
k = 3  # Number of clusters (background + warrior + shield details)
_, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

# Convert centers back to 8 bit values
centers = np.uint8(centers)
segmented_image = centers[labels.flatten()]
segmented_image = segmented_image.reshape(img.shape)

# Create mask for the background cluster
labels = labels.flatten()
background_label = np.argmax(np.bincount(labels))  # Most common cluster = background
mask = np.uint8((labels != background_label) * 255)
mask = mask.reshape((img.shape[0], img.shape[1]))

# Optional: Smooth mask
mask = cv2.medianBlur(mask, 5)

# Add alpha channel
b, g, r = cv2.split(img)
rgba = [b, g, r, mask]

final = cv2.merge(rgba)

# Save result
cv2.imwrite('log_transparent1.png', final)

print("Saved output_clean.png with much cleaner transparent background.")
