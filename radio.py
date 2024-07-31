import pygame
from pygame import mixer
import random
import time

# Path to song list 
lspath = "song.list"
# Opening list
lschk = open(lspath, "r")
# Finding Amount of songs 
with open(lspath, "r") as file:
    line_count = sum(1 for line in file)
l = line_count // 2
# Importing Info
i = 0
song_list = [] * l
song_titles = [] * l
while i < l:
    print(i)
    song_titles.append(lschk.readline().strip())
    song_list.append(lschk.readline().strip())
    i += 1

# Initializing Pygame
pygame.init()
mixer.init()

# Declaring basic info
background_colour = (0, 255, 0)
font = pygame.font.Font('fonts/Roboto-Regular.ttf', 24)
font_coulour0 = (0, 0, 0) 
font_coulour1 = (255, 255, 255) 
font_coulour2 = (0,255,0)
song_amount = l
song_current = 0
txt_temp = " Now Playing - "
txt_combine = font.render(txt_temp + song_titles[song_current], True, font_coulour0, font_coulour2)
screen = pygame.display.set_mode((500, 30)) 
pygame.display.set_caption('Radio') 
screen.fill(background_colour) 
pygame.display.flip() 
running = True
textRect = txt_combine.get_rect()

song_current = random.randint(0, song_amount)
songld = (song_list[song_current])
txt_combine = font.render(txt_temp + song_titles[song_current], True, font_coulour0, font_coulour2)
mixer.music.load(songld)
mixer.music.set_volume(0.6)
mixer.music.play() 



while running: 
    time.sleep(0.1)
    screen.blit(txt_combine, textRect)
    
    for event in pygame.event.get(): 
        if not pygame.mixer.music.get_busy():
            screen.fill(background_colour) 
            song_current = random.randint(0, song_amount)
            songld = (song_list[song_current])
            txt_combine = font.render(txt_temp + song_titles[song_current], True, font_coulour0, font_coulour2)
            mixer.music.load(songld)
            mixer.music.play() 

        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        pygame.display.update()