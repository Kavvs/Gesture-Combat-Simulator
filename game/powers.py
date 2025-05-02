import pygame

class Punch:
    def activate(self):
        sound = pygame.mixer.Sound("assets/sounds/punch.wav")
        sound.play()
        print("Punch power used!")

class Shield:
    def activate(self):
        sound = pygame.mixer.Sound("assets/sounds/shield.wav")
        sound.play()
        print("Shield activated!")

class Teleport:
    def activate(self):
        sound = pygame.mixer.Sound("assets/sounds/teleport.wav")
        sound.play()
        print("Teleported to new location!")
