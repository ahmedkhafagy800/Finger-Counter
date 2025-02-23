# Hand Tracking and Finger Counter

## Overview
This project utilizes OpenCV and the **MediaPipe Hands** model to detect a hand in a live camera feed and count the number of extended fingers. MediaPipe provides a robust and efficient solution for real-time hand tracking by detecting and analyzing hand landmarks.

## Project Structure
📂 Hand-Tracking-Finger-Counter
│   ├── Hand_Track.py → Handles hand detection and landmark extraction
│   ├── Counter.py → Uses Hand_Track.py to count the number of extended fingers
│   ├── README.md → Project documentation
│   ├── luca1.jpg
│   ├── luca2.jpg
│   ├── luca3.jpg
│   ├── peter-cat.jpg

perl
Copy
Edit

## Installation
Make sure you have the required dependencies installed:
```bash
pip install opencv-python mediapipe
Usage
Run Hand Tracking (Optional for testing hand detection):

bash
Copy
Edit
python Hand_Track.py
Run Finger Counting:

bash
Copy
Edit
python Counter.py
Features
✅ Modular Code: Hand_Track.py for hand tracking, Counter.py for finger counting.
✅ Real-time FPS Calculation for performance monitoring.
✅ Hand Landmark Extraction and visualization.
✅ Finger Counting Logic using MediaPipe Hand Landmarks.
✅ Error Handling for missing hands.

Future Enhancements
 Add gesture recognition (e.g., thumbs up, peace sign).
 Improve accuracy for different hand orientations.
 Implement multi-hand tracking.
