import leave_splite
import leave_border2

'''
1. leave splite
'''
# read in images , splite images and save images 
# './split_before/', './split_after/' is a example

leave_splite.split_save_images('./split_before/', './split_after/')



'''
2. leave process
'''
# get leaf border, here 'seg_0.jpg' is a example
leave_border2.get_leaf_border('seg_0.jpg')