
import warnings

warnings.simplefilter("error")

def cuff(fpkmlist):   # print lines with changes
    k = open(fpkmlist)
    l2 = []
    li = []
    for line in k:
        l2.append(line.strip().split('\t'))
    for i in range(len(l2)):
        if l2[i][0] != 'tracking_id':
            if (float(l2[i][9]) >= 5 or float(l2[i][13]) >= 5):
                li.append([l2[i][3], l2[i][0], l2[i][9], l2[i][13]])
    return li


import numpy as np


def change(fpkmlist, f2write):  # print out changes, which exceeds st dev
    lis = cuff(fpkmlist)
    list_with_dev = np.array([])
    li = []
    r = open(f2write, 'w')
    for i in range(len(lis)):
        k = 0
        for n in range(len(lis)):
            if lis[n][0] == lis[i][0]:
                k += float(lis[n][2])
        k2 = 0
        for n in range(len(lis)):
            if lis[n][0] == lis[i][0]:
                k2 += float(lis[n][3])
        if k != 0 and k2 != 0:
            list_with_dev = np.append(list_with_dev, abs(float(lis[i][3])/k2 - float(lis[i][2])/k))
            li.append([lis[i][0], lis[i][1], float(lis[i][2])/k, float(lis[i][3])/k2, float(lis[i][3])/k2 - float(lis[i][2])/k])
        elif k == 0 and k2 != 0:
            list_with_dev = np.append(list_with_dev, float(lis[i][3])/k2)
            li.append([lis[i][0], lis[i][1], 0, float(lis[i][3])/k2, float(lis[i][3])/k2])
        elif k != 0 and k2 == 0:
            list_with_dev = np.append(list_with_dev, float(lis[i][2])/k)
            li.append([lis[i][0], lis[i][1], float(lis[i][2])/k, 0, -float(lis[i][2])/k])
    stdev = np.std(list_with_dev)
    for i in range(len(li)):
        if li[i][2] != 0 and li[i][3] != 0 and abs(li[i][4]) > stdev:
            r.write(str(li[i][0]) + ' ' + str(li[i][1]) + ' ' + str(float(li[i][2])) + ' ' + str(float(li[i][3])) + ' ' + str(float(li[i][4])) + '\n')
        elif li[i][2] == 0 and li[i][3] != 0 and abs(li[i][4]) > stdev:
            r.write(str(li[i][0]) + ' ' + str(li[i][1]) + ' ' + '0' + ' ' + str(li[i][3]) + ' ' + str(float(li[i][3])) + '\n')
        elif k != 0 and k2 == 0 and abs(li[i][4]) > stdev:
            r.write(str(li[i][0]) + ' ' + str(li[i][1]) + ' ' + str(li[i][2]) + ' ' + '0' + ' ' + str(-float(li[i][2])) + '\n')
    r.close()

change('isoforms.fpkm_tracking', 'filewithchanges.txt')

