# Hand Tracking and Finger Counter

## Overview

This project utilizes **OpenCV** and the **MediaPipe Hands** model to detect hands in a live camera feed and count the number of extended fingers. MediaPipe offers a robust and efficient solution for real-time hand tracking by detecting and analyzing hand landmarks.

---

## Project Structure

- **Hand_Track.py**: Handles hand detection and landmark extraction.
- **Counter.py**: Uses `Hand_Track.py` to count the number of extended fingers.

---

## Dependencies

Ensure the following Python libraries are installed:

```bash
pip install opencv-python mediapipe

Features
✅ Modular Code: Hand_Track.py for hand tracking, Counter.py for finger counting.

✅ Real-time FPS Calculation for performance monitoring.

✅ Hand Landmark Extraction and Visualization.

✅ Finger Counting Logic using MediaPipe Hand Landmarks.

✅ Error Handling for missing hands.
