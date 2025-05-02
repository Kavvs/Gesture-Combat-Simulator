# from game.powers import Punch, Shield, Teleport
# from game.enemies import Enemy
# import pygame

# class GameEngine:
#     def __init__(self):
#         self.enemy = Enemy()
#         self.punch = Punch()
#         self.shield = Shield()
#         self.teleport = Teleport()

#     def handle_gesture(self, gesture):
#         if gesture == "punch":
#             self.punch.activate()
#             self.enemy.hit()
#         elif gesture == "shield":
#             self.shield.activate()
#         elif gesture == "teleport":
#             self.teleport.activate()

import pygame
import cv2
import sys
import numpy as np
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Gesture Combat Simulator")
        self.clock = pygame.time.Clock()

        # Load background and music
        self.background = pygame.image.load("assets/backgrounds/theme.png").convert()
        self.background = pygame.transform.scale(self.background, (800, 600))
        pygame.mixer.music.load("assets/audio/bgm.mp3")
        pygame.mixer.music.play(-1)

        # Load sprites
        self.player = pygame.image.load("assets/sprites/player.png").convert_alpha()
        self.enemy = pygame.image.load("assets/sprites/enemy.png").convert_alpha()
        self.shield_sprite = pygame.image.load("assets/sprites/shield.png").convert_alpha()
        self.fist_sprite = pygame.image.load("assets/sprites/fist.png").convert_alpha()
        self.teleport_sprite = pygame.image.load("assets/sprites/teleport.gif").convert_alpha()

        # Load sounds
        self.punch_sound = pygame.mixer.Sound("assets/sounds/punch.wav")
        self.shield_sound = pygame.mixer.Sound("assets/sounds/shield.wav")
        self.teleport_sound = pygame.mixer.Sound("assets/sounds/teleport.wav")

        self.player_pos = [400, 300]
        self.enemy_pos = [200, 300]
        self.shield_active = False
        self.show_fist = False
        self.show_teleport = False
        self.action_timer = 0

        # Effects
        self.fog_overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
        self.create_fog()

    def create_fog(self):
        for _ in range(100):
            x, y = random.randint(0, 800), random.randint(0, 600)
            radius = random.randint(10, 30)
            pygame.draw.circle(self.fog_overlay, (200, 200, 255, 10), (x, y), radius)

    def update_screen(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.fog_overlay, (0, 0))
        self.screen.blit(self.enemy, self.enemy_pos)
        self.screen.blit(self.player, self.player_pos)

        if self.shield_active:
            self.screen.blit(self.shield_sprite, (self.player_pos[0] - 20, self.player_pos[1] - 20))

        if self.show_fist:
            self.screen.blit(self.fist_sprite, (self.player_pos[0] + 50, self.player_pos[1]))

        if self.show_teleport:
            self.screen.blit(self.teleport_sprite, (self.player_pos[0], self.player_pos[1] - 50))

        pygame.display.flip()

        # Hide effects after 0.5 seconds
        if self.action_timer > 0:
            self.action_timer -= 1
        else:
            self.show_fist = False
            self.show_teleport = False

    def punch(self):
        self.punch_sound.play()
        self.show_fist = True
        self.action_timer = 30
        print("👊 Punch triggered!")

    def teleport(self):
        self.teleport_sound.play()
        self.show_teleport = True
        self.action_timer = 30
        new_x = random.randint(100, 700)
        new_y = random.randint(100, 500)
        self.player_pos = [new_x, new_y]
        print("✨ Teleported to new location!")

    def activate_shield(self):
        self.shield_active = True
        self.shield_sound.play()
        print("🛡️ Shield activated!")

    def superpower(self):
        print("🔥 Superpower unleashed!")

    def toggle_pause(self):
        print("⏸️ Game paused/resumed.")

    def heal(self):
        print("💖 Healed!")

    def respawn(self):
        self.player_pos = [400, 300]
        print("🔄 Respawned!")

    def run(self, cap):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.update_screen()
            self.clock.tick(60)

        cap.release()
        pygame.quit()
        sys.exit()





