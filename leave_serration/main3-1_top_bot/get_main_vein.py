# # from skimage.feature import hessian_matrix, hessian_matrix_eigvals
# # import cv2
# # from skimage import color
# # #assume you have an image img
# # img = '442_100_1.JPG'
# # img = cv2.imread(img)
# # #生成二值测试图像
# # img=color.rgb2gray(img)
# #
# # hxx, hxy, hyy = hessian_matrix(img, sigma=3)
# # i1, i2 = hessian_matrix_eigvals(hxx, hxy, hyy)
# # print(i1.shape)
# # #i2 is the variable you want.
# #
# # #Visualise the result
# import matplotlib.pyplot as plt
# # plt.imshow(i2)
# # plt.show()
# import cv2
# import numpy as np
#
# cups = cv2.imread('9.jpg')
#
# # preprocess by blurring and grayscale
# cups_preprocessed  = cv2.cvtColor(cv2.GaussianBlur(cups, (7,7), 0), cv2.COLOR_BGR2GRAY)
#
# # find binary image with thresholding
# _, cups_thresh = cv2.threshold(cups_preprocessed, 80, 255, cv2.THRESH_BINARY)
# plt.imshow(cv2.cvtColor(cups_thresh, cv2.COLOR_GRAY2RGB))
#
#
# # find binary image with edges
# cups_edges = cv2.Canny(cups_preprocessed, threshold1=90, threshold2=110)
# plt.imshow(cv2.cvtColor(cups_edges, cv2.COLOR_GRAY2RGB))
# cv2.imwrite('cups-edges.jpg', cups_edges)
#
# # copy of image to draw lines
# cups_lines = np.copy(cups)
#
# # find hough lines
# num_pix_threshold = 110 # minimum number of pixels that must be on a line
# lines = cv2.HoughLines(cups_edges, 1, np.pi/180, num_pix_threshold)
#
# for rho, theta in lines[0]:
#     # convert line equation into start and end points of line
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a * rho
#     y0 = b * rho
#
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))
#
#     cv2.line(cups_lines, (x1,y1), (x2,y2), (0,0,255), 1)
# plt.show()

import get_leave_boundary
import get_leave_serration

img = '20_39_2.jpg'
# get contours
contours = get_leave_boundary.get_leave_boundary(img)
print('叶片边界坐标: ', contours)

# get serration
ser4_idx, ser4_deepest_idx, serration_numbers, serration_depths, serration_widthes, \
    curvatures, total_curvature_mean = get_leave_serration.get_leave_serration(contours)

get_leave_serration.show_leave_serration(contours, ser4_idx, ser4_deepest_idx)














