import tkinter
from skimage import measure, color
import numpy as np
import cv2
import copy
import math


def get_boundary_segment_evenly(img):
    # get contours and points
    initial_img = copy.deepcopy(img)
    img = color.rgb2gray(img)
    img_cp = copy.deepcopy(initial_img)

    contours = measure.find_contours(img, 0.60)
    contours = [contours[i] for i in range(len(contours)) if len(contours[i]) > 100]
    contours = np.ceil(contours)
    points = [contours[0].flatten()[1::2], contours[0].flatten()[::2]]
    search_points = list(zip(*points))

    # plot
    def inputint():
        initial_img[:] = copy.deepcopy(img_cp[:])
        nonlocal num_of_points
        try:
            num_of_points = int(var.get().strip())
            plot_points = search_points[::math.ceil(len(search_points) / num_of_points)]
            for i in plot_points:
                i = list(i)
                i[0] = int(i[0])
                i[1] = int(i[1])
                cv2.circle(initial_img, tuple(i), 4, (0, 0, 255), -1)
            cv2.imshow('CURVATURE_OF_BOUNDARIES', initial_img)
        except:
            num_of_points = 'Not a valid integer.'

    def inputclear():
        nonlocal num_of_points
        var.set('')
        num_of_points = ''
        initial_img[:] = copy.deepcopy(img_cp[:])
        cv2.imshow('CURVATURE_OF_BOUNDARIES', initial_img)

    num_of_points = 0
    root = tkinter.Tk(className='num of intervals')
    root.geometry('270x60')

    var = tkinter.StringVar()
    var.set('An integer in (1, 2027]') # 超过2027也没事, 只是已画满了所有点, 所以和2027没有变化了.
    entry1 = tkinter.Entry(root, textvariable=var)
    entry1.pack()
    btn1 = tkinter.Button(root, text='Input', command=inputint)
    btn2 = tkinter.Button(root, text='Clear', command=inputclear)

    btn2.pack(side='right')
    btn1.pack(side='right')

    # 显示
    cv2.imshow('CURVATURE_OF_BOUNDARIES', initial_img)
    cv2.namedWindow('CURVATURE_OF_BOUNDARIES')

    root.mainloop()
