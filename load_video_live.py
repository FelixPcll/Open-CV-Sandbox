"""Docstring

"""

# import numpy as np
import cv2


def load_live():
    """Press "k" for quit

    """

    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('Processed', gray)
        cv2.imshow('Original', frame)
        if cv2.waitKey(1) & 0xFF == ord('k'):
            break

    cap.release()
    cv2.destroyAllWindows()


def load_live_edge():
    """Press "k" for quit

    """

    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edge_50_50 = cv2.Canny(gray, 50, 50)

        cv2.imshow('Original_gray', gray)
        cv2.imshow('edge_50_50', edge_50_50)

        if cv2.waitKey(1) & 0xFF == ord('k'):
            break

    cap.release()
    cv2.destroyAllWindows()


load_live_edge()
