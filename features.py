import cv2
import numpy as np

def generateHomography(src_img, dst_img):
    detector = cv2.ORB_create()
    k1, d1 = detector.detectAndCompute(src_img, None)
    k2, d2 = detector.detectAndCompute(dst_img, None)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = sorted(matcher.match(d1, d2), key=lambda x: x.distance)

    src_pts = np.float32([k1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([k2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    return H, mask
