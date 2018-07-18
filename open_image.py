"""
Docstring
"""

import cv2


def load_image(img):
    """Press "k" for quit

    :param img: Image to be charged
    :type img: String
    """

    #import numpy as np
    #import matplotlib.pyplot as plt

    image = cv2.imread(img, 0)

    # plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.show()

    cv2.imshow('imagem', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


load_image('pastor_branco_s.jpg')
