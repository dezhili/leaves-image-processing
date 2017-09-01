import cv2
import matplotlib.pyplot as plt

image = 'seg_0.jpg'

img = cv2.imread(image, 0)

img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 50, 90, apertureSize=3)

# plot
fig, axes = plt.subplots(1, 2, figsize=(8, 8))
ax0, ax1 = axes.ravel()
ax0.imshow(img, plt.cm.gray)
ax0.set_title('original image')

rows, cols = img.shape
ax1.axis([0, rows, cols, 0])

ax1.imshow(edges, cmap='gray')
ax1.axis('image')
ax1.set_title('image_after_canny')

plt.show()