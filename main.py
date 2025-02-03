import pygame
from pygame.locals import *
import random
import time
import json
from game import Game
from fruit import Fruit
from sound import Sound
from Functions import *


pygame.init()

music = Sound()

pygame.display.set_caption("Fruits Ninja") 
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("pictures/background.png")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#text formatting
title_font = pygame.font.SysFont("Arial", 60, italic = True)
second_title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)
game_letter_font = pygame.font.SysFont("Arial", 35, bold = True)
scoring_table_font = pygame.font.SysFont("Arial", 40, bold = True)

#images
ninja = pygame.image.load("pictures/ninja.png")
banana = pygame.image.load("pictures/fruits/banana.png")
boom = pygame.image.load("pictures/boom.png")
lives = pygame.image.load("pictures/redheart.png")

clock = pygame.time.Clock()
FPS = 0

#main program
def main_loop():
    game = Game()
    run = True
    game_state = {"state": "menu", "FPS": 0}

    while run:
        #different states of the program
        if game_state["state"] == "menu":
            menu()
        elif game_state["state"] == "game_over_score":
            game_state["state"] = add_score(game_score)
        elif game_state["state"] == "game_over_choice":
            game_over_screen()
        elif game_state["state"] == "playing":
            game_state["state"], game_score = game.main_game()
        elif game_state["state"] == "scoring_table":
            scoring_table()
        elif game_state["state"] == "level_choice":
            game_state["FPS"] = level_choice()
        elif game_state["state"] == "game_rules":
            game_rules()
       
        #events of the program
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if game_state["state"] == "menu":
                    if event.key == pygame.K_1:
                        game_state["state"] = "level_choice"
                        game_state["FPS"] = level_choice()
                        game.reset_game() 
                        game_state["state"] = "playing"
                    elif event.key == pygame.K_2:
                        game_state["state"] = "scoring_table"
                    elif event.key == pygame.K_3:
                        game_state["state"] = "game_rules"
                    elif event.key == pygame.K_4:
                        run = False
                elif game_state["state"] == "game_over_choice":
                    if event.key == pygame.K_1:
                        game.reset_game()  
                        game_state["state"] = "playing"
                    if event.key == pygame.K_2:
                        game_state["state"] = "menu"
                elif game_state["state"] == "scoring_table":
                    if event.key == K_ESCAPE:
                        game_state["state"] = "menu"
                    elif event.key == K_r:
                        init_json = {"scoring":[]}
                        with open ("score.json", "w") as f:
                            json.dump(init_json,f, indent=1)
                elif game_state["state"] == "game_rules":
                    if event.key == K_ESCAPE:
                        game_state["state"] = "menu"
                            
        pygame.display.update()
        clock.tick(game_state["FPS"])

main_loop()
pygame.quit()