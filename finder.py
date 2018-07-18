"""Docstring

"""
import cv2
#import numpy as np


def find_in_face(haarcascade, rec=False):
    """Press 'k' for quit

    """
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(haarcascade)

    cap = cv2.VideoCapture(0)

    if rec:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))

    while True:
        _, original = cap.read()
        gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (fx, fy, fw, fh) in faces:
            cv2.rectangle(original, pt1=(fx, fy), pt2=(
                fx+fw, fy+fh), color=(0, 0, 255), thickness=2)
            roi_gray = gray[fy:fy+fh, fx:fx+fw]
            roi_color = original[fy:fy+fh, fx:fx+fw]

            smiles = smile_cascade.detectMultiScale(roi_gray)
            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(roi_color, pt1=(sx, sy), pt2=(
                    sx+sw, sy+sh), color=(255, 0, 0), thickness=2)

        if rec:
            out.write(original)
        cv2.imshow('Image', original)

        if cv2.waitKey(1) & 0xFF == ord('k'):
            break

    cap.release()
    if rec:
        out.release()
    cv2.destroyAllWindows()


find_in_face('haarcascade_eye.xml', rec=False)
