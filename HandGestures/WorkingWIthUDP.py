import cv2
import numpy as np
import mediapipe as mp
import socket

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_x, prev_y = None, None
gesture_state = None

def send_data(message, ip, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode(), (ip, port))

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
                    if dx > 20 and gesture_state != "Left Swipe":
                        print("Left Swipe")
                        gesture_state = "Left Swipe"
                        send_data(gesture_state, "127.0.0.1", 8001)
                    elif dx < -20 and gesture_state != "Right Swipe":
                        print("Right Swipe")
                        gesture_state = "Right Swipe"
                        send_data(gesture_state, "127.0.0.1", 8001)
                    else:
                        gesture_state = None
                        send_data("None", "127.0.0.1", 8001)
                        print("None")
                else:
                    if dy > 20 and gesture_state != "Play":
                        print("Play")
                        gesture_state = "Play"
                        send_data(gesture_state, "127.0.0.1", 8001)
                    elif dy < -20 and gesture_state != "Pause":
                        print("Pause")
                        gesture_state = "Pause"
                        send_data(gesture_state, "127.0.0.1", 8001)
                    else:
                        gesture_state = None
                        send_data("None", "127.0.0.1", 8001)
                        print("None")
            else:
                gesture_state = None
                send_data("None", "127.0.0.1", 8001)
                print("None")
                

            prev_x, prev_y = cx, cy
     
      

     
    cv2.imshow('Hand Gesture Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
