import cv2
import pytesseract
import re

fields_array = [
    ['employer_address', (97, 330), (775, 365)],
    ['employee_address', (787, 330), (1494, 365)],
    ['employer_PAN', (99, 444), (545, 480)],
    ['employer_TAN', (557, 441), (1008, 480)],
    ['employee_PAN', (1019, 441), (1251, 480)],
    ['assessment_year', (787, 545), (1143, 649)],
    ['employment_from_date', (1150, 600), (1320, 649)], 
    ['employment_to_date', (1328, 601), (1499, 649)],
    ['tax_quarter', (95, 812), (390, 850)],
    ['tax_receipt', (398, 812), (706, 850)],
    ['tax_salary', (715, 812), (933, 850)], 
    ['tax_deducted', (940, 812), (1245, 850)],    
    ['tax_deposited', (1252, 812), (1496, 850)],  
    ['sign_place', (301, 1637), (777, 1677)], 
    ['sign_date', (301, 1686), (777, 1725)]] 


def clear_text(text):
    result = re.search(r'[A-Za-z0-9\-, ]+', text)
    return result.group() if result else ''
    
    
def extract_text(image):

    output = {}
    
    for field in fields_array:
        
        # Extract Field Details
        field_name = field[0]
        (x_tl, y_tl) = field[1]
        (x_bl, y_br) = field[2]
        
        # Extract field roi 
        roi = image[y_tl:y_br, x_tl:x_bl]
        
        # OCR on ROI
        text = pytesseract.image_to_string(roi)
        text = text.replace('\n', '') #clear_text(text)
        
        cv2.rectangle(image, (x_tl, y_tl), (x_bl, y_br), (0, 255, 0), 3 ) 
        cv2.putText(image, text, (x_tl, y_tl - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 3)
        
        # Add to output dictionary
        output[field_name] = text
     
    cv2.imshow('Image', image)
    cv2.waitKey(0)   
    return output