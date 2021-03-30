import cv2
import numpy as np


def resize_img(loc):

    img = cv2.imdecode(np.asarray(bytearray(loc.read()), dtype=np.uint8), cv2.IMREAD_GRAYSCALE)

    img = cv2.medianBlur(img, 1)

    width = 1200
    height = int(img.shape[0] * 1200 / img.shape[1])

    img = cv2.resize(img, (width, height))

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=50, param2=30, minRadius=12, maxRadius=20)

    circles = np.uint16(np.around(circles))

    x1_min = 0
    y1_min = 0

    x2_max = 0
    y2_min = 0

    x3_min = 0
    y3_max = 0

    x4_max = 0
    y4_max = 0

    tmp = 0

    d1, d1_keep = 0, 0
    d2, d2_keep = 0, 0
    d3, d3_keep = 0, 0
    d4, d4_keep = 0, 0

    for i in circles[0, :]:
        # draw the outer circle
        # cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # draw the center of the circle
        # cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

        if tmp == 0:
            x1_min = i[0]
            y1_min = i[1]

            x2_max = i[0]
            y2_min = i[1]

            x3_min = i[0]
            y3_max = i[1]

            x4_max = i[0]
            y4_max = i[1]

            d1 = (x1_min ** 2 + y1_min ** 2) ** 0.5
            d2 = ((abs(width - x2_max)) ** 2 + y2_min ** 2) ** 0.5
            d3 = (x3_min ** 2 + ((abs(height - y3_max)) ** 2)) ** 0.5
            d4 = ((abs(width - x4_max)) ** 2 + (abs(height - y4_max)) ** 2) ** 0.5
            tmp = 1

        d1_keep = (i[0] ** 2 + i[1] ** 2) ** 0.5
        d2_keep = ((abs(width - i[0])) ** 2 + i[1] ** 2) ** 0.5
        d3_keep = (i[0] ** 2 + (abs(height - i[1])) ** 2) ** 0.5
        d4_keep = ((abs(width - i[0])) ** 2 + ((abs(height - i[1])) ** 2)) ** 0.5

        if d1 > d1_keep:
            d1 = d1_keep
            x1_min = i[0]
            y1_min = i[1]
        elif d2 > d2_keep:
            d2 = d2_keep
            x2_max = i[0]
            y2_min = i[1]
        elif d3 > d3_keep:
            d3 = d3_keep
            x3_min = i[0]
            y3_max = i[1]
        elif d4 > d4_keep:
            d4 = d4_keep
            x4_max = i[0]
            y4_max = i[1]

    x1_min = int(x1_min) - 40
    x2_max = int(x2_max) + 40
    x3_min = int(x3_min) - 40
    x4_max = int(x4_max) + 40

    y1_min = int(y1_min) - 40
    y2_min = int(y2_min) - 40
    y3_max = int(y3_max) + 40
    y4_max = int(y4_max) + 40

    d1 = abs((x1_min - x2_max)) ** 2 + abs((y1_min - y2_min)) ** 2
    d2 = abs((x3_min - x4_max)) ** 2 + abs((y3_max - y4_max)) ** 2

    d3 = abs((x1_min - x3_min)) ** 2 + abs((y1_min - y3_max)) ** 2
    d4 = abs((x4_max - x2_max)) ** 2 + abs((y4_max - y2_min)) ** 2

    x_max = int((max(d1, d2)) ** .5)
    y_max = int((max(d3, d4)) ** .5)

    dst = np.array([
        [0, 0],
        [x_max - 1, 0],
        [x_max - 1, y_max - 1],
        [0, y_max - 1]], dtype="float32")

    rect = np.zeros((4, 2), dtype="float32")

    rect[0] = [x1_min, y1_min]
    rect[1] = [x2_max, y2_min]
    rect[2] = [x4_max, y4_max]
    rect[3] = [x3_min, y3_max]

    M = cv2.getPerspectiveTransform(rect, dst)

    img = cv2.resize(img, (width, height))
    img = cv2.warpPerspective(img, M, (x_max, y_max))
    return img
