from gtts import gTTS
import pygame

mytext= 'investment framework!'
language='en'
myobj=gTTS(text=mytext,lang=language,slow=False)
myobj.save("IF.mp3")
pygame.mixer.init()
pygame.mixer.music.load("IF.mp3")
pygame.mixer.music.play() 