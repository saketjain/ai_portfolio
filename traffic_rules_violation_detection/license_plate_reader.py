import cv2
import pytesseract
import numpy as np
from config import base_path

plate_cascade = cv2.CascadeClassifier(base_path + '/assets/xmls/haarcascade_russian_plate_number.xml')


def get_license_plate_number(car_image):
    number = ''

    if car_image is None or car_image.size < 1000:
        return ''

    plates = plate_cascade.detectMultiScale(car_image, 1.1, 4)
    for (x, y, w, h) in plates:
        temp = car_image[y:y+h, x:x+w]
        result= detectNumber(temp).strip()
        result = result.encode("ascii", errors="ignore").decode()
        if "?" not in result and len(result) > 4:
            number = result
    return number.upper()


def detectNumber(image):
    (h, w, _) = image.shape

    aspectRatio = h/w

    w = w*1.2
    h = w * aspectRatio

    image = cv2.resize(image, (int(w), int(h)))

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cntrs, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the largest contour by area
    largest_contour = max(cntrs, key=cv2.contourArea)

    # Approx the contours
    (x, y, w, h) = cv2.boundingRect(largest_contour)
    image = image[y:y+h, x:x+w]

    result = pytesseract.image_to_string(image, config='--psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    return result