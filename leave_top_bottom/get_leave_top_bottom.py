import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
import get_leave_boundary

image = '9.jpg'
contours = get_leave_boundary.get_leave_boundary(image)

img = cv2.imread(image, 0)

img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 50, 150, apertureSize=3)

lines = cv2.HoughLines(edges, 1, np.pi / 180, 118)  # 这里对最后一个参数使用了经验型的值
print(lines)
# print(len(lines))
result = img.copy()
for line in lines[0]:
    rho = line[0]  # 第一个元素是距离rho
    theta = line[1]  # 第二个元素是角度theta
    print(rho)
    print(theta)
    if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):  # 垂直直线
        # 该直线与第一行的交点
        pt1 = (int(rho / np.cos(theta)), 0)
        print('pt1 = ', pt1)
        # 该直线与最后一行的交点
        pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
        print('pt2 = ', pt2)



# 竖线 (找到轮廓上的点)
axe1 = []
axe2 = []
for ax in contours:
    d = (ax[1]-pt1[1])**2 + (ax[0]-pt1[0])**2
    axe1.append(d)
    axe2.append(ax)
a = axe1.index(min(axe1))
p1_t = axe2[a]
print('顶端的坐标: ', p1_t)


axe3 = []
axe4 = []
for ax in contours:
    d = (ax[1]-pt2[1])**2 + (ax[0]-pt2[0])**2
    axe3.append(d)
    axe4.append(ax)
b = axe3.index(min(axe3))
p2_b = axe4[b]
print('低端的坐标: ', p2_b)


# 横着的和竖着的 斜率
k1 = (p2_b[1]-p1_t[1])/(p2_b[0]-p1_t[0])
k2 = -1/(k1)


def search_points(p1, p2, k, contours, search_heng=True):
    '''
    :param p1: e.g. p1_t
    :param p2: e.g. p2_b
    :param k: 准备画的线的斜率 k1 or k2
    :param contours: boundary
    :return: center point , left point right point or top point bottom point
    '''
    p_c = [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]  # 要画的线经过的中心点
    ax1 = []
    ax1_points = []
    ax2 = []
    ax2_points = []

    for ax in contours:
        d = abs((k) * ax[0] - ax[1] - (k) * p_c[0] + p_c[1]) / math.sqrt(((k) ** 2 + 1))
        if search_heng is True:
            if ax[0] >= p1[0]:
                ax1.append(d)
                ax1_points.append(ax)
            else:
                ax2.append(d)
                ax2_points.append(ax)
        else:
            if ax[1] >= p2[1]:
                ax1.append(d)
                ax1_points.append(ax)
            else:
                ax2.append(d)
                ax2_points.append(ax)
    p3 = ax1_points[ax1.index(min(ax1))]
    p4 = ax2_points[ax2.index(min(ax2))]

    return p_c, p3, p4

p3_c, p4_r, p5_l = search_points(p1_t, p2_b, k2, contours, search_heng=True)
p6_c, p7_r, p8_l = search_points(p1_t, p3_c, k2, contours, search_heng=True)
p9_c, p10_r, p11_l = search_points(p2_b, p3_c, k2, contours, search_heng=True)
p12_c, p13_t, p14_b = search_points(p5_l, p3_c, k1, contours, search_heng=False)
p15_c, p16_t, p17_b = search_points(p4_r, p3_c, k1, contours, search_heng=False)



# # 找横线(找中间的点)
# p3 = [(p1_t[0]+p2_b[0])/2, (p1_t[1]+p2_b[1])/2]
# print('中间的坐标: ', p3)
#
# axe5 = []
# axe5_ax = []
# axe6 = []
# axe6_ax = []
# for ax in contours:
#     d = abs((k2)*ax[0] - ax[1] - (k2)*p3[0] + p3[1]) / math.sqrt(((k2)**2 + 1))
#     if ax[0] >= p1_t[0]:
#         axe5.append(d)
#         axe5_ax.append(ax)
#     else:
#         axe6.append(d)
#         axe6_ax.append(ax)
# p4_r = axe5_ax[axe5.index(min(axe5))]
# p5_l = axe6_ax[axe6.index(min(axe6))]
# print(p4_r)
# print(p5_l)
#
#
# # 找中上横线
# p6 = [(p1_t[0]+p3[0])/2, (p1_t[1]+p3[1])/2]
# print('中上的坐标: ', p6)
#
# axe7 = []
# axe7_ax = []
# axe8 = []
# axe8_ax = []
# for ax in contours:
#     d = abs((k2)*ax[0] - ax[1] - (k2)*p6[0] + p6[1]) / math.sqrt(((k2)**2 + 1))
#     if ax[0] >= p1_t[0]:
#         axe7.append(d)
#         axe7_ax.append(ax)
#     else:
#         axe8.append(d)
#         axe8_ax.append(ax)
# p7_r = axe7_ax[axe7.index(min(axe7))]
# p8_l = axe8_ax[axe8.index(min(axe8))]
# print(p7_r)
# print(p8_l)
#
#
# # 找中下横线
# p9 = [(p2_b[0]+p3[0])/2, (p2_b[1]+p3[1])/2]
# print('中上的坐标: ', p9)
#
# axe10 = []
# axe10_ax = []
# axe11 = []
# axe11_ax = []
# for ax in contours:
#     d = abs((k2)*ax[0] - ax[1] - (k2)*p9[0] + p9[1]) / math.sqrt(((k2)**2 + 1))
#     if ax[0] >= p1_t[0]:
#         axe10.append(d)
#         axe10_ax.append(ax)
#     else:
#         axe11.append(d)
#         axe11_ax.append(ax)
# p10_r = axe10_ax[axe10.index(min(axe10))]
# p11_l = axe11_ax[axe11.index(min(axe11))]
# print(p10_r)
# print(p11_l)
#
# # 找左边
# p12 = [(p5_l[0]+p3[0])/2, (p5_l[1]+p3[1])/2]
# print('左边的坐标: ', p12)
#
# axe13 = []
# axe13_ax = []
# axe14 = []
# axe14_ax = []
# for ax in contours:
#     d = abs((k1)*ax[0] - ax[1] - (k1)*p12[0] + p12[1]) / math.sqrt(((k1)**2 + 1))
#     if ax[1] >= p3[1]:
#         axe13.append(d)
#         axe13_ax.append(ax)
#     else:
#         axe14.append(d)
#         axe14_ax.append(ax)
# p13_t = axe13_ax[axe13.index(min(axe13))]
# p14_b = axe14_ax[axe14.index(min(axe14))]
# print(p13_t)
# print(p14_b)
#
# # 找右边
# p15 = [(p4_r[0]+p3[0])/2, (p4_r[1]+p3[1])/2]
# print('右边的坐标: ', p15)
#
# axe16 = []
# axe16_ax = []
# axe17 = []
# axe17_ax = []
# for ax in contours:
#     d = abs((k1)*ax[0] - ax[1] - (k1)*p15[0] + p15[1]) / math.sqrt(((k1)**2 + 1))
#     if ax[1] >= p3[1]:
#         axe16.append(d)
#         axe16_ax.append(ax)
#     else:
#         axe17.append(d)
#         axe17_ax.append(ax)
# p16_t = axe16_ax[axe16.index(min(axe16))]
# p17_b = axe17_ax[axe17.index(min(axe17))]
# print(p16_t)
# print(p17_b)


# 绘制轮廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

rows,cols=img.shape
ax1.axis([0,rows,cols,0])
# for n, contour in enumerate(contours):

ax1.plot(contours[:, 0], contours[:, 1], linewidth=2)
ax1.axis('image')
ax1.set_title('contours')
ax1.plot([p1_t[0],p2_b[0]], [p1_t[1],p2_b[1]], 'r-')
ax1.plot([p4_r[0],p5_l[0]], [p4_r[1],p5_l[1]], 'g-')
ax1.plot([p7_r[0],p8_l[0]], [p7_r[1],p8_l[1]], 'g-')
ax1.plot([p10_r[0],p11_l[0]], [p10_r[1],p11_l[1]], 'g-')
ax1.plot([p13_t[0],p14_b[0]], [p13_t[1],p14_b[1]], 'r-')
ax1.plot([p16_t[0],p17_b[0]], [p16_t[1],p17_b[1]], 'r-')

plt.show()


