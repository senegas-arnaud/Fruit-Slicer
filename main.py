import pygame
from pygame.locals import *

pygame.init()

#colors used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (190,190,190)
PINK = (255,192,203)


# size window, background and pictures
window = pygame.display.set_mode((800, 600))

background = pygame.image.load("pictures/background.png").convert()
ninja = pygame.image.load("pictures/ninja.png").convert_alpha()


#text formatting

title_font = pygame.font.SysFont("Arial", 60, italic = True)
second_title_font = pygame.font.SysFont("Arial", 30, italic = True)
text_font = pygame.font.SysFont("Arial", 15)
text_font_bold = pygame.font.SysFont("Arial", 16, bold = True)

def text(text,font, text_color, x, y):
    img = font.render(text, True, text_color)
    background.blit(img, (x,y))

#Menu function
def menu():
    window.blit(background,(0,0))
    window.blit(ninja,(0,200))
    text("Welcome to", second_title_font, (WHITE), 425, 50)
    text("NINJA FRUITS", title_font, (WHITE), 300, 100)
    
    text("1. PLAY GAME", text_font_bold, (WHITE), 420, 250)
    text("2. CHANGE YOUR NAME", text_font_bold, (WHITE), 420, 300)
    text("3. SCORING TABLE", text_font_bold, (WHITE), 420, 350)
    text("4. EXIT THE GAME (are you sure ?)", text_font_bold, (WHITE), 420, 400)

    text("ENTER YOUR CHOICE", text_font, (WHITE), 460, 450)


window.blit(background,(0,0))
main_loop = True

while main_loop :

    for event in pygame.event.get():
        if event.type == QUIT:
            main_loop = False


    menu()

    pygame.display.update()
pygame.quit()