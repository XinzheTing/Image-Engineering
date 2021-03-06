# -*- coding: UTF-8 -*-
# 要求：生成图像文件，要求颜色等阶渐变，观察人眼最小分辨率

import numpy as np
import cv2

img = np.zeros((400, 700, 3), np.uint8)

img[:,:, 0].fill(108)
img[:,:, 1].fill(99)
img[:,:, 2].fill(139)

# 生成渐变灰度图
for i in range(256):
    img[i + 50, 120:180, :] = 255 - i
    # 彩色渐变
    img[i + 50, 420:480, 0] = 255
    img[i + 50, 420:480, 1] = 255 - i
    img[i + 50, 420:480, 2] = i

# 生成等阶灰度图
for i in range(0, 256, 32):
    img[i + 50:i + 82, 220:280, :] = 255 - i
    # 彩色等阶图
    img[i + 50:i + 82, 520:580, 0] = 255
    img[i + 50:i + 82, 520:580, 1] = 255-i
    img[i + 50:i + 82, 520:580, 2] = i

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
