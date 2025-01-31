import os
import pygame
from pygame.locals import *
import random
import json

pygame.init()

#colors used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# size screen, background and pictures
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruits Ninja") 
background = pygame.image.load("pictures/background.png").convert()
ninja = pygame.image.load("pictures/ninja.png").convert_alpha()

#Load images
apple = pygame.image.load("pictures/fruits/apple.png")
banana = pygame.image.load("pictures/fruits/banana.png")
kiwi = pygame.image.load("pictures/fruits/kiwi.png")
lime = pygame.image.load("pictures/fruits/lime.png")
orange = pygame.image.load("pictures/fruits/orange.png")
strawberry = pygame.image.load("pictures/fruits/strawberry.png")
watermelon = pygame.image.load("pictures/fruits/watermelon.png")
ice = pygame.image.load("pictures/fruits/ice.png")
bomb = pygame.image.load("pictures/fruits/bomb.png")
lives = pygame.image.load("pictures/fruits/redcross.png")
boom = pygame.image.load("pictures/fruits/boom.jpg")

fruits = [apple, banana, kiwi, lime, orange, strawberry, watermelon]
bonus = [ice, bomb]
alphabet = ["A", "Z", "E", "R", "T", "Y", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N"]
clock = pygame.time.Clock()
FPS = 20
GRAVITY  = 2

#text formatting
title_font = pygame.font.SysFont("Arial", 60, italic = True)
second_title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)
game_letter_font = pygame.font.SysFont("Arial", 35, bold = True)
scoring_table_font = pygame.font.SysFont("Arial", 40, bold = True)

#Text function
def text(text,font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))

class Objet:
    def __init__(self):
        self.x = random.randint(100,600)
        self.y = 600
        self.vitesse_x = random.randint(-15,15)
        self.vitesse_y = random.randint(-50, -35) 
        self.fruit = random.choice(fruits)
        self.letter = random.choice(alphabet)
        self.fruit_rect = self.fruit.get_rect()
        self.letter_surface = game_letter_font.render(self.letter, True, YELLOW)
        self.letter_rect = self.letter_surface.get_rect()
        self.width = max(self.fruit_rect.width, self.letter_rect.width)
        self.height = self.fruit_rect.height + self.letter_rect.height
        self.rect = pygame.Rect(self.x, self.y,self.width, self.height)
    
    def update(self):
        self.vitesse_y += GRAVITY 
        self.x += self.vitesse_x
        self.y += self.vitesse_y
        self.rect.x = self.x
        self.rect.y = self.y

    def display(self, screen):
        screen.blit(self.fruit, (self.rect.x, self.rect.y + self.letter_rect.height))
        screen.blit(self.letter_surface, (self.rect.x + (self.width - self.letter_rect.width) // 2, self.rect.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


class Objet_bis:
    def __init__(self):
        self.x = random.randint(100,600)
        self.y = 600
        self.vitesse_x = random.randint(-15,15)
        self.vitesse_y = random.randint(-50, -35) 
        self.fruit = random.choice(bonus)
        self.letter = random.choice(alphabet)
        self.fruit_rect = self.fruit.get_rect()
        self.letter_surface = game_letter_font.render(self.letter, True, YELLOW)
        self.letter_rect = self.letter_surface.get_rect()
        self.width = max(self.fruit_rect.width, self.letter_rect.width)
        self.height = self.fruit_rect.height + self.letter_rect.height
        self.rect = pygame.Rect(self.x, self.y,self.width, self.height)
    
    def update(self):
        self.vitesse_y += GRAVITY 
        self.x += self.vitesse_x
        self.y += self.vitesse_y
        self.rect.x = self.x
        self.rect.y = self.y

    def display(self, screen):
        screen.blit(self.fruit, (self.rect.x, self.rect.y + self.letter_rect.height))
        screen.blit(self.letter_surface, (self.rect.x + (self.width - self.letter_rect.width) // 2, self.rect.y))
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)


#Menu function
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

#Game-Over screen
def game_over_screen():
    screen.blit(background, (0, 0)) 
    screen.blit(boom, (250,-10))
    screen.blit(lives, (1050, 20))
    screen.blit(lives, (1110, 20))
    screen.blit(lives, (1170, 20))
    text(f"GAME OVER !", text_font, WHITE, 535, 375)
    text(f"1. Play again?", text_font, WHITE, 75, 300)
    text(f"2. Back to menu?", text_font, WHITE, 75,500 )

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
                text(player, scoring_table_font, (WHITE), 400, coordonate)
                text(score, scoring_table_font, (WHITE), 550, coordonate)
                coordonate += 55 

def spawn_new_fruits():
    objets.append(Objet())

def spawn_bonus():
    objets.append(Objet_bis())


def main_game():

    objets.clear()
    spawn_new_fruits()
    life = 3
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "menu"

        screen.blit(background, (0, 0)) 

        for i in range(life):
            screen.blit(lives, (600 + i * 60, 20))

        for objet in objets[:]:
            objet.update()
            objet.display(screen)

            if objet.y > 600 or objet.y<0 or objet.x<0 or objet.x>850:
                objets.remove(objet)
                spawn_count = random.choices([1, 2, 3, 4, 5, 6], weights=[45, 25, 10, 5, 5, 10])[0]
                match spawn_count:
                    case 1:
                        spawn_new_fruits()
                    case 2:
                        spawn_new_fruits()
                        spawn_new_fruits()
                    case 3:
                        spawn_new_fruits()
                        spawn_new_fruits()
                        spawn_new_fruits()
                    case 4:
                        spawn_new_fruits() or spawn_bonus()
                        spawn_new_fruits()
                        spawn_new_fruits()
                        spawn_new_fruits()
                    case 5:
                        spawn_bonus()
                    case 6:
                        spawn_bonus()
                        spawn_new_fruits()
                        spawn_new_fruits()
            

                if objets:
                    life -= 1
                    if life == 0:
                        return "game_over_score"

        pygame.display.update()
        clock.tick(FPS)

def add_score():
    player_input = ""
    party_score = 200
    
    with open("score.json", "r") as f:
        data_json = json.load(f)

    loop_add_score = True

    while loop_add_score:

        screen.blit(background,(0,0))
        screen.blit(boom, (250,-10))

        text("Score : ", text_font, WHITE, 75, 400)
        text(str(party_score), text_font, WHITE, 125, 400)
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

                        add_json = {"player": player_input, "score":party_score}
                        data_json["scoring"].append(add_json)

                        with open ("score.json", "w") as f:
                            json.dump(data_json,f, indent=1)

                        return "game_over_choice", False

                elif event.key == K_BACKSPACE:
                    player_input = player_input[:-1]

                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    player_input += chr(event.key)

        pygame.display.update()



objets = [Objet()]
game_state = "menu"
main_loop = True

while main_loop :
    if game_state == "menu":
        menu()
    elif game_state == "playing":
        game_state = main_game()
    elif game_state == "game_over_score":
        game_state, loop_add_score = add_score()   
    elif game_state == "game_over_choice":
        game_over_screen()
    elif game_state == "scoring_table":
        scoring_table()


    for event in pygame.event.get():
        if event.type == QUIT:
            main_loop = False
        if event.type == KEYDOWN:
            if game_state == "menu":
                if event.key == K_1:
                    game_state = "playing"
                elif event.key == K_3:
                    game_state = "scoring_table"
                elif event.key == K_4:
                    main_loop = False

            elif game_state == "game_over_choice":
                if event.key == K_1:
                    game_state = "playing"
                elif event.key == K_2:
                    game_state == "menu"  

            elif game_state == "scoring_table":
                if event.key == K_ESCAPE:
                    game_state = "menu"
                elif event.key == K_r:
                    init_json = {"scoring":[]}
                    with open ("score.json", "w") as f:
                        json.dump(init_json,f, indent=1)


    pygame.display.update()
    clock.tick(FPS)
pygame.quit()