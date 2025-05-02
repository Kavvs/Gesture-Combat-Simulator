import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Marvel Gesture Combat Simulator")

        # Load character image
        self.player_image = pygame.image.load("assets/sprites/player.png").convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (150, 150))
        self.player_pos = [325, 225]

        # Load sounds
        self.sounds = {
            "fist": pygame.mixer.Sound("assets/sounds/punch.wav"),
            "open_palm": pygame.mixer.Sound("assets/sounds/shield.wav"),
            "point": pygame.mixer.Sound("assets/sounds/teleport.wav")
        }

    def trigger_power(self, gesture):
        if gesture in self.sounds:
            self.sounds[gesture].play()
        
        # Visual effect or action placeholder
        print(f"[Game] Power activated: {gesture}")

        # (Optional) Display image in pygame window
        self.screen.fill((0, 0, 0))  # Clear screen
        self.screen.blit(self.player_image, self.player_pos)
        pygame.display.flip()
