import cv2
import numpy as np
import math
import matplotlib.pyplot as plt



# 获取顶端 低端 两点坐标
def get_leave_top_bottom(image, contours):
    img = cv2.imread(image, 0)

    img = cv2.GaussianBlur(img, (3, 3), 0)
    edges = cv2.Canny(img, 50, 90, apertureSize=3)
    plt.imshow(edges, cmap='gray')
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 90)  # 这里对最后一个参数使用了经验型的值
    print('lines.shape :', lines.shape)

    result = img.copy()
    # for line in lines[0]:
    #     rho = line[0]  # 第一个元素是距离rho
    #     theta = line[1]  # 第二个元素是角度theta
    #     print(rho)
    #     print(theta)
    #     if (theta < (np.pi / 4.)) or (theta > (3. * np.pi / 4.0)):  # 垂直直线
    #
    #         # 该直线与第一行的交点
    #         pt1 = (int(rho / np.cos(theta)), 0)
    #         print('pt1 = ', pt1)
    #         # 该直线与最后一行的交点
    #         pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
    #         print('pt2 = ', pt2)

    theta_list = []
    pt1_list = []
    pt2_list = []
    for li in lines:
        rho = li[0][0]
        theta = li[0][1]
        theta_list.append(theta)
        pt1 = (int(rho / np.cos(theta)), 0)
        pt1_list.append(pt1)
        pt2 = (int((rho - result.shape[0] * np.sin(theta)) / np.cos(theta)), result.shape[0])
        pt2_list.append(pt2)
        print('theta:', theta, 'pt1:', pt1, 'pt2:', pt2)

    a = theta_list.index(min(theta_list))
    b = theta_list.index(max(theta_list))

    pt1_1 = pt1_list[a]
    pt1_2 = pt1_list[b]

    pt2_1 = pt2_list[a]
    pt2_2 = pt2_list[b]

    theta_list_l = [list for list in theta_list if list >1]
    theta_list_r = [list for list in theta_list if list <= 1]
    print(theta_list_l)
    print(theta_list_r)

    if len(theta_list_r) >= len(theta_list_l):
        pt1 = pt1_1
        pt2 = pt2_1
    else:
        pt1 = pt1_2
        pt2 = pt2_2

    print('real pt1: ', pt1, 'real pt2: ', pt2)



    # 竖线 (找到轮廓上的点)
    axe1 = []
    axe2 = []
    for ax in contours:
        d = (ax[1] - pt1[1]) ** 2 + (ax[0] - pt1[0]) ** 2
        axe1.append(d)
        axe2.append(ax)
    a = axe1.index(min(axe1))
    p1_t = axe2[a]
    print('顶端的坐标: ', p1_t)

    axe3 = []
    axe4 = []
    for ax in contours:
        d = (ax[1] - pt2[1]) ** 2 + (ax[0] - pt2[0]) ** 2
        axe3.append(d)
        axe4.append(ax)
    b = axe3.index(min(axe3))
    p2_b = axe4[b]
    print('低端的坐标: ', p2_b)

    # 横着的和竖着的 斜率
    k1 = (p2_b[1] - p1_t[1]) / (p2_b[0] - p1_t[0])
    k2 = -1 / (k1)
    return p1_t, p2_b, k1, k2


# 获取其他相关点坐标
def search_points(p1, p2, k, contours, search_heng=True):
    '''
    :param p1: e.g. p1_t
    :param p2: e.g. p2_b
    :param k: 准备画的线的斜率 k1 or k2
    :param contours: boundary
    :return: center point , left point right point or top point bottom point
    '''
    p_c = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]  # 要画的线经过的中心点
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






