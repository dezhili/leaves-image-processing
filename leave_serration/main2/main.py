import get_leave_boundary
import get_leave_serration
import leave_splite
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
# get the serration of each image
for img in img_list:
    # get contours
    contours = get_leave_boundary.get_leave_boundary(img)
    print('叶片边界坐标: ', contours)

    # get serration
    ser4_idx, ser4_deepest_idx, serration_numbers, serration_depths, serration_widthes, \
        curvatures_mean, curvatures_median, curvatures_std, \
        boundary_curvature_mean, boundary_curvature_median, \
        boundary_curvature_std, boundary_curvature, serrations_curvatures = \
        get_leave_serration.get_leave_serration(contours)

    serrations_names = ['serration_idx', 'serration_depths', 'serration_widthes', 'curvatures_mean', 'curvatures_median',
                  'curvatures_std', 'boundary_curvature_mean', 'boundary_curvature_median', 'boundary_curvature_std']
    serrations = [serration_numbers, serration_depths, serration_widthes, curvatures_mean, curvatures_median,
                  curvatures_std, boundary_curvature_mean, boundary_curvature_median, boundary_curvature_std]


    (filepath, tempfilename) = os.path.split(img)
    (shotname, extension) = os.path.splitext(tempfilename)  # shotname : 442_100_1



    # 442_100.xls
    # save to results of csv format
    sheet1 = f1.add_sheet(str(shotname) + '.csv', cell_overwrite_ok=True)
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
    sheet2 = f2.add_sheet(str(shotname) + '_curvatures.csv', cell_overwrite_ok=True)
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

f1.save(images[0].split('.')[0]+'.csv')
f2.save(images[0].split('.')[0]+'_curvatures.csv')









