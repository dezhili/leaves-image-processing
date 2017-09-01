import cv2
import numpy as np


def get_leave_areas(image):
    img = cv2.imread(image)
    GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, threshed_img = cv2.threshold(GrayImage, 160, 255,cv2.THRESH_BINARY)
    image, contours, hierarchy = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    small_areas = [i for i in contours if cv2.contourArea(i) < 200]
    cv2.fillPoly(threshed_img, small_areas, 255)

    print(cv2.contourArea(contours[0]) / (96*96))
    print(cv2.contourArea(contours[1]) / (96*96))
    # method_2
    area_pixel = 0
    for i in np.array(threshed_img).flatten():
        if i == 0:
            area_pixel += 1
    area_inch = area_pixel / (96*96)
    return area_inch
