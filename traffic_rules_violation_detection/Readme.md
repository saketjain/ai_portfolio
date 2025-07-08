# 🚦 AI Traffic Rules Violation Detection System

An end-to-end AI system that automatically detects **vehicles violating red lights** and extracts their **registration numbers from license plates** using computer vision.

This project leverages object detection, traffic signal analysis, and automatic number plate recognition (ANPR) to assist in smart city surveillance and law enforcement automation.

---

## Features

- **Vehicle Detection**: Identifies moving vehicles approaching intersections.
- **Red Light Violation Detection**: Detects vehicles that cross the stop line when the traffic signal is red.
- **License Plate Recognition**: Extracts vehicle registration numbers from license plates using OCR.
- **Violation Logging**: Stores time-stamped violation events with plate numbers and evidence images.

---

## How It Works

1. **Video Input** (Live camera feed or pre-recorded footage)
2. **Traffic Signal Status Detection** (based on signal color detection or external input)
3. **Vehicle Tracking** across frames using YOLO or DeepSORT
4. **Violation Detection** when vehicle crosses the stop line during red signal
5. **License Plate Detection & OCR** using OpenCV and Tesseract
6. **Data Logging**: Violation details saved with license plate, timestamp, and image evidence.

---

## Tech Stack

| Component         | Technology             |
|------------------|------------------------|
| Object Detection | YOLOv5 / YOLOv8        |
| License Plate OCR| EasyOCR / Tesseract OCR|
| Image Processing | OpenCV                 |
---

## Project Structure

```bash
.
├── models/                   # Pre-trained weights for detection
├── assets/                   # Sample videos and test frames
├── red_light_detector.py     # Detects red light status
├── vehicle_tracker.py        # Tracks vehicles and stop line crossing
├── license_plate_reader.py   # OCR module for plate recognition
├── main.py                   # Pipeline script
├── requirements.txt
└── README.md
