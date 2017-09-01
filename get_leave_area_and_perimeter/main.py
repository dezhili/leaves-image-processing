import get_leave_area
import get_leave_perimeter
import get_leave_serration

# image = 'seg_0.jpg'
# area = get_leave_area.get_leave_areas(image)
# print('area:', area)
#
# perimeter = get_leave_perimeter.get_leave_perimeter(image)
# print('perimeter:', perimeter)

import get_leave_serration
import get_leave_boundary
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage

img = 'seg_0.jpg'
# img = cv2.imread(img)
# GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, threshed_img = cv2.threshold(GrayImage, 160, 255,cv2.THRESH_BINARY)
# image, contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)
# print(len(contours[0]))
# small_areas = [i for i in contours if cv2.contourArea(i) < 200]
# for i in small_areas:
#     print(cv2.contourArea(i))

# img = cv2.imread(img)
# GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# ret, threshed_img = cv2.threshold(GrayImage, 150, 255,cv2.THRESH_BINARY)
# image, contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))
# print(contours)
# contours = [contours[i] for i in range(len(contours)) if len(contours[i]) > 100]
# contours = np.array(contours)
# contours = np.squeeze(contours)
# # for i in range(len(contours)):
# #     contours[i, 0], contours[i, 1] = contours[i, 1], contours[i, 0]
# # small_areas = [i for i in contours if cv2.contourArea(i) < 200]
# # cv2.fillPoly(threshed_img, small_areas, 255)
#
# print(contours.shape)
# print(contours)
# # print(cv2.contourArea(contours[0]) / (96*96))
# # print(cv2.contourArea(contours[1]) / (96*96))

# print(get_leave_area.get_leave_areas(img))
contours = get_leave_boundary.get_leave_boundary(img)
contours = np.ceil(contours)
print(contours)
contours = contours.astype(int)
props = skimage.measure.regionprops(contours)
print(props[0].area)

# #绘制轮廓
# fig, axes = plt.subplots(1,2,figsize=(8,8))
# ax0, ax1= axes.ravel()
# ax0.imshow(img,plt.cm.gray)
# ax0.set_title('original image')
#
# rows,cols=GrayImage.shape
# ax1.axis([0,rows,cols,0])
# ax1.plot(contours[:,0], contours[:,1], linewidth=2)
# ax1.axis('image')
# ax1.set_title('contours')
# plt.show()

