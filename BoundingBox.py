# Here's a Python script that detects a syringe in a live video feed, draws a bounding box around it,
# and checks the confidence level to determine if it is indeed a syringe. 
# This example uses the tensorFlow model for object detection.

# In practice this code would need to be optimized for fast processing time to quickly detect any 
# errors in administration to prevent health risks, as well as decreasing size of the entire algorithim
# to implement on a small wearable. 

import cv2
import numpy as np
import tensorflow as tf

# Load the TFLite model
interpreter = tf.lite.Interpreter(model_path="yolov8n.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess_image(image):
    # Resize the image to the model's input size (e.g., 416x416 was used)
    image_resized = cv2.resize(image, (416, 416))
    # Normalize pixel values to [0, 1] - helps with reducing algorithim bias
    image_normalized = image_resized / 255.0
    # Expand dimensions to match model input shape
    return np.expand_dims(image_normalized, axis=0).astype(np.float32)

def draw_bounding_boxes(frame, boxes, class_ids, confidences):
    for i in range(len(boxes)):
        if confidences[i] > 0.5:  # Confidence threshold
            x1, y1, x2, y2 = boxes[i]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = f"Syringe: {confidences[i]:.2f}"
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

def main():
    # Initialize video capture (or use an image)
    cap = cv2.VideoCapture(0)  # Change to your camera index or use a video file

    while True:
        ret, frame = cap.read()
        if not ret:
            break # End frame

        # Preprocess the image
        input_image = preprocess_image(frame)

        # Set the input tensor
        interpreter.set_tensor(input_details[0]['index'], input_image)

        # Run inference
        interpreter.invoke()

        # Get output tensors
        boxes = interpreter.get_tensor(output_details[0]['index'])[0]  # Bounding boxes
        confidences = interpreter.get_tensor(output_details[1]['index'])[0]  # Confidence scores
        class_ids = interpreter.get_tensor(output_details[2]['index'])[0]  # Class IDs

        # Draw bounding boxes on the frame
        draw_bounding_boxes(frame, boxes, class_ids, confidences)

        # Display the resulting frame
        cv2.imshow('Syringe Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Goes to Optical Character Recognition, picks out the highest confidence text frame and reads the information

# Performs text recognition

# Volume Assessment to detect amount of anesthesia adminisitered (Comparing before and after frames of syringe)

# Data (Text Recognition and Volume Assesment) is reported to Physician and EMR.


