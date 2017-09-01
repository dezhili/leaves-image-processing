import cv2
import matplotlib.pyplot as plt
import get_leave_boundary
from get_leave_top_bottom import get_leave_top_bottom
from get_leave_top_bottom import search_points
import math


image = 'seg_0.jpg'

# image = '442_100_1.jpg'
img = cv2.imread(image, 0)
contours = get_leave_boundary.get_leave_boundary(image)


p1_t, p2_b, k1, k2 = get_leave_top_bottom(image, contours)


p3_c, p4_r, p5_l = search_points(p1_t, p2_b, k2, contours, search_heng=True)
p6_c, p7_r, p8_l = search_points(p1_t, p3_c, k2, contours, search_heng=True)
p9_c, p10_r, p11_l = search_points(p2_b, p3_c, k2, contours, search_heng=True)
p12_c, p13_t, p14_b = search_points(p5_l, p3_c, k1, contours, search_heng=False)
p15_c, p16_t, p17_b = search_points(p4_r, p3_c, k1, contours, search_heng=False)


# 计算长度 宽度
len_c = math.sqrt((p1_t[0]-p2_b[0])**2 + (p1_t[1]-p2_b[1])**2) / 118.11
len_l = math.sqrt((p13_t[0]-p14_b[0])**2 + (p13_t[1]-p14_b[1])**2) / 118.11
len_r = math.sqrt((p16_t[0]-p17_b[0])**2 + (p16_t[1]-p17_b[1])**2) / 118.11
wid_c = math.sqrt((p5_l[0]-p4_r[0])**2 + (p5_l[1]-p4_r[1])**2) / 118.11
wid_t = math.sqrt((p8_l[0]-p7_r[0])**2 + (p8_l[1]-p7_r[1])**2) / 118.11
wid_b = math.sqrt((p11_l[0]-p10_r[0])**2 + (p11_l[1]-p10_r[1])**2) / 118.11
print('中间的长度为:\t', len_c)
print('左边的长度为:\t', len_l)
print('右边的长度为:\t', len_r)
print('中间的宽度为:\t', wid_c)
print('上边的宽度为:\t', wid_t)
print('下边的宽度为:\t', wid_b)


# plot
fig, axes = plt.subplots(1, 2, figsize=(8, 8))
ax0, ax1 = axes.ravel()
ax0.imshow(img, plt.cm.gray)
ax0.set_title('original image')

rows, cols = img.shape
ax1.axis([0, rows, cols, 0])

ax1.plot(contours[:, 0], contours[:, 1], linewidth=2)
ax1.axis('image')
ax1.set_title('boundary and lines')
ax1.plot([p1_t[0], p2_b[0]], [p1_t[1], p2_b[1]], 'r-')
ax1.plot([p4_r[0], p5_l[0]], [p4_r[1], p5_l[1]], 'g-')
ax1.plot([p7_r[0], p8_l[0]], [p7_r[1], p8_l[1]], 'g-')
ax1.plot([p10_r[0], p11_l[0]], [p10_r[1], p11_l[1]], 'g-')
ax1.plot([p13_t[0], p14_b[0]], [p13_t[1], p14_b[1]], 'r-')
ax1.plot([p16_t[0], p17_b[0]], [p16_t[1], p17_b[1]], 'r-')

plt.show()