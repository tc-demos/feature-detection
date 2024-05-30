import cv2
import matplotlib.pyplot as plt
import numpy
import os
from matplotlib import pyplot as plot

def orbFinder():

    img0 = cv2.imread('./images/nasa_logo.png', cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread('./images/kennedy_space_center.jpg', cv2.IMREAD_GRAYSCALE)

    orb = cv2.ORB.create()
    kp0, des0 = orb.detectAndCompute(img0, None)
    kp1, des1 = orb.detectAndCompute(img1, None)

    choice = -1
    while choice != 0:

        while choice < 0 or choice > 3:
            print(
"""
Enter choice of matching method:
1. Use brute force method
2. Use k-nearest neighbors (knn) method
3. Use knn matching with radio testing
0: quit            
""")
            choice = int(input('> '))

        if choice == 1:
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
            matches = bf.match(des0, des1)

            matches = sorted(matches, key=lambda x: x.distance)

            img_matches = cv2.drawMatches(img0, kp0, img1, kp1, matches[:25], img1,
                                          flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

            plot.imshow(img_matches)
            plot.show()

            choice = -1

        elif choice == 2:

            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

            pairs_of_matches = bf.knnMatch(des0, des1, k=2)

            pairs_of_matches = sorted(pairs_of_matches, key=lambda x: x[0].distance)

            img_pairs_of_matches = cv2.drawMatchesKnn(img0, kp0, img1, kp1, pairs_of_matches[:25], img1,
                                                      flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

            plot.imshow(img_pairs_of_matches)
            plot.show()

            choice = -1

        elif choice == 3:
            bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
            pairs_of_matches = bf.knnMatch(des0, des1, k=2)
            matches = [x[0] for x in pairs_of_matches
                       if len(x) > 1 and x[0].distance < 0.8 * x[1].distance]

            img_matches = cv2.drawMatches(img0, kp0, img1, kp1, matches[:25], img1,
                                          flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

            plt.imshow(img_matches)
            plt.show()

            choice = -1

        else:
            break

