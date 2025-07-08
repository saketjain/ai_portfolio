from ultralytics import YOLO
import cv2
from config import base_path
from vehicle_tracker import track_vehicle

# Read the Video
cap = cv2.VideoCapture(base_path + '/assets/videos/traffic_video.mp4')

# Get the frames per second (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)

# Calculate number of frames to skip
frames_to_skip = int(fps * 10)

# Set the position of the video to start after 5 seconds
cap.set(cv2.CAP_PROP_POS_FRAMES, frames_to_skip)

while True:
    
    success, frame = cap.read()
    
    track_vehicle(frame)
 
    cv2.imshow('Traffic', frame)
            
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()    
    
    

