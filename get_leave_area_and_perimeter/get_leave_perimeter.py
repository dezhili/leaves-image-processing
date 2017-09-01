import cv2
from skimage import measure, color
import numpy as np


def get_leave_perimeter(image, dpi=(96, 96)):
    img = cv2.imread(image)
    # 生成二值测试图像
    img = color.rgb2gray(img)

    # 检测所有图形的轮廓
    contours = measure.find_contours(img, 0.68, fully_connected='high')
    contours = [contours[i] for i in range(len(contours)) if len(contours[i]) > 100]
    contours = np.array(contours)
    contours = np.squeeze(contours, axis=(0,))
    for i in range(len(contours)):
        contours[i, 0], contours[i, 1] = contours[i, 1], contours[i, 0]

    perimeter = len(contours) / dpi[0] * 2.54
    return perimeter
