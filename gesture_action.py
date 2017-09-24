import cv2
import numpy as np
import pyautogui as gui
from gesture_api import do_gesture_action
from collections import deque

cam = cv2.VideoCapture(0)
yellow_lower = np.array([7, 96, 85])                          # HSV yellow lower
yellow_upper = np.array([255, 255, 255])                      # HSV yellow upper
screen_width, screen_height = gui.size()
camx, camy = 480, 360
buff = 128
line_pts = deque(maxlen = buff)

def process_created_gesture(created_gesture):
    """
    function to remove all the St direction and removes duplicate direction if they
    occur consecutively.
    """
    if created_gesture != []:
        for i in range(created_gesture.count("St")):
            created_gesture.remove("St")
        for j in range(len(created_gesture)):
            for i in range(len(created_gesture) - 1):
                if created_gesture[i] == created_gesture[i+1]:
                    created_gesture.remove(created_gesture[i+1])
                    break
    return created_gesture

def gesture_action():
    centerx, centery = 0, 0
    old_centerx, old_centery = 0, 0
    area1 = 0
    c = 0
    flag_do_gesture = 0
    flag0 = True

    created_gesture_hand1 = []

    while True:
        _, img = cam.read()

        # Resize for faster processing. Flipping for better orientation
        img = cv2.flip(img, 1)
        img = cv2.resize(img, (camx, camy))

        # Convert to HSV for better color segmentation
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Mask for yellow color
        mask = cv2.inRange(imgHSV, yellow_lower, yellow_upper)

        # Bluring to reduce noises
        blur = cv2.medianBlur(mask, 15)
        blur = cv2.GaussianBlur(blur , (5,5), 0)

        # Thresholding
        _,thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow("Thresh", thresh)

        _, contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        w, h = 0, 0
        if len(contours) == 0:                                                  # Completion of a gesture
            line_pts = deque(maxlen = buff)                                     # Empty the deque
            processed_gesture_hand1 = tuple(process_created_gesture(created_gesture_hand1))
            if flag_do_gesture == 0:                                            # flag_do_gesture to make sure that gesture runs only once and not repeatedly
                if processed_gesture_hand1 != ():
                    do_gesture_action(processed_gesture_hand1)
                flag_do_gesture = 1
            print(processed_gesture_hand1)                                      # for debugging purposes
            created_gesture_hand1 = []
            flag0 = True
        else:
            flag_do_gesture = 0
            max_contour = max(contours, key = cv2.contourArea)
            rect1 = cv2.minAreaRect(max_contour)
            (w, h) = rect1[1]
            area1 = w*h
            if area1 > 450:
                center1 = list(rect1[0])
                box = cv2.boxPoints(rect1)                                      # to draw a rectangle
                box = np.int0(box)
                cv2.drawContours(img,[box],0,(0,0,255),2)
                centerx = center1[0] = int(center1[0])                          # center of the rectangle
                centery = center1[1] = int(center1[1])
                cv2.circle(img, (centerx, centery), 2, (0, 255, 0), 2)
                line_pts.appendleft(tuple(center1))
                if c == 0:
                    old_centerx = centerx
                    old_centery = centery
                c += 1

                diffx, diffy = 0, 0
                if c > 5:                                                       # check after every 5 iteration the new center
                    diffx = centerx - old_centerx
                    diffy = centery - old_centery
                    c = 0

                if flag0 == False:
                # the difference between the old center and the new center determines the direction of the movement
                    if abs(diffx) <=10 and abs(diffy) <= 10:
                        created_gesture_hand1.append("St")
                    elif diffx > 15 and abs(diffy) <= 15:
                        created_gesture_hand1.append("E")
                    elif diffx < -15 and abs(diffy) <= 15:
                        created_gesture_hand1.append("W")
                    elif abs(diffx) <= 15 and diffy < -15:
                        created_gesture_hand1.append("N")
                    elif abs(diffx) <= 15 and diffy > 15:
                        created_gesture_hand1.append("S")
                    elif diffx > 25 and diffy > 25:
                        created_gesture_hand1.append("SE")
                    elif diffx < -25 and diffy > 25:
                        created_gesture_hand1.append("SW")
                    elif diffx > 25 and diffy < -25:
                        created_gesture_hand1.append("NE")
                    elif diffx < -25 and diffy < -25:
                        created_gesture_hand1.append("NW")

                for i in range(1, len(line_pts)):
                    if line_pts[i - 1] is None or line_pts[i] is None:
                        continue
                    cv2.line(img, line_pts[i-1], line_pts[i], (0, 255, 0), 2)

                flag0 = False

        cv2.imshow("IMG", img)
        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()
    cam.release()


gesture_action()
