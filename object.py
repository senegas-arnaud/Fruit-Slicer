import pygame
import random


apple = pygame.image.load("pictures/fruits/apple.png")
banana = pygame.image.load("pictures/fruits/banana.png")
kiwi = pygame.image.load("pictures/fruits/kiwi.png")
lime = pygame.image.load("pictures/fruits/lime.png")
orange = pygame.image.load("pictures/fruits/orange.png")
strawberry = pygame.image.load("pictures/fruits/strawberry.png")
watermelon = pygame.image.load("pictures/fruits/watermelon.png")

fruits = [apple, banana, kiwi, lime, orange, strawberry, watermelon]
GRAVITY = 2

class Objet:
    def __init__(self):
        self.x = random.randint(100,600)
        self.y = 600
        self.vitesse_x = random.randint(-15,15)
        self.vitesse_y = random.randint(-50, -35) 
        self.image = random.choice(fruits)
    
    def update(self):
        self.vitesse_y += GRAVITY 
        self.x += self.vitesse_x
        self.y += self.vitesse_y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))