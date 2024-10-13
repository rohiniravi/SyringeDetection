# Here's a Python script that detects a syringe in a live video feed, draws a bounding box around it,
# and checks the confidence level to determine if it is indeed a syringe. 
# This example uses the YOLOv8 model for object detection.

# In practice this code would need to be optimized for fast processing time to quickly detect any 
# errors in administration to prevent health risks, as well as decreasing size of the entire algorithim
# to implement on a small wearable. 

# Potential solutions for wearable algorithims - tinyML, YOLOv8n (nano), optimized for efficiency and being lightweight.
# Potential Microcontrollers - STM32F4 Series or STM32WB Series for High Speed processing and wireless communication. 

import cv2
import torch

# Load the trained model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=Syringe_Detect.pt', force_reload=True)

# Initialize video capture from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        Break # End of Video

# Syringe Detection
    
    # Perform object detection on obtained frame
    results = model(frame)

    # Process results
    for box in results.xyxy[0]:  # Iterate through detected objects
        x1, y1, x2, y2, conf, cls = box  # Get bounding box coordinates and confidence
        
        # Check if detected object is a syringe
        if int(cls) == 0:  # Class ID is the object category
            # Draw bounding box and label on the frame
            label = f"Syringe: {conf:.2f}"
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the resulting frame
    cv2.imshow('Syringe Detection', frame)

# Goes to Optical Character Recognition, picks out the highest confidence text frame and reads the information

# Performs text recognition

# Volume Assessment to detect amount of anesthesia adminisitered (Comparing before and after frames of syringe)

# Data (Text Recognition and Volume Assesment) is reported to Physician and EMR.


