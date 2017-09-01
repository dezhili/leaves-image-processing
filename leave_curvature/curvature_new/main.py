import cv2
import get_leaf_curvature
import display_curvature_in_excel
import get_boundary_segment_evenly


# 读入图像
img = cv2.imread('seg_1.jpg')

# 显示曲率
curvature, points = get_leaf_curvature.get_leaf_curvature(img)

# 生成excel(x, y, curvature)
path_and_filename = input("Please enter the filename of .xlsx: ")
display_curvature_in_excel.display_curvature_in_excel(path_and_filename, points, curvature)

# 均分轮廓
get_boundary_segment_evenly.get_boundary_segment_evenly(img)

