import os
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1250, 750))
background = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/back.png")

banana = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/banana.png")
orange = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/orange.png")
apple = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/apple.png")
ice = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/ice.png")
bomb = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/bomb.png")
strawberry = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/strawberry.png")

fruits = [banana, orange, apple, ice, bomb, strawberry]
clock = pygame.time.Clock()
FPS = 12
GRAVITY  = 2

class Objet:
    def __init__(self):
        self.x = random.randint(100,1100)
        self.y = 700
        self.vitesse_x = random.randint(-10,10)
        self.vitesse_y = random.randint(-60, -30) 
        self.image = random.choice(fruits)
    
    def update(self):
        self.vitesse_y += GRAVITY 
        self.x += self.vitesse_x
        self.y += self.vitesse_y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

def spawn_new_fruits():
    objets.append(Objet())

objets = [Objet()]



def main_game():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.blit(background, (0, 0)) 

        for objet in objets[:]:
            objet.update()
            objet.display(screen)

        if objet.y > 750 or objet.y<0 or objet.x<0 or objet.x>1250:
                objets.remove(objet)
                spawn_new_fruits()
                         
        pygame.display.update()
        clock.tick(FPS)

main_game()

