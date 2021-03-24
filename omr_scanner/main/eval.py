import cv2


def eval(loc1, loc2):
    img1 = cv2.imread(loc1, 0)  # answer
    h = int(img1.shape[0] * 1200 / img1.shape[1])
    img1 = cv2.resize(img1, (1200, h))

    img2 = cv2.imread(loc2, 0)  # omr
    img2 = cv2.resize(img2, (1200, h))

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

    return img

