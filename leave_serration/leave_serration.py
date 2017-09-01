
'''
contours = leave_border2.get_leaf_border('13.jpg')
contours = np.floor(contours)
# print(contours)
print(len(contours))

contours_1 = contours[:len(contours)//4]
print(contours_1)
print(contours.shape)
print(contours_1.shape)

plt.gca().invert_yaxis()
plt.plot(contours[:, 0], contours[:, 1])
# plt.scatter(contours_1[:,0], contours_1[:,1])

'''
# 对 contours_1 进行锯齿搜索
'''

# j = 0 # 记录跳跃的点
# i = 1
# l = []
# while i<len(contours_1)-2:
#     if contours_1[i][0] - contours_1[j][0] == 0:
#         i += 1
#         continue
#     k = (contours_1[i][1] - contours_1[j][1])/(contours_1[i][0] - contours_1[j][0])
#     m = (contours_1[i+1][1] - contours_1[j][1])/(contours_1[i+1][0] - contours_1[j][0])
#     n = (contours_1[i+2][1] - contours_1[j][1])/(contours_1[i+2][0] - contours_1[j][0])

#     if (m-k)*(n-m)<0:
#         l.append(i+1)
#         j = i+1
#         i = j
#         continue
#     else:
#         i+=1
# print(l)
# for i in l:
#     plt.scatter(contours_1[i,0], contours_1[i,1])
# plt.show()


j = 0
M = []

for k in range(len(contours_1)):
    L = []
    for i in range(0, j+1):
        k1 = -10
        L.append(k1)
    for i in range(j+1, len(contours_1)): 
        if (contours_1[i][0] == contours_1[j][0]) or (contours_1[i][1] == contours_1[j][1]):
            k1 = -10            
        else:
            k1 = (contours_1[i][1] - contours_1[j][1])/(contours_1[i][0] - contours_1[j][0])
        L.append(k1)
    j = L.index(max(L))
    M.append(j)
    if j >= len(contours_1):
        break
M = set(M)
print(M)
print(len(M))

for i in M:
    plt.scatter(contours_1[i,0], contours_1[i,1])
plt.show()

# B = []
# j = 0
# for i in range(len(contours_1)):
#     if (contours_1[i][0] == contours_1[j][0]) or (contours_1[i][1] == contours_1[j][1]):
#         k2 = -10
#     else:
#         k2 = (contours_1[i][1] - contours_1[j][1])/(contours_1[i][0] - contours_1[j][0])
#     B.append(k2)
# print(B)
# print(len(B))


# j = 0
# m = 0
# for i in range(0:len(contours):2):
#     k[i] = (contours[j+1, 2] - contours[j, 2])/(contours[j+1, 1] - contours[j, 1])
#     k[i+1] = (contours[j+2, 2] - contours[j, 2])/(contours[j+2, 1] - contours[j, 1])
#     k[i+2] = (contours[j+3, 2] - contours[j, 2])/(contours[j+3, 1] - contours[j, 1])
#     if (k[i+1]-k[i]) * (k[i+2]-k[i+1]) < 0:
#         p[m] = i+2
#         m += 1
'''
import get_leave_boundary
# import numpy as np
# import cv2
# # from skimage import measure,data,color
# # import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import math

#生成二值测试图像
contours = get_leave_boundary.get_leave_boundary('9.jpg')
# print(contours)
print('contours的形状是, ', contours.shape)
hull = ConvexHull(contours)

print('ConvexHull选出的凸角', hull)
print('len(vertices): ', len(hull.vertices))

# hull 中的index
vertices = sorted(hull.vertices)
print('排序后的 hull index: ', vertices)


plt.gca().invert_yaxis()
plt.plot(contours[:,0], contours[:,1])

for i in range(10):
    plt.plot(contours[i, 0], contours[i, 1], c = 'b', marker='x')



# hull 中点的坐标
ser1 = [contours[i] for i in vertices]
print('hull 中点的坐标: ', ser1)

# 第一步修正
vertices_re = []
for i in range(len(vertices)-1):
    if abs(vertices[i] - vertices[i+1]) >=10:
        vertices_re.append(vertices[i])
print('去除靠近的点后剩余的hull index: ', vertices_re)
print('len(vertices_re): ', len(vertices_re))

# 计算每一个vertices_re 点之间的斜率
M = []
K = []
for j in range(len(vertices_re)):
    if j== len(vertices_re)-1:
        break
    for k in range(vertices_re[j], vertices_re[j+1]):
        m = (contours[k+1, 1] - contours[vertices_re[j], 1])/(contours[k+1, 0] - contours[vertices_re[j], 0])
        M.append(m)
    K.append(M)
    M = []
print('vertices_re 两点之间斜率的变化: ')
print(K)
print(len(K))

# 寻找中间斜率最大的index
I = []
for k in K:
    b = k.index(max(k))
    I.append(b)
print('vertices_re 两点之间斜率最大的点: ', I)


# 更改了vertices_re
vertices_re1 = [a+b+1 for a,b in zip(vertices_re[:-1], I)]
print('斜率最大的点的 index: ', vertices_re1)

vertices_re2 = vertices_re1 + vertices_re
vertices_re2 = set(vertices_re2)
vertices_re2 = sorted(list(vertices_re2))
print('添加斜率搜寻后的点 vertices_re2: ', vertices_re2)
print(len(vertices_re2))

ser2 = [contours[i] for i in vertices_re2]
print('vertices_re2 中点的坐标: ', ser2)



# depth
N = []
D = []
for j in range(len(vertices_re2)):
    if j== len(vertices_re2)-1:
        break

    k = (contours[vertices_re2[j+1], 1] - contours[vertices_re2[j], 1])/(contours[vertices_re2[j+1], 0] - contours[vertices_re2[j], 0])

    for p in range(vertices_re2[j], vertices_re2[j+1]):
        f = abs(k*contours[p+1, 0]- contours[p+1, 1]-k*contours[vertices_re2[j], 0] + contours[vertices_re2[j], 1])
        d = f/math.sqrt(k**2 + 1)
        N.append(d)
    D.append(N)
    N = []
print('vertices_re2 中两点之间的 depth: ', D)
print(len(D))

# 寻找中间深度最大的index
DI = []
DP = []
for d in D:
    b = d.index(max(d))
    DI.append(b)
print(DI)
DP = [max(d) for d in D]
print(DP)
print('len(DP): ', len(DP))

# Depth point
Depth_re2 = [a+b+1 for a,b in zip(vertices_re2[:-1], DI)]
print('最大高度点的 index: ', Depth_re2)
print('最大高度点对应的高度是: ', DP)


vertices_re3 = []
for i in range(len(DP)):
    if DP[i] > 1:
        vertices_re3.append(vertices_re2[i])
        vertices_re3.append(vertices_re2[i+1])

Depth_re3 = [Depth_re2[i] for i in range(len(DP)) if DP[i] > 1]
print('Depth_re3: ', Depth_re3)

print('vertices_re3: ', vertices_re3)
print(len(vertices_re3))


for i in Depth_re3:
    plt.scatter(contours[i, 0], contours[i, 1], c='g', marker='x')
for ver in vertices_re3:
    plt.scatter(contours[ver, 0], contours[ver, 1])


plt.plot(contours[vertices_re3,0], contours[vertices_re3,1], 'r--', lw=2)
# plt.plot(contours[hull.vertices[0],0], contours[hull.vertices[0],1], 'ro')


plt.show()