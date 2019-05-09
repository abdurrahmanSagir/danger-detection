import numpy as np
import cv2

def denoise(frame):
##    frame = cv2.medianBlur(frame,9)
    frame = cv2.GaussianBlur(frame,(5,5),0)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    return frame
