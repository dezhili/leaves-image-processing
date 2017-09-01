import numpy as np
from scipy.interpolate import UnivariateSpline
import cv2
import copy
from skimage import measure, color


def curvature_splines(x, y=None, error=0.1):
    if y is None:
        x, y = x.real, x.imag

    t = np.arange(x.shape[0])
    std = error * np.ones_like(x)

    fx = UnivariateSpline(t, x, k=4, w=1 / np.sqrt(std))
    fy = UnivariateSpline(t, y, k=4, w=1 / np.sqrt(std))

    xˈ = fx.derivative(1)(t)
    xˈˈ = fx.derivative(2)(t)
    yˈ = fy.derivative(1)(t)
    yˈˈ = fy.derivative(2)(t)
    curvature = abs((yˈ* xˈˈ - xˈ* yˈˈ)) / np.power(xˈ** 2 + yˈ** 2, 3 / 2)
    return curvature


def get_leaf_curvature(img):
    # draw_circle函数
    def draw_circle(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            initial_img[:] = copy.deepcopy(img_cp[:])
            cv2.circle(initial_img, (x, y), 4, (0, 0, 255), -1)
            cv2.putText(initial_img, 'curvature on (' + str(x) + ',' + str(y) + ')', (0, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        0.4, (111, 0, 111))
            if (x, y) in search_points:
                idx = search_points.index((x, y))
                cv2.putText(initial_img, str(curvature[idx]), (0, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (111, 0, 111))

    # 保存原图及刷新所用备用图.
    initial_img = copy.deepcopy(img)
    img = color.rgb2gray(img)
    img_cp = copy.deepcopy(initial_img)

    # 取轮廓点
    contours = measure.find_contours(img, 0.60)
    contours = [contours[i] for i in range(len(contours)) if len(contours[i]) > 100]
    contours = np.ceil(contours)
    points = [contours[0].flatten()[1::2], contours[0].flatten()[::2]]
    search_points = list(zip(*points))
    curvature = curvature_splines(points[0], points[1])

    # 显示
    cv2.imshow('CURVATURE_OF_BOUNDARIES', initial_img)
    cv2.namedWindow('CURVATURE_OF_BOUNDARIES')
    cv2.setMouseCallback('CURVATURE_OF_BOUNDARIES', draw_circle)

    while 1:
        cv2.imshow('CURVATURE_OF_BOUNDARIES', initial_img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return curvature, points
