import pygame
import random
from pygame.locals import *

pygame.init()

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
GRAVITY = 1

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

title_font = pygame.font.SysFont("Arial", 60, italic = True)

apple = pygame.image.load("pictures/fruits/apple.png")
banana = pygame.image.load("pictures/fruits/banana.png")
kiwi = pygame.image.load("pictures/fruits/kiwi.png")
lime = pygame.image.load("pictures/fruits/lime.png")
orange = pygame.image.load("pictures/fruits/orange.png")
strawberry = pygame.image.load("pictures/fruits/strawberry.png")
watermelon = pygame.image.load("pictures/fruits/watermelon.png")

fruits = [apple, banana, kiwi, lime, orange, strawberry, watermelon]


class Fruit:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 600
        self.vitesse_x = random.randint(-10, 10)
        self.vitesse_y = random.randint(-35, -25)
        self.image = random.choice(fruits)
        self.letter = random.choice(alphabet)

    def update(self):
        self.vitesse_y += GRAVITY
        self.x += self.vitesse_x
        self.y += self.vitesse_y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
        text_surface = title_font.render (self.letter, True, YELLOW)
        screen.blit (text_surface, (self.x, self.y))
