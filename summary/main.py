import get_leave_boundary
import get_leave_serration
import leave_splite
import get_leave_top_bottom
import get_leave_area_circum
import save_in_csv_and_text
import correction
import cv2
import math
import os

import matplotlib.pyplot as plt
import xlwt


# split images
leave_splite.split_save_images('./split_before/', './split_after/')
images = os.listdir('./split_before/')


# get the list of splited images
img_list = leave_splite.get_imlist('./split_after/')


plt.figure(figsize=(6, 8))

f1 = xlwt.Workbook()
f2 = xlwt.Workbook()


for img in img_list:
    # get leaf contours
    contours = get_leave_boundary.get_leave_boundary(img)
    print('叶片边界坐标: ', contours)

    print('getting serration width depth numbers and curvatures ...')
    # get serration width depth numbers and curvatures ...
    ser4_idx, ser4_deepest_idx, serration_numbers, serration_depths, serration_widthes, \
        serration_circums, curvatures_mean, curvatures_median, curvatures_std, \
        boundary_curvature_mean, boundary_curvature_median, \
        boundary_curvature_std, boundary_curvature, serrations_curvatures = \
        get_leave_serration.get_leave_serration(contours)


    # serration_area = get_leave_area_circum.get_leave_area(contours)
    serrations_names = ['serration_idx', 'serration_depths', 'serration_widthes',
                        'serration_circums', 'curvatures_mean', 'curvatures_median',
                        'curvatures_std', 'boundary_curvature_mean', 'boundary_curvature_median',
                        'boundary_curvature_std']
    serrations = [serration_numbers, serration_depths, serration_widthes,
                  serration_circums, curvatures_mean, curvatures_median,
                  curvatures_std, boundary_curvature_mean, boundary_curvature_median,
                  boundary_curvature_std]


    (filepath, tempfilename) = os.path.split(img)
    (shotname, extension) = os.path.splitext(tempfilename)  # shotname : 442_100_1
    name1 = str(shotname) + '.csv'
    name2 = str(shotname) + '_curvatures.csv'


    # 442_100.xls
    # save to results of csv format
    save_in_csv_and_text.save_in_csv_serrations(f1,
                                                serrations=serrations,
                                              serrations_names=serrations_names,
                                              filename=name1)
    sheet1 = f1.add_sheet(name1, cell_overwrite_ok=True)
    for i in range(len(serrations)):
        sheet1.write(0, i, serrations_names[i])
    for i in range(9):
        if i == 0:
            for j in range(1, serrations[i]+1):
                sheet1.write(j, i, j)
            continue
        for j in range(1, len(serrations[i])+1):
            sheet1.write(j, i, serrations[i][j-1])

    # 442_100_curvatures.xls
    save_in_csv_and_text.save_in_csv_curvatures(f2,
                                                serrations_curvatures=serrations_curvatures,
                                                boundary_curvature=boundary_curvature,
                                                filename=name2)

    sheet2 = f2.add_sheet(name2, cell_overwrite_ok=True)
    for i in range(len(serrations_curvatures)):
        sheet2.write(0, i, 'serrations_'+str(i+1)+'_curvature')
    sheet2.write(0, len(serrations_curvatures), 'boundary_curvature')
    for i in range(len(serrations_curvatures)):
        for j in range(1, len(serrations_curvatures[i]) + 1):
            sheet2.write(j, i, serrations_curvatures[i][j-1])
    for i in range(1, len(boundary_curvature)+1):
        sheet2.write(i, len(serrations_curvatures), boundary_curvature[i-1])

    get_leave_serration.show_leave_serration(contours, ser4_idx, ser4_deepest_idx)
    plt.figure(figsize=(6, 8))


    print('getting leaf width height ...')
    # get leaf width height and rotating angle
    p1_t, p2_b, k1, k2 = get_leave_top_bottom.get_leave_top_bottom(img, contours)
    p3_c, p4_r, p5_l = get_leave_top_bottom.search_points(p1_t, p2_b, k2, contours, search_heng=True)
    p6_c, p7_r, p8_l = get_leave_top_bottom.search_points(p1_t, p3_c, k2, contours, search_heng=True)
    p9_c, p10_r, p11_l = get_leave_top_bottom.search_points(p2_b, p3_c, k2, contours, search_heng=True)
    p12_c, p13_t, p14_b = get_leave_top_bottom.search_points(p5_l, p3_c, k1, contours, search_heng=False)
    p15_c, p16_t, p17_b = get_leave_top_bottom.search_points(p4_r, p3_c, k1, contours, search_heng=False)
    # 计算长度 宽度
    len_c = math.sqrt((p1_t[0] - p2_b[0]) ** 2 + (p1_t[1] - p2_b[1]) ** 2) / 118.11
    len_l = math.sqrt((p13_t[0] - p14_b[0]) ** 2 + (p13_t[1] - p14_b[1]) ** 2) / 118.11
    len_r = math.sqrt((p16_t[0] - p17_b[0]) ** 2 + (p16_t[1] - p17_b[1]) ** 2) / 118.11
    wid_c = math.sqrt((p5_l[0] - p4_r[0]) ** 2 + (p5_l[1] - p4_r[1]) ** 2) / 118.11
    wid_t = math.sqrt((p8_l[0] - p7_r[0]) ** 2 + (p8_l[1] - p7_r[1]) ** 2) / 118.11
    wid_b = math.sqrt((p11_l[0] - p10_r[0]) ** 2 + (p11_l[1] - p10_r[1]) ** 2) / 118.11
    print('中间的长度为:\t', len_c)
    print('左边的长度为:\t', len_l)
    print('右边的长度为:\t', len_r)
    print('中间的宽度为:\t', wid_c)
    print('上边的宽度为:\t', wid_t)
    print('下边的宽度为:\t', wid_b)

    # plot
    image = cv2.imread(img, 0)
    fig, axes = plt.subplots(1, 2, figsize=(8, 8))
    ax0, ax1 = axes.ravel()
    ax0.imshow(image, plt.cm.gray)
    ax0.set_title('original image')

    rows, cols = image.shape
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


    print('correct image with rotating angle ...')
    # correct image with rotating angle
    img_corrected, correction_angle = correction.correction(img)


    # get leave area and circum
    leaf_circum = get_leave_area_circum.get_leave_circum(contours)
    print('整个叶片的周长为: ', leaf_circum)


f1.save(images[0].split('.')[0]+'.csv')
f2.save(images[0].split('.')[0]+'_curvatures.csv')









