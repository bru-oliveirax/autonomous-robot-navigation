import os
from dotenv import load_dotenv
load_dotenv()
import cv2

video = cv2.VideoCapture()
cam = os.getenv("IP_WEBCAM")
video.open(cam)

cv2.namedWindow("testing!", cv2.WINDOW_NORMAL)

while True:
    check, img = video.read()
    cv2.imshow("testing!", img)
    key = cv2.waitKey(1)
    if key == ord('q'): 
        break