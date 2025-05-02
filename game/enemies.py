import pygame

class Enemy:
    def __init__(self):
        self.health = 100

    def hit(self):
        self.health -= 10
        print(f"Enemy hit! Health: {self.health}")
