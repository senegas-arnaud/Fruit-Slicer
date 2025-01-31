import pygame
from pygame.locals import *
import json
from game import Game


pygame.init()

pygame.display.set_caption("Fruits Ninja") 
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load("pictures/background.png")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#text formatting
title_font = pygame.font.SysFont("Arial", 60, italic = True)
second_title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)
game_letter_font = pygame.font.SysFont("Arial", 35, bold = True)
scoring_table_font = pygame.font.SysFont("Arial", 40, bold = True)


ninja = pygame.image.load("pictures/ninja.png")
banana = pygame.image.load("pictures/fruits/banana.png")
boom = pygame.image.load("pictures/boom.png")
lives = pygame.image.load("pictures/redcross.png")

clock = pygame.time.Clock()
FPS = 0


def menu():
    screen.blit(background,(0,0))
    screen.blit(ninja,(0,200))
    text("Welcome to", second_title_font, (WHITE), 425, 50)
    text("NINJA FRUITS", title_font, (WHITE), 300, 100)
    text("1. PLAY GAME", text_font_bold, (WHITE), 420, 250)
    text("2. CHANGE YOUR NAME", text_font_bold, (WHITE), 420, 300)
    text("3. SCORING TABLE", text_font_bold, (WHITE), 420, 350)
    text("4. EXIT THE GAME (are you sure ?)", text_font_bold, (WHITE), 420, 400)
    text("ENTER YOUR CHOICE", text_font, (WHITE), 460, 450)

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
                    return 10 #FPS
                elif event.key == K_2:
                    return 15  #FPS
                elif event.key == K_3:
                    return 20 #FPS


def game_over_screen():
    screen.blit(background, (0, 0)) 
    screen.blit(boom, (250,-10))
    text("GAME OVER !", title_font, WHITE, 235, 375)
    text("1. Play again?", second_title_font, WHITE, 75, 300)
    text("2. Back to menu?", second_title_font, WHITE, 75,500 )


def text(texte, text_font, couleur, x, y):
    texte_surface = text_font.render(texte, True, couleur)
    screen.blit(texte_surface, (x, y))
    


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
    coordonate = 50
    for player,score in top_score:
        if coordonate <= 500:
                player = str(player)
                score = str(score)
                text(player, scoring_table_font, (WHITE), 350, coordonate)
                text(score, scoring_table_font, (WHITE), 600, coordonate)
                coordonate += 55 



def add_score(game_score):
    player_input = ""
    
    with open("score.json", "r") as f:
        data_json = json.load(f)

    loop_add_score = True

    while loop_add_score:

        screen.blit(background,(0,0))
        screen.blit(boom, (250,-10))

        text("Score : ", text_font, WHITE, 75, 400)
        text(str(game_score), text_font, WHITE, 125, 400)
        text("Enter your player name", text_font, WHITE, 75, 350)
        text("Press ENTER to save", text_font, WHITE, 75, 500)
    
    # Display current input
        current_input_text = text_font.render(player_input, True, WHITE)
        screen.blit(current_input_text, (75, 450))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                
                if event.key == K_RETURN:
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



def main_loop():
    game = Game() 
    run = True
    game_state = {"state": "menu", "FPS": 0}

    while run:
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
                    elif event.key == pygame.K_3:
                        game_state["state"] = "scoring_table"
                    elif event.key == pygame.K_4:
                        run = False

                if game_state["state"] == "game_over_choice":
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


        pygame.display.update()
        clock.tick(game_state["FPS"])

main_loop()
pygame.quit()