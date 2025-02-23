import cv2
import time
import os
import Hand_Track as htm

wCam, hCam = 1000, 780
pTime = 0

cap = cv2.VideoCapture(0)  # 0 for the default webcam
cap.set(3, wCam)  # Set width
cap.set(4, hCam)  # Set height

path = "number"
myList = os.listdir(path)
fullPath = [cv2.imread(f'{path}/{itr}') for itr in myList]

detector = htm.handDetector(min_detect_confid=0.75)
tipIds = [4, 8, 12, 16, 20]  # Landmark IDs for fingertips: [thumb, index, middle, ring, pinky]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHand(img)
    lmlist = detector.findPos(img)

    if len(lmlist) != 0:
        fingers = []

        # Thumb (Check x-coordinate for thumb)
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0] - 1][1]:  # Compare x-coordinate
            fingers.append(1)  # Thumb is open
        else:
            fingers.append(0)  # Thumb is closed

        # Other Fingers (Check y-coordinate for index, middle, ring, and pinky)
        for id in range(1, 5):  # Loop through index (1), middle (2), ring (3), pinky (4)
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id] - 2][2]:  # Compare y-coordinate
                fingers.append(1)  # Finger is open
            else:
                fingers.append(0)  # Finger is closed

        #print(fingers)  # Print finger states: [thumb, index, middle, ring, pinky]
        totalFingers = fingers.count(1)
        print(totalFingers)

        h, w, c = fullPath[totalFingers-1].shape
        # img = cv2.flip(img, 1)
        img[0:h, 0:w] = fullPath[totalFingers-1]

        cv2.rectangle(img, (20, 255), (170, 425), (0, 255, 0))
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f"FPS: {int(fps)}", (470, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



        