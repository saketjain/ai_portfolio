from ultralytics import YOLO
import numpy as np
import math
import cv2
from traffic_light import traffic_light_color
from sort import Sort
from license_plate import get_license_plate_number
from config import base_path

# Read the Video
cap = cv2.VideoCapture(base_path + '/assets/videos/traffic_video.mp4')

# Get the frames per second (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)

# Calculate number of frames to skip
frames_to_skip = int(fps * 10)

# Set the position of the video to start after 5 seconds
cap.set(cv2.CAP_PROP_POS_FRAMES, frames_to_skip)

# Create Model
model = YOLO(base_path + '/yolov8n.pt')
class_names = model.names

# Load the Image mask
mask = cv2.imread(base_path + '/assets/images/mask.png')


# Initailize the object tracker
tracker = Sort(max_age=20)

# Car Ids
car_ids = {}

while True:
    
    success, frame = cap.read()
    
    # Get the ROI using the mask
    region = cv2.bitwise_and(frame, mask)
    
    # Pass the ROI to the model to get results
    results = model(region)
    
    # Initialize the tracker
    detections = []
        
    color = 'green'
    #cv2.line(frame, (700, 900), (1900, 900), (255, 255, 255), 10)   
       
    for result in results:
        boxes = result.boxes
        
        for box in boxes:           

            # Fetch the class
            cls = int(box.cls[0])
            class_name = class_names[cls]
            
            # Fetch the bouding box coordinates
            (x1, y1, x2, y2) = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 
                            
            if (class_name == 'traffic light' and x1 > 1000):
                
                traffic_light_roi = frame[y1:y2+1, x1:x2+1]
                traffic_light_roi = cv2.cvtColor(traffic_light_roi, cv2.COLOR_BGR2HSV)
                color = traffic_light_color(traffic_light_roi)
                cv2.putText(frame, color, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0 , 255), 3) 
                
            if (class_name in ['car']):
                
                # Fetch the confidence
                conf = math.ceil(box.conf[0]*100) / 100                
                detections.append([x1, y1, x2, y2, conf])
    
    
    if len(detections) > 0:
        tracked_cars = tracker.update(np.array(detections))
        for car in tracked_cars:
            x1, y1, x2, y2, car_id  = map(int, car)
            
            if (color == 'red' and 900 < y2 < 920) or car_id in car_ids:
                number = get_license_plate_number(frame[y1:y2, x1:x2])
                number = number if number else car_ids.get(car_id, '')
                car_ids[car_id] = number
                cv2.putText(frame, f"LP: {number}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 3)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)
           
    cv2.imshow('Video1', frame)
            
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()    
    
    

