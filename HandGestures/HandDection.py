import cv2
import numpy as np
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_x, prev_y = None, None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = [(lm.x, lm.y) for lm in hand_landmarks.landmark]
            cx, cy = int(landmarks[9][0] * frame.shape[1]), int(landmarks[9][1] * frame.shape[0])

            if prev_x and prev_y:
                dx, dy = cx - prev_x, cy - prev_y
                if abs(dx) > abs(dy):
                   ''' if dx > 20:
                        print("Right Swipe")
                    elif dx < -20:
                        print("Left Swipe")'''
                if dx > 20:
                    print("Left Swipe")
                elif dx < -20:
                    print("Right Swipe")
                            
            prev_x, prev_y = cx, cy

    cv2.imshow('Hand Gesture Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
