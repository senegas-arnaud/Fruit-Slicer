import random
import pygame
import time
from fruit import Fruit
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("pictures/background.png")

title_font = pygame.font.SysFont("Arial", 60, italic = True)
second_title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)
game_letter_font = pygame.font.SysFont("Arial", 35, bold = True)
scoring_table_font = pygame.font.SysFont("Arial", 40, bold = True)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

ice = pygame.image.load("pictures/fruits/ice.png")
bomb = pygame.image.load("pictures/fruits/bomb.png")
lives = pygame.image.load("pictures/redcross.png")
clock = pygame.time.Clock()
FPS = 0

def text(texte, text_font, couleur, x, y):
    texte_surface = text_font.render(texte, True, couleur)
    screen.blit(texte_surface, (x, y))

class Game:
    def __init__(self):
        self.score = 0
        self.life = 3
        self.objets = [Fruit()]  
        self.game_state = "menu"  

    def reset_game(self):
        self.score = 0
        self.life = 3
        self.objets = [Fruit()]

    def spawn_new_fruits(self):
        self.objets.append(Fruit())

    def main_game(self):
        run = True
        game_state = {"state": "menu", "FPS": 5}
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return "menu", 0

                    sliced_fruits = {}  
                    to_remove = []  

                    for objet in self.objets[:]:  
                        
                        if event.key == getattr(pygame, f"K_{objet.letter}"):

                            if objet.type == "bomb":
                                game_score = self.score
                                self.objets.clear()
                                return "game_over_score", game_score

                            if objet.type == "ice":
                                to_remove.append(objet)
                                time.sleep(4)
                                if len(self.objets) <= 1:
                                    self.spawn_new_fruits()
                                continue 

                            if objet.letter not in sliced_fruits:
                                sliced_fruits[objet.letter] = []

                            sliced_fruits[objet.letter].append(objet)

                    
                    for letter, fruits in sliced_fruits.items():
                        count = len(fruits)
                        if count > 0:
                            self.score += count  
                            self.score += max(0, count - 1)  

                        
                        to_remove.extend(fruits)

                    
                    for fruit in to_remove:
                        if fruit in self.objets:  
                            self.objets.remove(fruit)

                    
                    if random.random() < 0.5 and len(self.objets) >= 2:
                        pass
                    else:
                        self.spawn_new_fruits()
                        if random.random() < 0.5:
                            self.spawn_new_fruits()

            screen.blit(background, (0, 0))
            text(f"{self.score}", second_title_font, YELLOW, 50,20 )

            for i in range(self.life):
                screen.blit(lives, (550 + i * 50, 20))

            for objet in self.objets[:]:
                objet.update()
                objet.display(screen)

            for objet in self.objets[:]:
                if objet.y > 595 or objet.y < 5 or objet.x < 5 or objet.x > 795:
                    self.objets.remove(objet)
                    if len(self.objets) <= 1:
                        self.spawn_new_fruits()
                    else:
                        continue

                    if objet.image == bomb or objet.image == ice:
                        continue 

                    self.life -= 1
                    if self.life == 0:
                        game_score = self.score
                        self.objets.clear()
                        return "game_over_score", game_score
                    
            pygame.display.update()
            clock.tick(game_state["FPS"])