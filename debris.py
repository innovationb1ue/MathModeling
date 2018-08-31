import numpy as np
from PIL import Image
import os
import time

img_path = 'C:/Users/Administrator/Desktop/2010-2017年全国数学建模竞赛题/cumcm2013problems/B/附件3'
filenames = os.listdir(img_path)
print(filenames)

debrislist = []
for i in range(0, 209):
    temp = Image.open(img_path+'/'+filenames[i])
    debrislist.append(temp)

print(debrislist)

rightleftlist = []
for img in debrislist:
    blackwhite = img.convert('1')
    blackwhitelist = np.array(blackwhite)
    left , right = [], []
    for row in blackwhitelist:
        left.append(row[0])
        right.append(row[len(row)-1])
    rightleftlist.append([left, right])


print(len(rightleftlist))
print(len(blackwhitelist))


lefts = []
rights = []


lefts = []
rights = []

for i in rightleftlist:
    lefts.append(i[0])
    rights.append(i[1])

print(len(lefts))




finaldict = {}
for left in enumerate(lefts):
    maxcount = 0
    for right in enumerate(rights):
        count = 0
        print('comparing:', left[0],'&',right[0] )
        for i in range(180):
            if left[1][i] == False and right[1][i] == False:
                count += 1
            if left[1][i] == True and right[1][i] == True:
                count += 1
        if count >= maxcount:
            maxcount = count
            temp = []
        temp.append(left[0])
        temp.append(right[0])

    if maxcount >= 0.98*len(left[1]) or count >= 0.98*len(right[1]):
        finaldict[temp[1]] = temp[0]


print(finaldict)
