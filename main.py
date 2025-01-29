import pygame
from pygame.locals import *
import random

pygame.init()

#colors used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# size screen, background and pictures
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fruits Ninja") 


background = pygame.image.load("pictures/background.png").convert()
ninja = pygame.image.load("pictures/ninja.png").convert_alpha()


#text formatting

title_font = pygame.font.SysFont("Arial", 60, italic = True)
second_title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)

def text(text,font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))

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

apple = pygame.image.load("pictures/fruits/apple.png")
banana = pygame.image.load("pictures/fruits/banana.png")
kiwi = pygame.image.load("pictures/fruits/kiwi.png")
lime = pygame.image.load("pictures/fruits/lime.png")
orange = pygame.image.load("pictures/fruits/orange.png")
strawberry = pygame.image.load("pictures/fruits/strawberry.png")
watermelon = pygame.image.load("pictures/fruits/watermelon.png")
ice = pygame.image.load("pictures/fruits/ice.png")
bomb = pygame.image.load("pictures/fruits/bomb.png")
# lives = pygame.image.load("/pictures/fruits/redcross.png")


fruits = [apple, banana, kiwi, lime, orange, strawberry, watermelon, ice, bomb]
clock = pygame.time.Clock()
FPS = 20
GRAVITY  = 2

alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
letter = random.choice(alphabet)


class Objet:
    def __init__(self):
        self.x = random.randint(150,1000)
        self.y = 700
        self.vitesse_x = random.randint(-15,15)
        self.vitesse_y = random.randint(-50, -35) 
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

def main_game():
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return "menu"

        screen.blit(background, (0, 0)) 
        # screen.blit(lives,(1050,20))
        # screen.blit(lives,(1110,20))
        # screen.blit(lives,(1170,20))

        for objet in objets[:]:
            objet.update()
            objet.display(screen)

        if objet.y > 750 or objet.y<0 or objet.x<0 or objet.x>1250:
                objets.remove(objet)
                if random.random() < 0.25:
                    spawn_new_fruits()  
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                if random.random()< 0.05:
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                    spawn_new_fruits() 
                else:
                    spawn_new_fruits() 
                    spawn_new_fruits() 

        pygame.display.update()
        clock.tick(FPS)


game_state = "menu"
main_loop = True

while main_loop :
    if game_state == "menu":
        menu()
    elif game_state == "playing":
        game_state = main_game()


    for event in pygame.event.get():
        if event.type == QUIT:
            main_loop = False
        if event.type == KEYDOWN:
            if game_state == "menu":
                if event.key == K_1:
                    game_state = "playing"
                elif event.key == K_4:
                    main_loop = False


    pygame.display.update()
    clock.tick(FPS)
pygame.quit()