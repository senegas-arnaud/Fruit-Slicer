import pygame
from pygame.locals import *
import random
import keyboard
import time
import json

pygame.init()

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


ninja = pygame.image.load("pictures/ninja.png")
banana = pygame.image.load("pictures/fruits/banana.png")
orange = pygame.image.load("pictures/fruits/orange.png")
apple = pygame.image.load("pictures/fruits/apple.png")
ice = pygame.image.load("pictures/fruits/ice.png")
bomb = pygame.image.load("pictures/fruits/bomb.png")
strawberry = pygame.image.load("pictures/fruits/strawberry.png")
boom = pygame.image.load("pictures/boom.png")
lives = pygame.image.load("pictures/redcross.png")

fruits = [banana, orange, apple, ice, bomb, strawberry]
clock = pygame.time.Clock()
FPS = 25
GRAVITY = 1

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]

class Fruit:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 600
        self.vitesse_x = random.randint(-10, 10)
        self.vitesse_y = random.randint(-35, -25)
        self.image = random.choice(fruits)
        self.letter = random.choice(alphabet)

    def update(self):
        self.vitesse_y += GRAVITY
        self.x += self.vitesse_x
        self.y += self.vitesse_y

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
        text_surface = title_font.render (self.letter, True, YELLOW)
        screen.blit (text_surface, (self.x, self.y))

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
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == K_ESCAPE:
                        return "menu", 0

                    for objet in self.objets[:]:
                        if event.key == getattr(pygame, f"K_{objet.letter}"):
                        # Pour les combos mais ca marche pas trop    
                            #if getattr(pygame, f"K_{objet.letter}") > 3:
                                #self.score += 3
                            #if getattr(pygame, f"K_{objet.letter}") > 4:
                                #self.score += 4
                            if objet.image == bomb:
                                game_score = self.score
                                return "game_over_score", game_score
                            if objet.image == ice :
                                self.objets.remove(objet)
                                time.sleep(4)
                                continue 
                            else : 
                                self.objets.remove(objet)
                                self.score +=1
                                if random.random() < 0.5 and len(self.objets) >= 2:
                                    continue
                                else:
                                    if random.random() < 0.5:
                                        self.spawn_new_fruits()
                                    else:
                                        self.spawn_new_fruits()
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
                        return "game_over_score", game_score
                    
            pygame.display.update()
            clock.tick(FPS)


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

    while run:
        if game.game_state == "menu":
            menu()
        elif game.game_state == "game_over_score":
            game.game_state = add_score(game_score)
        elif game.game_state == "game_over_choice":
            game_over_screen()
        elif game.game_state == "playing":
            game.game_state, game_score = game.main_game()
        elif game.game_state == "scoring_table":
            scoring_table()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if game.game_state == "menu":
                    if event.key == pygame.K_1:
                        game.reset_game() 
                        game.game_state = "playing"
                    elif event.key == pygame.K_3:
                        game.game_state = "scoring_table"
                    elif event.key == pygame.K_4:
                        run = False

                if game.game_state == "game_over_choice":
                    if event.key == pygame.K_1:
                        game.reset_game()  
                        game.game_state = "playing"
                    if event.key == pygame.K_2:
                        game.game_state = "menu"
                
                elif game.game_state == "scoring_table":
                    if event.key == K_ESCAPE:
                        game.game_state = "menu"
                    elif event.key == K_r:
                        init_json = {"scoring":[]}
                        with open ("score.json", "w") as f:
                            json.dump(init_json,f, indent=1)


        pygame.display.update()
        clock.tick(FPS)

main_loop()
pygame.quit()