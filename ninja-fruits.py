import pygame
import random
import keyboard

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
FPS = 15
GRAVITY = 2

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]

class Fruit:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 600
        self.vitesse_x = random.randint(-15, 15)
        self.vitesse_y = random.randint(-50, -40)
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
                    for objet in self.objets[:]:
                        if event.key == getattr(pygame, f"K_{objet.letter}"):
                            if objet.image == bomb:
                                return "game_over"
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

            for i in range(self.life):
                screen.blit(lives, (550 + i * 50, 20))

            for objet in self.objets[:]:
                objet.update()
                objet.display(screen)

            for objet in self.objets[:]:
                if objet.y > 745 or objet.y < 5 or objet.x < 5 or objet.x > 1245:
                    self.objets.remove(objet)
                    if random.random() < 0.5 and len(self.objets) >= 2:
                        continue
                    else:
                        if random.random() < 0.5:
                            self.spawn_new_fruits()
                        else:
                            self.spawn_new_fruits()
                            self.spawn_new_fruits()

                    if objet.image == bomb or objet.image == ice:
                        continue 

                    self.life -= 1
                    if self.life == 0:
                        return "game_over"
                    
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
    


def main_loop():
    game = Game() 
    run = True

    while run:
        if game.game_state == "menu":
            menu()
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
                        game.reset_game() 
                        game.game_state = "playing"
                    elif event.key == pygame.K_4:
                        run = False
                if game.game_state == "game_over":
                    if event.key == pygame.K_1:
                        game.reset_game()  
                        game.game_state = "playing"
                    if event.key == pygame.K_2:
                        game.game_state = "menu"

        pygame.display.update()
        clock.tick(FPS)

main_loop()
pygame.quit()