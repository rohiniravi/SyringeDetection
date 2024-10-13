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

    # Goes to Optical Character Recognition Step
