import pygame

class Sound:
    def __init__(self):
        self.music = pygame.mixer_music.load("sounds/ninja-247546.mp3")
        self.music_volume = pygame.mixer.music.set_volume(0.25)
        self.music_play = pygame.mixer.music.play(loops = -1) #-1 makes the music loop indefinitely
        self.slice_sound = pygame.mixer.Sound("sounds/slice_sound.wav")
        self.explosion_sound = pygame.mixer.Sound("sounds/explosion.wav")
        # self.life_sound = pygame.mixer.Sound("sounds\error.wav")

    def sound_volume(self):
        self.slice_sound.set_volume(0.15)
        self.explosion_sound.set_volume(0.15)
        self.life_sound.set_volume(0.15)