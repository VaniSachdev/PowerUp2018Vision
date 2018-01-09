import cv2
import numpy as np
import GlobalVariables

cap = cv2.VideoCapture(0)

m_lower_limit = np.array([0,0,0])
m_upper_limit = np.array([1,1,1])

def setHSVLimits(lower_limit, upper_limit):
    m_lower_limit = lower_limit
    m_upper_limit = upper_limit

def HSVColorDetection():
    _, frame = cap.read()
   hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   mask = cv2.inRange(hsv, m_lower_limit, m_upper_limit)
   res = cv2.bitwise_and(frame,frame, mask= mask)
    # cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    cv2.imshow('res',res)

def CannyEdgeDetection(minVal, maxVal):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    edges = cv2.Canny(hsv, minVal, maxVal)
    cv2.imshow('img',edges)

def end():
    cv2.destroyAllWindows()
