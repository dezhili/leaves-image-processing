import cv2  
import numpy as np  
from matplotlib import pyplot as plt


# GrayImage=cv2.imread('9.JPG', cv2.IMREAD_GRAYSCALE)  

# GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
# ret,thresh1=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)  
# ret,thresh2=cv2.threshold(GrayImage,200,255,cv2.THRESH_BINARY_INV) 

# ret,thresh3=cv2.threshold(GrayImage,127,255,cv2.THRESH_TRUNC)  
# ret,thresh4=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO)  
# ret,thresh5=cv2.threshold(GrayImage,127,255,cv2.THRESH_TOZERO_INV)
# im_floodfill = thresh2.copy()
# h, w = thresh2.shape[:2]
# mask = np.zeros((h+2, w+2), np.uint8)
# cv2.floodFill(im_floodfill, mask, (0,0), 255)
# im_floodfill_inv = cv2.bitwise_not(im_floodfill)
# im_out = thresh2 | im_floodfill_inv
# plt.imshow(thresh2)
# plt.imshow(im_floodfill)
# plt.imshow(im_floodfill_inv)
# plt.imshow(im_out)
# plt.show()
# cv2.imshow("Thresholded Image", thresh2)
# cv2.imshow("Floodfilled Image", im_floodfill)
# cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
# cv2.imshow("Foreground", im_out)
# cv2.waitKey(0)



# titles = ['Gray Image','BINARY_INV']  
# images = [GrayImage, thresh2]  
# for i in range(2):  
#    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')  
#    plt.title(titles[i])  
#    plt.xticks([]),plt.yticks([])  
# plt.show() 




# img = cv2.imread('9.jpg',0) 
# edges = cv2.Canny(img,100,200)
# plt.subplot(121),plt.imshow(img,cmap = 'gray') 
# plt.title('Original Image')
# plt.xticks([]), plt.yticks([]) 
# plt.subplot(122),plt.imshow(edges,cmap = 'gray') 
# plt.title('Edge Image')
# plt.xticks([]), plt.yticks([])
# plt.show()




import cv2  
from skimage import measure
  
img = cv2.imread('9.jpg')  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# contours1 = measure.find_contours(gray, 0.5)

ret, binary = cv2.threshold(gray,155,255,cv2.THRESH_BINARY_INV)  
  
_, contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
  

contours_rechanged = list(filter(lambda x:len(x)>=100, contours))
print(type(contours_rechanged))
print(type(contours_rechanged[0]))
print(len(contours_rechanged))
print(contours_rechanged)
print(len(contours_rechanged[-1])) 

cv2.drawContours(img,contours_rechanged,-1,(0,0,255),3) 

contours_rechanged = np.asarray(contours_rechanged)
print(type(contours_rechanged))
contours_rechanged = np.squeeze(contours_rechanged)
print(contours_rechanged.shape)
plt.plot(contours_rechanged[:,0], contours_rechanged[:,1])
# print(hierarchy)
# print(contours)
# print(len(contours))
# plt.imshow(img)
# plt.imshow(binary)
plt.show()
# cv2.imshow("image", img)
# cv2.imshow("binary image", binary)
# cv2.waitKey(0)