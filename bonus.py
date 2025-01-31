import random
import pygame

GRAVITY = 2

ice = pygame.image.load("pictures/fruits/ice.png")
bomb = pygame.image.load("pictures/fruits/bomb.png")
bonus = [ice, bomb]

class Bonus:
    def __init__(self):
        self.x = random.randint(100,600)
        self.y = 600
        self.vitesse_x = random.randint(-15,15)
        self.vitesse_y = random.randint(-50, -35) 
        self.image = random.choice(bonus)
    
    def update(self):
        self.vitesse_y += GRAVITY 
        self.x += self.vitesse_x
        self.y += self.vitesse_y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))