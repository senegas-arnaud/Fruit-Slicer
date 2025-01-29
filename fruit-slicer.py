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
boom = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/boom.png")
lives = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/redcross.png")

fruits = [banana, orange, apple, ice, bomb, strawberry]
clock = pygame.time.Clock()
FPS = 20
GRAVITY  = 2

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
letter = random.choice(alphabet)

def write(texte, text_font, couleur, x, y):
    texte_surface = text_font.render(texte, True, couleur)
    screen.blit(texte_surface, (x, y))

def game_over_screen():
    screen.blit(background, (0, 0)) 
    screen.blit(boom, (250,0))
    write(f"GAME OVER !", text_font, BLACK, 600, 375)
    write(f"1. Play again?", text_font, BLACK, 200, 50)
    write(f"2. Back to menu?", text_font, BLACK, 950,50 )
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                main_game()
            if event.key == pygame.K_2:
                menu()


class Objet:
    def __init__(self):
        self.x = random.randint(150,1000)
        self.y = 700
        self.vitesse_x = random.randint(-15,15)
        self.vitesse_y = random.randint(-50, -40) 
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
    game_over = False
    life = 3
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.blit(background, (0, 0))

        if game_over == True :
            game_over_screen()

        for i in range(life):
            screen.blit(lives, (1050 + i * 60, 20))

        for objet in objets[:]:
            objet.update()
            objet.display(screen)

        for objet in objets[:]:
            if objet.y > 750 or objet.y < 0 or objet.x < 0 or objet.x > 1250:
                objets.remove(objet)
                if random.random() < 0.5 and len(objets) >= 2 :
                    continue  
                else:
                    if random.random() < 0.5:
                        spawn_new_fruits()
                    else:
                        spawn_new_fruits()
                        spawn_new_fruits()
                if objets:
                    life -= 1
                    if life == 0:
                        objets.clear()
                        game_over = True


        pygame.display.update()
        clock.tick(FPS)

main_game()

