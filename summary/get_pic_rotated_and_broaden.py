import cv2
from math import *
import numpy as np


def get_pic_rotated_and_broaden(img, degree=45, flag=0):

    # 获取旋转后4角的填充色
    filled_color = img[0][0]
    if isinstance(filled_color, np.uint8):
        filled_color = (filled_color, )
    filled_color = tuple([int(i) for i in filled_color])
    if flag:
        filled_color = (0, 0, 0)
    height, width = img.shape[:2]

    # 旋转后的尺寸
    height_new = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    width_new = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))

    mat_rotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree, 1)

    mat_rotation[0, 2] += (width_new - width) / 2  # 重点在这步，目前不懂为什么加这步
    mat_rotation[1, 2] += (height_new - height) / 2  # 重点在这步

    img_rotation = cv2.warpAffine(img, mat_rotation, (width_new, height_new), borderValue=filled_color)

    return img_rotation
