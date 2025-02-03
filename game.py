import random
import pygame
import time
from fruit import Fruit
from pygame.locals import *
from sound import Sound

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
lives = pygame.image.load("pictures/redheart.png")
clock = pygame.time.Clock()
FPS = 0

def text(text, text_font, couleur, x, y):
    text_surface = text_font.render(text, True, couleur)
    screen.blit(text_surface, (x, y))

class Game:
    def __init__(self):
        self.score = 0
        self.life = 3
        self.items = [Fruit()]  
        self.game_state = "menu"  
        self.music = Sound()

    def reset_game(self):
        self.score = 0
        self.life = 3
        self.items = [Fruit()]

    def spawn_new_fruits(self):
        self.items.append(Fruit())

    def main_game(self,game_state):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return "menu", 0

                    sliced_fruits = {}  
                    to_remove = []  

                    for item in self.items[:]:  
                        
                        if event.key == getattr(pygame, f"K_{item.letter}"):

                            if item.type == "bomb":
                                self.music.explosion_sound.play()
                                game_score = self.score
                                self.items.clear()
                                return "game_over_score", game_score

                            if item.type == "ice":
                                to_remove.append(item)
                                time.sleep(4)
                                if len(self.items) <= 1:
                                    self.spawn_new_fruits()
                                continue 

                            # add fruits to sliced_fruits dictionnary per letter
                            if item.letter not in sliced_fruits:
                                self.music.slice_sound.play()
                                sliced_fruits[item.letter] = []

                            sliced_fruits[item.letter].append(item)

                    # combo point
                    for letter, fruits in sliced_fruits.items():
                        count = len(fruits)
                        if count > 0:
                            self.score += count  
                            self.score += max(0, count - 1)  

                        
                        to_remove.extend(fruits)

                    # del fruits based on to_remove list
                    for fruit in to_remove:
                        if fruit in self.items:  
                            self.items.remove(fruit)

                    
                    if random.random() < 0.5 and len(self.items) >= 2:
                        pass
                    else:
                        self.spawn_new_fruits()
                        if random.random() < 0.3:
                            self.spawn_new_fruits()

            screen.blit(background, (0, 0))
            text(f"{self.score}", second_title_font, YELLOW, 50,20 )

            for i in range(self.life):
                screen.blit(lives, (550 + i * 65, 20))

            for item in self.items[:]:
                item.update()
                item.display(screen)

            for item in self.items[:]:
                if item.y > 595 or item.y < 5 or item.x < 5 or item.x > 795:
                    self.items.remove(item)
                    if len(self.items) <= 1:
                        self.spawn_new_fruits()
                    else:
                        continue

                    if item.type == "bomb" or item.type == "ice":
                        continue 

                    self.life -= 1
                    if self.life == 0:
                        game_score = self.score
                        self.items.clear()
                        return "game_over_score", game_score
                    
            pygame.display.update()
            clock.tick(game_state["FPS"])