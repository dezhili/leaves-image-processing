import matplotlib.pyplot as plt
from skimage import measure,data,color
import cv2
import numpy as np 

def get_leave_boundary(image):
    img = cv2.imread(image)
    #生成二值测试图像
    img=color.rgb2gray(img)

    #检测所有图形的轮廓
    contours = measure.find_contours(img, 0.68, fully_connected='high')
    contours = [contours[i] for i in range(len(contours)) if len(contours[i]) > 100]
    contours = np.array(contours)
    contours = np.squeeze(contours, axis=(0,))
    for i in range(len(contours)):
        contours[i, 0], contours[i, 1] = contours[i, 1], contours[i, 0]
    # print(type(contours))
    # print(contours)
    # print(contours.shape)


    #绘制轮廓
    fig, axes = plt.subplots(1,2,figsize=(8,8))
    ax0, ax1= axes.ravel()
    ax0.imshow(img,plt.cm.gray)
    ax0.set_title('original image')

    rows,cols=img.shape
    ax1.axis([0,rows,cols,0])
    ax1.plot(contours[:,0], contours[:,1], linewidth=2)
    ax1.axis('image')
    ax1.set_title('contours')
    plt.show()
    return contours
