import pygame
from pygame.locals import *
import random
import time
import json
import game
import fruit
from sound import Sound


screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("pictures/background.png")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#text formatting
title_font = pygame.font.SysFont("Arial", 60, italic = True)
second_title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 20)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)
game_letter_font = pygame.font.SysFont("Arial", 35, bold = True)
scoring_table_font = pygame.font.SysFont("Arial", 40, bold = True)
game_rule_font = pygame.font.SysFont("Arial", 20, bold = True)

#images
ninja = pygame.image.load("pictures/ninja.png")
banana = pygame.image.load("pictures/fruits/banana.png")
lime = pygame.image.load("pictures/fruits/lime.png")
kiwi = pygame.image.load("pictures/fruits/kiwi.png")
orange = pygame.image.load("pictures/fruits/orange.png")
apple = pygame.image.load("pictures/fruits/apple.png")
ice = pygame.image.load("pictures/fruits/ice.png")
bomb = pygame.image.load("pictures/fruits/bomb.png")
strawberry = pygame.image.load("pictures/fruits/strawberry.png")
watermelon = pygame.image.load("pictures/fruits/watermelon.png")
boom = pygame.image.load("pictures/boom.png")
lives = pygame.image.load("pictures/redheart.png")

fruits = [apple, banana, kiwi, lime, orange, strawberry, watermelon, bomb, ice]
clock = pygame.time.Clock()

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]

#Menu
def menu():
    screen.blit(background,(0,0))
    screen.blit(ninja,(0,200))
    text("Welcome to", second_title_font, (WHITE), 425, 50)
    text("FRUITS NINJA", title_font, (WHITE), 300, 100)
    text("1. PLAY GAME", text_font_bold, (WHITE), 420, 250)
    text("2. SCORING TABLE", text_font_bold, (WHITE), 420, 300)
    text("3. GAME RULES", text_font_bold, (WHITE), 420, 350)
    text("4. EXIT THE GAME (are you sure ?)", text_font_bold, (WHITE), 420, 400)
    text("ENTER YOUR CHOICE", text_font, (WHITE), 460, 450)

#level selection
def level_choice():
    screen.blit(background, (0, 0)) 
    screen.blit(ninja,(0,200))
    text("Choose you difficulty", second_title_font, (WHITE), 300, 200)
    text("1. EASY", text_font_bold, (WHITE), 300, 250)
    text("2. MEDIUM", text_font_bold, (WHITE), 300, 300)
    text("3. HARD", text_font_bold, (WHITE), 300, 350)
    pygame.display.update()

    while True: 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_1:
                    return 15 #FPS
                elif event.key == K_2:
                    return 20  #FPS
                elif event.key == K_3:
                    return 40 #FPS

#game rules
def game_rules():
    screen.blit(background,(0,0))
    text("FRUITS NINJA\nGAME RULES", title_font, (WHITE), 300, 60)
    text("Collect as many points as possible before getting game over.", game_rule_font, (WHITE), 30, 210)
    text("Type the letter that appears above every fruit entering the screen before \nit disappears.", game_rule_font, (WHITE), 30, 240)
    text("If you miss the fruit, you lose a life (you start the game with 3 lives)", game_rule_font, (WHITE), 30, 300)
    text("If you type the letter above an icecube the game will pause for 3 seconds \nthen resume.", game_rule_font, (WHITE), 30, 330)
    text("You can get extra points by getting a combo of 3 fruits with the same letter.", game_rule_font, (WHITE), 30, 390)
    text("Be careful though! Make sure you don't type the letter above the bomb, \nor you lose the game immediately!", game_rule_font, (WHITE), 30, 420)
    text("GOOD LUCK!", second_title_font, (WHITE), 250, 500)
    text("ESC to return to menu",text_font,(WHITE),200, 560)

#options once game over is reached: replay or menu
def game_over_screen():
    screen.blit(background, (0, 0)) 
    screen.blit(boom, (250,-10))
    text("GAME OVER !", title_font, WHITE, 235, 375)
    text("1. Play again?", second_title_font, WHITE, 75, 300)
    text("2. Back to menu?", second_title_font, WHITE, 75,500 )


def text(text, text_font, couleur, x, y):
    text_surface = text_font.render(text, True, couleur)
    screen.blit(text_surface, (x, y))

#scoring table
def scoring_table():
    
    screen.blit(background, (0, 0)) 
    text("Press ESC to cancel, Press R to reset scoring", text_font, WHITE, 380, 560)

    with open("score.json", "r") as f:
        score_json = json.load(f)

    all_score = []

    for player_data in score_json["scoring"]:
        
        list_score = (player_data["player"],player_data["score"])
        all_score.append(list_score)
        
    sort_score = sorted(all_score, key=lambda score:score[1], reverse=True)

    top_score = sort_score[:10]
    coordinate = 50
    for player,score in top_score:
        if coordinate <= 500:
                player = str(player)
                score = str(score)
                text(player, scoring_table_font, (WHITE), 350, coordinate)
                text(score, scoring_table_font, (WHITE), 600, coordinate)
                coordinate += 55 
 
#end of game: save player's score
def add_score(game_score):
    player_input = ""
    
    with open("score.json", "r") as f:
        data_json = json.load(f)

    loop_add_score = True

    while loop_add_score:

        screen.blit(background,(0,0))
        screen.blit(boom, (250,-10))

        text("Score :  ", text_font, WHITE, 75, 400)
        text(str(game_score), text_font, WHITE, 125, 400) 
        text("GAME OVER !", title_font, WHITE, 235, 375)
        text("Enter your player name", text_font, WHITE, 75, 350)
        text("Press ENTER to save", text_font, WHITE, 75, 500)
    
    # Display current input
        current_input_text = text_font.render(player_input, True, WHITE)
        screen.blit(current_input_text, (75, 450))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game.gamestate = "menu"

                elif event.key == K_RETURN:
                    if player_input and len(player_input) > 1:
                        player_input = player_input.lower()

                        add_json = {"player": player_input, "score":game_score}
                        data_json["scoring"].append(add_json)

                        with open ("score.json", "w") as f:
                            json.dump(data_json,f, indent=1)

                        return "game_over_choice"

                elif event.key == K_BACKSPACE:
                    player_input = player_input[:-1]

                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    player_input += chr(event.key)

        pygame.display.update()

