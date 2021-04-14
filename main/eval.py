import cv2
import base64
import numpy as np


def eval(loc1, loc2):
    img1 = loc1
    h = int(img1.shape[0] * 1200 / img1.shape[1])
    img1 = cv2.resize(img1, (1200, h))

    img2 = cv2.resize(loc2, (1200, h))

    img = cv2.drawContours(
        cv2.drawContours(
            cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR),
            cv2.findContours(cv2.Canny(
                cv2.threshold(cv2.medianBlur(cv2.add(cv2.subtract(img1, img2), img2), 21), 100, 255, cv2.THRESH_OTSU)[
                    1],
                10, 10), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0], -1, (0, 255, 0), 3)
        ,
        cv2.findContours(cv2.Canny(
            cv2.threshold(cv2.medianBlur(cv2.bitwise_not(cv2.subtract(img2, img1)), 21), 100, 255, cv2.THRESH_OTSU)[1]
            , 10, 10), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
        , -1, (0, 0, 255), 3)

    img = cv2.resize(img, (500, int(img.shape[0] * 500 / img.shape[1])))

    img = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode('UTF-8')

    return str(img)

