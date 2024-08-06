from imutils import paths
import cv2
import numpy as np

def loadImages(path, resize):
    image_path = sorted(list(paths.list_images(path)))
    list_image = []
    for _, j in enumerate(image_path):
        image = cv2.imread(j)
        if resize == 1:
            image = cv2.resize(image, (int(image.shape[1] / 4), int(image.shape[0] / 4)))
        list_image.append(image)
    return list_image

def trim(frame):
    if not np.sum(frame[0]):
        return trim(frame[1:])
    if not np.sum(frame[-1]):
        return trim(frame[:-2])
    if not np.sum(frame[:, 0]):
        return trim(frame[:, 1:])
    if not np.sum(frame[:, -1]):
        return trim(frame[:, :-2])
    return frame

def padding(img, top, bottom, left, right):
    border = cv2.copyMakeBorder(img, top=top, bottom=bottom, left=left, right=right, borderType=cv2.BORDER_CONSTANT)
    return border
