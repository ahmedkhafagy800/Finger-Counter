import cv2
import mediapipe as mp
import time
import warnings
warnings.filterwarnings("ignore")

class handDetector():
    def __init__(self, mode=False, mxHands=1, modelComp=1, min_detect_confid=0.7, min_track_confid=0.5):
        if modelComp not in [0, 1, 2]: # model complexity has 3 values, 2 which balance between speed and accuracy to capture the hand
            raise ValueError("modelComp should be 0, 1, or 2.")
        self.mode = mode
        self.mxHands = mxHands
        self.modelComp = modelComp  # This should be an integer (0, 1, or 2)
        self.min_detect_confid = min_detect_confid
        self.min_track_confid = min_track_confid
        self.mpHands = mp.solutions.hands  # Initializes mediapipe hand models
        self.mpDraw = mp.solutions.drawing_utils  # Draw points and connections
        self.hands = self.mpHands.Hands(self.mode, self.mxHands, self.modelComp,
                                        self.min_detect_confid, self.min_track_confid)

    # Find hands and draw landmarks on the image
    def findHand(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert image to RGB
        self.result = self.hands.process(imgRGB)  # Process the frame for hand landmarks

        if self.result.multi_hand_landmarks:  # Check if any hand landmarks are detected
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    landmark_col = self.mpDraw.DrawingSpec(color=(255, 0, 0), thickness=1) #BGR(BLUE, GREEN, RED)
                    connection_col = self.mpDraw.DrawingSpec(color=(0, 0, 255), thickness=1)
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS, landmark_col, connection_col)
        return img

    # Get positions of hand landmarks
    def findPos(self, img, handNo=0, draw=True):
        lmlist = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)  # Convert hand landmarks into pixels
                lmlist.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
        return lmlist



#Main function to capture video and detect hands
def main():
    pTime = 0  # Previous time for FPS calculation
    cTime = 0  # Current time for FPS calculation

    detector = handDetector(modelComp=1)
    cap = cv2.VideoCapture(0)  # Start capture from the default camera (0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            success, img = cap.read()  # Capture the frames from the video
            if not success:
                print("Failed to capture image")
                break
            img = cv2.resize(img, (640, 480))
            img = cv2.flip(img, 1)

            img = detector.findHand(img)
            lmlist = detector.findPos(img)  # Use findPos to get landmark positions
            if len(lmlist) > 0:             # avoid potential indexing error
                print("Landmark 0:", lmlist[0])  # Print the first landmark (if available)

            # Calculate and display FPS
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

            # Display the image
            cv2.imshow("Image", img)

            # Exit condition: Press 'q' to quit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("Program interrupted. Closing resources.")
    finally:
        cap.release()  # Release the video capture object
        cv2.destroyAllWindows()  # Close all OpenCV windows






# Run the main function
if __name__ == "__main__":
    main()



