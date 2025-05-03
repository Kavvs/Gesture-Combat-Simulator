# Marvel-Inspired Gesture Combat Simulator 🦾

# 🕹️ Gesture-Controlled Gothic Fighter Game
This is an AI-powered gesture-based action game built using Python, OpenCV, and Pygame. It features a gothic-themed combat environment where a player can perform real-time battle actions using hand gestures via webcam.

## 🖼 Preview
<p align="center">
  <img src="gesture_combat_simulator MAIN THEME.png" width="500"><br>
  <em>Gothic UI with Punch, Shield, Teleport and Superpower actions</em>
</p>

# ⚔️ Features
🎮 Real-time gesture detection using webcam (via vision/gesture_detector.py)

🧛‍♂️ Gothic animated background with ambient aesthetics

🥊 Punch using fist gesture

🛡 Activate shield with palm/namaste gesture

✨ Teleport using victory gesture (encircled by animated teleportation ring)

🚀 Start game with thumbs_up, pause/stop with thumbs_down

🎯 Enemy is centered, and player always faces & targets the enemy

🔊 Integrated sound effects for actions (punch, shield, teleport)

⏱ Smooth 60 FPS rendering

This game uses your webcam and MediaPipe to detect hand gestures and trigger Marvel-style powers like:

- 👊 Punch
- 🛡️ Shield
- 🌀 Teleport

fist → do ✊ and move a bit (collect at least 100 samples)

thumbs_up → do 👍 gesture

namaste → bring both palms together 🙏

call_me → 🤙 thumb and pinky

rock → 🤘 (index and pinky up)

victory → ✌️

thumbs_down → 👎

## 👣 Steps to Run

1. Clone/download the repo
2. Install Python packages:

```bash
pip install pygame opencv-python mediapipe pyttsx3

