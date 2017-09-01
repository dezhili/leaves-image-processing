import numpy as np

def get_leave_circum(contours):
    circum = 0
    for i in range(len(contours)):
        if i == (len(contours)-1):
            break
        circum += (np.sqrt((contours[i+1, 1]-contours[i, 1])**2 + (contours[i+1, 0]-contours[i, 0])**2))/118.11
    return circum

# def get_leave_area(contours):
