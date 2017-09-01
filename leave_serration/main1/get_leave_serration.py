import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import math
import csv


def get_leave_serration(contours):
    '''
    contours: 叶片边界坐标
    return: 叶片锯齿索引, 最深处索引, 锯齿个数，深度，宽度
    '''
    hull = ConvexHull(contours)

    print('ConvexHull选出的凸角索引: ', hull.vertices)
    print('ConvexHull选出的凸角个数: ', len(hull.vertices))

    # hull 中的index
    ser1_idx = sorted(hull.vertices)
    print('排序后的凸角索引: ', ser1_idx)

    plt.gca().invert_yaxis()
    plt.plot(contours[:,0], contours[:,1])


    # hull 中点的坐标
    ser1 = [contours[i] for i in ser1_idx]
    print('ConvexHull选出的凸角坐标: ', ser1)


    # 寻找ser2_idx
    ser2_idx = []
    for i in range(len(ser1_idx)-1):
        if abs(ser1_idx[i] - ser1_idx[i+1]) >=10:
            ser2_idx.append(ser1_idx[i])
    print('去除靠近的点后剩余的凸角索引: ', ser2_idx)
    print('去除靠近的点后剩余的凸角个数: ', len(ser2_idx))

    # 计算每一个ser2_idx 点之间的斜率
    M = []
    K = []
    for j in range(len(ser2_idx)):
        if j== len(ser2_idx)-1:
            break
        for k in range(ser2_idx[j], ser2_idx[j+1]):
            m = (contours[k+1, 1] - contours[ser2_idx[j], 1])/(contours[k+1, 0] - contours[ser2_idx[j], 0])
            M.append(m)
        K.append(M)
        M = []
    print('ser2_idx 两点之间斜率的变化: ')
    print(K)
    print(len(K))

    # 寻找中间斜率最大的index
    I = []
    for k in K:
        b = k.index(max(k))
        I.append(b)
    print('ser2_idx 两点之间斜率最大的点: ', I)


    # ser2_idx_max, 选择 ser3_idx
    ser2_idx_max = [a+b+1 for a,b in zip(ser2_idx[:-1], I)]
    print('斜率最大的点的 index: ', ser2_idx_max)

    ser3_idx = ser2_idx_max + ser2_idx
    ser3_idx = set(ser3_idx)
    ser3_idx = sorted(list(ser3_idx))
    print('添加斜率搜寻后的点 ser3_idx: ', ser3_idx)
    print(len(ser3_idx))

    ser3 = [contours[i] for i in ser3_idx]
    print('ser3_idx 中点的坐标: ', ser3)



    # depth
    N = []
    D = []
    for j in range(len(ser3_idx)):
        if j== len(ser3_idx)-1:
            break

        k = (contours[ser3_idx[j+1], 1] - contours[ser3_idx[j], 1])/(contours[ser3_idx[j+1], 0] - contours[ser3_idx[j], 0])

        for p in range(ser3_idx[j], ser3_idx[j+1]):
            f = abs(k*contours[p+1, 0]- contours[p+1, 1]-k*contours[ser3_idx[j], 0] + contours[ser3_idx[j], 1])
            d = f/math.sqrt(k**2 + 1)
            N.append(d)
        D.append(N)
        N = []
    print('ser3_idx 中两点之间的 depth: ', D)
    print(len(D))

    # 寻找中间深度最大的index
    DI = []
    ser3_deepest = []
    for d in D:
        b = d.index(max(d))
        DI.append(b)
    # print(DI)
    ser3_deepest = [max(d) for d in D]


    # Depth point
    ser3_deepest_idx = [a+b+1 for a,b in zip(ser3_idx[:-1], DI)]
    print('最大高度点的ser3_deepest_idx: ', ser3_deepest_idx)
    print('最大高度点对应的ser3_deepest个数为: ', len(ser3_deepest))
    print('最大高度点对应的ser3_deepest高度是: ', ser3_deepest)


    ser4_idx = []
    for i in range(len(ser3_deepest)):
        if ser3_deepest[i] > 1:
            ser4_idx.append(ser3_idx[i])
            ser4_idx.append(ser3_idx[i+1])

    ser4_deepest_idx = [ser3_deepest_idx[i] for i in range(len(ser3_deepest)) if ser3_deepest[i] > 1]
    ser4_deepest = [ser3_deepest[i] for i in range(len(ser3_deepest)) if ser3_deepest[i] > 1]

    ser4_widthes = []
    for i in range(0, len(ser4_idx), 2):
        width = math.sqrt((contours[ser4_idx[i+1], 1] - contours[ser4_idx[i], 1])**2 +
                          (contours[ser4_idx[i+1], 0] - contours[ser4_idx[i], 0])**2)
        ser4_widthes.append(width)

    ser4_deepest = [i/118.11 for i in ser4_deepest]
    ser4_widthes = [i/118.11 for i in ser4_widthes]

    print('最大高度点的ser4_deepest_idx: ', ser4_deepest_idx)
    print('最大高度点对应的ser4_deepest个数为: ', len(ser4_deepest))
    print('最大高度点对应的ser4_deepest高度是: ', ser4_deepest)
    print('ser4 的宽度: ', ser4_widthes)
    print('ser4 的个数: ', len(ser4_idx))
    print('ser4 的索引: ', ser4_idx)

    serration_numbers = len(ser4_deepest)
    serration_depths = ser4_deepest
    serration_widthes = ser4_widthes

    return ser4_idx, ser4_deepest_idx, serration_numbers, serration_depths, serration_widthes


def show_leave_serration(contours, ser4_idx, ser4_deepest_idx):
    for i in ser4_deepest_idx:
        plt.scatter(contours[i, 0], contours[i, 1], c='g', marker='x')
    for idx in ser4_idx:
        plt.scatter(contours[idx, 0], contours[idx, 1])


    plt.plot(contours[ser4_idx,0], contours[ser4_idx,1], 'r--', lw=2)

    plt.show()



def save_to_csv(serration_numbers, serration_depths, serration_widthes, name_str):
    # 将深度宽度等结果保存到文件
    results_list = list()
    # 写入参数配置
    results_list.append(['serration_idx', 'serration_depth', 'serration_width'])

    serration_idx = 0
    for i in range(serration_numbers+1):
        if serration_idx >= serration_numbers:
            break
        if serration_idx < serration_numbers:
            serration_depth = serration_depths[serration_idx]
            serration_width = serration_widthes[serration_idx]
            serration_idx += 1
            results_list.append([serration_idx, serration_depth, serration_width])

    # 将结果保存到文件
    results_file = open(name_str, 'w', newline='')
    csv_writer = csv.writer(results_file, dialect='excel')
    for row in results_list:
        csv_writer.writerow(row)


