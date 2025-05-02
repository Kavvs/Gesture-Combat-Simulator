# import cv2
# import pygame
# import pyttsx3
# from vision.gesture_detector import detect_gesture
# from game.engine import GameEngine

# # Init TTS and Sound
# engine = pyttsx3.init()
# pygame.mixer.init()
# pygame.mixer.music.load("assets/sounds/bgm.mp3")
# pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1)

# # Camera
# cap = cv2.VideoCapture(0)
# game = GameEngine()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)
#     gesture = detect_gesture(frame)

#     if gesture:
#         game.handle_gesture(gesture)
#         engine.say(f"{gesture} activated")
#         engine.runAndWait()

#     cv2.imshow("Gesture Combat", frame)
#     if cv2.waitKey(1) & 0xFF == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

# # main.py
# import cv2
# import pygame
# from vision.gesture_detector import detect_gesture
# from game.engine import Game

# pygame.init()
# game = Game()

# cap = cv2.VideoCapture(0)

# try:
#     while True:
#         success, frame = cap.read()
#         if not success:
#             continue

#         gesture = detect_gesture(frame)

#         if gesture == "fist":
#             game.punch()
#         elif gesture == "palm":
#             game.activate_shield()
#         elif gesture in ["rock"]:
#             game.teleport()

#         game.update_screen()
#         game.clock.tick(60)

#         # Show webcam with hand detection
#         cv2.imshow("Gesture Detection", frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

# except KeyboardInterrupt:
#     print("Game interrupted.")

# finally:
#     cap.release()
#     cv2.destroyAllWindows()
#     pygame.quit()

import cv2
import pygame
from vision.gesture_detector import detect_gesture
from game.engine import Game

cap = cv2.VideoCapture(0)
pygame.init()
game = Game()

try:
    while True:
        success, frame = cap.read()
        if not success:
            continue

        gesture = detect_gesture(frame)

        if gesture == "fist":
            game.punch()
        elif gesture == "namaste":
            game.activate_shield()
        elif gesture == "call_me":
            game.teleport()
        elif gesture == "rock":
            game.superpower()
        elif gesture == "victory":
            game.teleport()
        elif gesture == "thumbs_up":
            game.toggle_pause()
        elif gesture == "thumbs_down":
            game.toggle_pause()

        game.update_screen()
        game.clock.tick(60)

        cv2.imshow("Gesture Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Game interrupted.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()
