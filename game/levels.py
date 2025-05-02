import pygame

def load_level(name):
    return Level(name)

class Level:
    def __init__(self, name):
        self.name = name
        self.bg = pygame.Surface((800, 600))
        self.bg.fill((30, 30, 30))

    def render(self, screen):
        screen.blit(self.bg, (0, 0))