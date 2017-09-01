import get_leave_boundary
import get_leave_serration


# get contours
contours = get_leave_boundary.get_leave_boundary('442_100_1.JPG')
print('叶片边界坐标: ', contours)

# get serration
ser4_idx, ser4_deepest_idx, serration_numbers, serration_depths, serration_widthes = \
    get_leave_serration.get_leave_serration(contours)


# save to results of csv format
get_leave_serration.save_to_csv(serration_numbers, serration_depths,
                                serration_widthes, 'serration_results.csv')

# show serration
get_leave_serration.show_leave_serration(contours, ser4_idx, ser4_deepest_idx)

