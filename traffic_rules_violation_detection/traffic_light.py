import cv2
from utils import get_hsv_range
import numpy as np

# Use BGR ordering
red_range = get_hsv_range([0, 0, 255]) 
green_range = get_hsv_range([0, 255, 0])
orange_range = get_hsv_range([0, 165, 255])

def traffic_light_color(traffic_light_image):

    red_mask = cv2.inRange(traffic_light_image, red_range[0], red_range[1])
    green_mask = cv2.inRange(traffic_light_image, green_range[0], green_range[1])
    orange_mask = cv2.inRange(traffic_light_image, orange_range[0], orange_range[1])

    red_count = np.count_nonzero(red_mask)
    green_count = np.count_nonzero(green_mask)
    orange_count = np.count_nonzero(orange_mask)

    index = np.argmax([red_count, green_count, orange_count])

    if index == 0:
       color = 'red'
   
    elif index == 1:
       color = 'green'
    else:
       color = 'orange'

    return color