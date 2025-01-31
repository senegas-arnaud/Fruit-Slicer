import pygame
import random
from game import Game

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
GRAVITY = 1

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]

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
    

def select_level(game):
    selecting = True
    while selecting:
        screen.blit(background,(0,0))
        screen.blit(ninja,(0,200))
        text("Choose Difficulty", second_title_font, WHITE, 320, 150)
        text("1. EASY", text_font_bold, WHITE, 350, 250)
        text("2. MEDIUM", text_font_bold, WHITE, 350, 300)
        text("3. HARD", text_font_bold, WHITE, 350, 350)
        text("Press 1, 2, or 3 to select", text_font, WHITE, 360, 400)
    
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game.fps = 20  # Easy
                    selecting = False
                elif event.key == pygame.K_2:
                    game.fps = 30  # Medium
                    selecting = False
                elif event.key == pygame.K_3:
                    game.fps = 60  # Hard
                    selecting = False

    game.reset_game()
    game.game_state = "playing"

def main_loop():
    game = Game() 
    run = True

    while run:
        if game.game_state == "menu":
            menu()
        elif game.game_state == "select_level":
            select_level(game)  
        elif game.game_state == "game_over":
            game_over_screen()
        elif game.game_state == "playing":
            game.game_state = game.main_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if game.game_state == "menu":
                    if event.key == pygame.K_1:
                        game.game_state = "select_level"  
                    elif event.key == pygame.K_4:
                        run = False
                elif game.game_state == "game_over":
                    if event.key == pygame.K_1:
                        game.reset_game()
                        game.game_state = "select_level"
                    elif event.key == pygame.K_2:
                        game.game_state = "menu"
                

        pygame.display.update()
        clock.tick(25)

main_loop()
pygame.quit()