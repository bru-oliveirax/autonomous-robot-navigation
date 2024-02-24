import os
from dotenv import load_dotenv
load_dotenv()
import numpy as np
import cv2


# Defining params
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)

for id in range(10):
    marker_id = id
    marker_size = 250

    # Creating an empty image
    marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)

    # Generating the image
    cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size, marker_image)

    # Saving the image
    output_path = os.path.join(os.getenv("MARKERS"), f"marker_{marker_id}.png")
    cv2.imwrite(output_path, marker_image)

'''
cv2.imshow(f"marker_{marker_id}.png", marker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''