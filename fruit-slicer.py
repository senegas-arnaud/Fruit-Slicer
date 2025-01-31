import os
import pygame
import random
import keyboard

pygame.init()

screen = pygame.display.set_mode((1250, 750))
background = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/back.png")
text_font = pygame.font.SysFont("Arial", 40)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ninja = pygame.image.load(r"C:/Users/arnau/Documents/La Plateforme/Python/Fruit-Slicer/images/ninja.png")
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
FPS = 30
GRAVITY  = 2

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
letter = random.choice(alphabet)

def text(texte, text_font, couleur, x, y):
    texte_surface = text_font.render(texte, True, couleur)
    screen.blit(texte_surface, (x, y))

def menu():
    screen.blit(background,(0,0))
    screen.blit(ninja,(0,200))
    text("Welcome to", text_font, (WHITE), 425, 50)
    text("NINJA FRUITS", text_font, (WHITE), 300, 100)
    text("1. PLAY GAME", text_font, (WHITE), 420, 250)
    text("2. CHANGE YOUR NAME", text_font, (WHITE), 420, 300)
    text("3. SCORING TABLE", text_font, (WHITE), 420, 350)
    text("4. EXIT THE GAME (are you sure ?)", text_font, (WHITE), 420, 400)
    text("ENTER YOUR CHOICE", text_font, (WHITE), 460, 450)

def game_over_screen():
    screen.blit(background, (0, 0)) 
    screen.blit(boom, (250,-10))
    screen.blit(lives, (1050, 20))
    screen.blit(lives, (1110, 20))
    screen.blit(lives, (1170, 20))
    text(f"GAME OVER !", text_font, WHITE, 535, 375)
    text(f"1. Play again?", text_font, WHITE, 75, 300)
    text(f"2. Back to menu?", text_font, WHITE, 75,500 )


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

game_state = "menu"
main_loop = True

def reset_game():
    global objets, life
    objets = [Objet()] 
    life = 3 

def main_game():
    reset_game()
    life = 3
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.blit(background, (0, 0))

        for i in range(life):
            screen.blit(lives, (1050 + i * 60, 20))

        for objet in objets[:]:
            objet.update()
            objet.display(screen)

        for objet in objets[:]:
            if objet.y > 745 or objet.y < 5 or objet.x < 5 or objet.x > 1245:
                objets.remove(objet)
                if random.random() < 0.5 and len(objets) >= 2 :
                    continue  
                else:
                    if random.random() < 0.5:
                        spawn_new_fruits()
                    else:
                        spawn_new_fruits()
                        spawn_new_fruits()

                if objet.image == bomb or objet.image == ice:
                    continue 

                if objets:
                    life -= 1
                    if life == 0:
                        return "game_over"


        pygame.display.update()
        clock.tick(FPS)

while main_loop :
    if game_state == "menu":
        menu()
    if game_state == "game_over":
        game_over_screen()
    elif game_state == "playing":
        game_state = main_game()


    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            main_loop = False
        if event.type == pygame.KEYDOWN:
            if game_state == "menu":
                if event.key == pygame.K_1:
                    game_state = "playing"
                elif event.key == pygame.K_4:
                    main_loop = False
            if game_state == "game_over":
                if event.key == pygame.K_1:
                    game_state = "playing"
                if event.key == pygame.K_2:
                    game_state == "menu"    


    pygame.display.update()
    clock.tick(FPS)
pygame.quit()

