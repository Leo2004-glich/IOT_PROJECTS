#Group 6

import cv2
import pytesseract
import pyttsx3
import RPi.GPIO as GPIO
import os

# Initialize the camera
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set width to 640 pixels
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set height to 480 pixels

# Set up Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set up GPIO
BUTTON_PIN_CAPTURE = 40  # Example GPIO pin for capturing image
BUTTON_PIN_QUIT = 32  # Example GPIO pin for quitting
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUTTON_PIN_CAPTURE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_QUIT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to perform OCR and convert text to speech
def process_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform OCR on the grayscale frame
    text = pytesseract.image_to_string(gray)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()

# Main loop
while True:
    ret, frame = camera.read()

    # Check for capture button press
    if GPIO.input(BUTTON_PIN_CAPTURE) == GPIO.LOW:
        process_frame(frame)

    # Check for quit button press
    if GPIO.input(BUTTON_PIN_QUIT) == GPIO.LOW:
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Check for key press (press 'q' to quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
camera.release()
cv2.destroyAllWindows()
GPIO.cleanup()  # Clean up GPIO
