# Marvel-Inspired Gesture Combat Simulator 🦾

# 🕹️ Gesture-Controlled Gothic Fighter Game
This is an AI-powered gesture-based action game built using Python, OpenCV, and Pygame. It features a gothic-themed combat environment where a player can perform real-time battle actions using hand gestures via webcam.

## 🖼 Preview
<p align="center">
  <img src="https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22gesture_combat_simulator%20MAIN%20THEME.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-05-02T02%3A44%3A07.624Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2Fb87df42c3c22410c%2Fgesture_combat_simulator%20MAIN%20THEME.png%3FExpires%3D1840848248%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DDvWghMbKn04fgRSY--qzHwJM4aJ2O1cJAGWIw2TQjxWmObyA1eeESgPAu1VviEXxtGIilf1uRQ~m7wvoUr21reKK~6uiqR4epY3oaqZFiWxfApasfkGxJH0LjSw5OahXp2jsfKSlmI0-TUjBD1UMAclDkdpxC~ylhTkDjnhKk847SrfQEhD46ekR5gJi82-OYU2fQkcHqrzM5Vq8bp-rr4KjN69J10YpWOOYKCisTcFZRUQfEtHMys3qR9QHERCkc~Owa1XGWnzi6amaTPkqD-7u33WBP8P1DQpfbL9QmthmfYAxZ3zJqe7v3CK4w4RZnHsdTMh7ryHUhaazjdxZ6g__%22%7D" width="500"><br>
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

