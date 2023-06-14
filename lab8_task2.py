import time

import cv2
import numpy as np


def video_processing():
    fly64 = cv2.imread('fly64.png')
    fly64 = cv2.resize(fly64, (32, 32))
    fly_height, fly_width, _ = fly64.shape

    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    x_middle = np.array([])
    y_middle = np.array([])
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        frame_height, frame_width, _ = frame.shape
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            x_l = x + (w // 2)
            y_l = y + (h // 2)
            frame[y_l: y_l + fly_height, x_l: x_l + fly_width] = fly64
            x_middle = np.append(x_middle, x_l)
            y_middle = np.append(y_middle, y_l)
            print(f'Middle coordinates of current frame: ({x_l}, {y_l})')
            print(f'Middle coordinates of all frames: ({np.mean(x_middle)}, {np.mean(y_middle)})')

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()


if __name__ == '__main__':
    video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()