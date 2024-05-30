import cv2
import numpy
import os
from matplotlib import pyplot as plot

img = None
gray = None
blockSize = 2
sobelAperture = 23
freeParam = 40
detectThresh = 10

def readImage():
    global gray, img

    img = cv2.imread('./images/5_of_diamonds.png')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def calcCorners():
    global gray, img, blockSize, sobelAperture, freeParam, detectThresh

    k = 0.001*freeParam

    dst = cv2.cornerHarris(gray, blockSize, sobelAperture, k)

    img[dst > 0.001 * detectThresh * dst.max()] = [0, 255, 0]

def processHarrisCorners():
    global img

    readImage()

    calcCorners()

    cv2.imshow("Harris Corners", img)


def updateBlockSize(sliderPosition = 0):
    # Event handler for moving block size trackbar position

    global blockSize

    blockSize = cv2.getTrackbarPos('blockSize', 'Harris Corners')

    processHarrisCorners()

def updateSobelAperture(sliderPosition = 0):
    # Event handler for sobel aperature bar
    global sobelAperture

    sobelAperture = cv2.getTrackbarPos('sobelAperture', "Harris Corners")

    if sobelAperture % 2 == 0:
        sobelAperture += 1
    if sobelAperture > 31:
        sobelAperture = 31
    if sobelAperture < 3:
        sobelAperture = 3

    processHarrisCorners()


def updateFreeParam(sliderPosition = 0):
    # Event handler free param bar
    global freeParam

    freeParam = cv2.getTrackbarPos('freeParam', 'Harris Corners')

    processHarrisCorners()

def updateDetectionThresh(sliderPosition = 0):
    # Event handler detection thresh bar

    global detectThresh

    detectThresh = cv2.getTrackbarPos('det Thresh', 'Harris Corners')

    processHarrisCorners()

def detectHarrisCorners():
    global blockSize, sobelAperture, freeParam, detectThresh

    cv2.namedWindow("Harris Corners")

    cv2.createTrackbar('blockSize', 'Harris Corners', blockSize, 10, updateBlockSize)
    cv2.setTrackbarMin('blockSize', 'Harris Corners', 1)

    cv2.createTrackbar('sobelAperture', 'Harris Corners', sobelAperture, 31, updateSobelAperture)
    cv2.setTrackbarMin('sobelAperture', 'Harris Corners', 3)

    cv2.createTrackbar('freeParam', 'Harris Corners', freeParam, 100, updateFreeParam)
    cv2.setTrackbarMin('freeParam', 'Harris Corners', 1)

    cv2.createTrackbar('det Thresh', 'Harris Corners', detectThresh, 100, updateDetectionThresh)
    cv2.setTrackbarMin('det Thresh', 'Harris Corners', 1)

    updateBlockSize()
    updateSobelAperture()
    updateFreeParam()
    updateDetectionThresh()

    cv2.waitKey()

    cv2.destroyAllWindows()
