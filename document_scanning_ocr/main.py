import cv2
from align_images import align_images
from extract_text import extract_text
import matplotlib.pyplot as plt

base_path = './document_scanning_ocr'

image = cv2.imread(base_path + '/assets/Form2.jpg')
template = cv2.imread(base_path + '/assets/Template.png')

print(template.shape)

aligned = align_images(image, template)

output = extract_text(aligned)

print(output)