import cv2
import numpy as np

def get_hsv_range(bgr, sensitivity=15):
    """
    Convert an RGB color to a low and high HSV range for color detection.

    Args:
        r (int): Red value (0–255)
        g (int): Green value (0–255)
        b (int): Blue value (0–255)
        sensitivity (int): Range to extend hue (default 15)

    Returns:
        Tuple[np.array, np.array]: Lower and upper HSV bounds
    """
    # Convert RGB to HSV using OpenCV (expects BGR)
    bgr_color = np.uint8([[bgr]])  # OpenCV uses BGR
    hsv_color = cv2.cvtColor(bgr_color, cv2.COLOR_BGR2HSV)[0][0]

    # Extract hue and build lower/upper bounds
    h, s, v = hsv_color
    lower = np.array([max(h - sensitivity, 0), 50, 50])
    upper = np.array([min(h + sensitivity, 179), 255, 255])

    return lower, upper