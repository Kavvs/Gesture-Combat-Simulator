import cv2
import mediapipe as mp
import numpy as np
import csv
import os

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

gesture_name = input("🖐️ Enter gesture label (e.g. fist, thumbs_up): ")
save_path = "data/gesture_data.csv"

cap = cv2.VideoCapture(0)
data = []

print(f"🎥 Collecting gesture: {gesture_name} ... Press 'q' to stop.\n")

try:
    while True:
        success, frame = cap.read()
        if not success:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                landmarks = [[lm.x, lm.y] for lm in hand_landmarks.landmark]
                flat = np.array(landmarks).flatten().tolist()
                data.append([gesture_name] + flat)

        cv2.imshow("Gesture Collector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
    print(f"📝 Collected {len(data)} samples for '{gesture_name}'")

    os.makedirs("data", exist_ok=True)
    with open(save_path, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
