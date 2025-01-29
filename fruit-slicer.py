import os
import pygame
import random
import keyboard

pygame.init()

screen = pygame.display.set_mode((1250, 750))
background = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/back.png")
text_font = pygame.font.SysFont("Arial", 15)
BLACK = (0, 0, 0)

banana = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/banana.png")
orange = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/orange.png")
apple = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/apple.png")
ice = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/ice.png")
bomb = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/bomb.png")
strawberry = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/strawberry.png")
lives = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/redcross.png")

fruits = [banana, orange, apple, ice, bomb, strawberry]
clock = pygame.time.Clock()
FPS = 20
GRAVITY  = 2

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
letter = random.choice(alphabet)

def text(text,font, text_color, x, y):
    screen.blit(text, (x,y))


class Objet:
    def __init__(self):
        self.x = random.randint(150,1000)
        self.y = 700
        self.vitesse_x = random.randint(-15,15)
        self.vitesse_y = random.randint(-50, -35) 
        self.image = random.choice(fruits)
    
    def update(self):
        self.vitesse_y += GRAVITY 
        self.x += self.vitesse_x
        self.y += self.vitesse_y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

def spawn_new_fruits():
    objets.append(Objet())
    text(letter, text_font, BLACK, (objet_x, objet_y))

objets = [Objet()]

def main_game():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.blit(background, (0, 0)) 
        screen.blit(lives,(1050,20))
        screen.blit(lives,(1110,20))
        screen.blit(lives,(1170,20))

        for objet in objets[:]:
            objet.update()
            objet.display(screen)

        if objet.y > 750 or objet.y<0 or objet.x<0 or objet.x>1250:
                objets.remove(objet)
                if random.random() < 0.25:
                    spawn_new_fruits()  
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                if random.random()< 0.05:
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                else:
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                         
        pygame.display.update()
        clock.tick(FPS)

main_game()

