from skimage import io,transform
import matplotlib.pyplot as plt

def get_leave_rotated(img, rotated_angle=180):
    img2 = io.imread(img)
    img2 =transform.rotate(img2, rotated_angle)     #旋转180度，不改变大小
    plt.imshow(img2)
    plt.show()
