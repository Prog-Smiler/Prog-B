import speech_recognition as sr
import pygame
import time
import asyncio
#need to work on edge-tts
import edge_tts


r  = sr.Recognizer()

#Voice Setting
Voice = "en-US-GuyNeural"
voice_file = "output.mp3"

async def speak():
        print("Jarvis: ", text)
        communicate = edge_tts.Communicate(text, Voice)
        await communicate.save(voice_file)

#Talk
async def talk(text):
    
    
    await speak()
    pygame.mixer.init()
    pygame.mixer.music.load(voice_file)
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            text = text.lower()  
            print("You said:", text)
            
            if "exit" in text:
                print("You said: ", text)
                asyncio.run(talk())
                break

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("Could not understand audio")

    except KeyboardInterrupt:
        print("Program terminated by user")
        break