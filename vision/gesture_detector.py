# import cv2
# import mediapipe as mp

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
# draw = mp.solutions.drawing_utils

# def detect_gesture(frame):
#     h, w, _ = frame.shape
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     result = hands.process(rgb)
#     landmarks = []

#     if result.multi_hand_landmarks:
#         for hand in result.multi_hand_landmarks:
#             draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
#             for lm in hand.landmark:
#                 landmarks.append((int(lm.x * w), int(lm.y * h)))

#     # Gesture logic
#     if landmarks:
#         thumb_tip = landmarks[4]
#         index_tip = landmarks[8]
#         pinky_tip = landmarks[20]
#         wrist = landmarks[0]

#         def dist(a, b):
#             return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

#         if dist(index_tip, wrist) < 40:
#             return "punch"
#         elif dist(thumb_tip, pinky_tip) < 50:
#             return "shield"
#         elif index_tip[1] < thumb_tip[1]:
#             return "teleport"
#     return None

# vision/gesture_detector.py
import cv2
import mediapipe as mp
import joblib
import numpy as np

model = joblib.load("gestures/model.pkl")  # Make sure it's retrained properly

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def detect_gesture(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    gesture = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            landmarks = []
            for lm in hand_landmarks.landmark:
                landmarks.append([lm.x, lm.y])
            landmarks = np.array(landmarks).flatten().reshape(1, -1)
            gesture = model.predict(landmarks)[0]

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return gesture

import os

model_path = "gestures/model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError("❌ model.pkl not found! Please train or re-save it.")

try:
    model = joblib.load(model_path)
except EOFError:
    raise EOFError("❌ model.pkl is empty or corrupted. Retrain the model and save it again.")


