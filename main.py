#Importing packages

import speech_recognition as sr
import pygame
import datetime
import webbrowser
import os
import random
import pyjokes
import asyncio
import edge_tts

listener = sr.Recognizer()

#Talk Function:
def talk(test):
    print(f"Prog B: {test}")

    async def _say():
        voice = "en-US-AriaNeural"
        communication = edge_tts.Communicate("voice.mp3")

    asyncio.run(_say())
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")  
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass
    os.remove("voice.mp3")

    def take_command():
        try:
            with sr.Microphone() as source:
                listener.adjust_for_ambient_noise(source, duration = 1)
                print("Prog B: Listening...")
                audio = listener.listen(source)
                command = listener.recognize_google(audio)
                command = command.lower()
                print(f"Prog B: You said: {command}")
        except Exception as e:
            print("Error:", e)
            command = ""
        return command
    
    def run_progb():
        talk("Hi, How can I help you today?")

        while True:
            command = take_command()

            if 'hello' in command:
                talk("Hi bro")
            
            elif 'how are you' in command:
                talk("Rocking and rolling bro ;D")

            elif "purpose" in command or "what can you do" in command:
                talk('''Hi! I am Prog B, a virtual assistant created by my creator, 
                    Prog Smiler. I can assist you by opening any website of your
                    choice or from the list of websites you store, i can tell you
                    date/time, and also search for anything on google, crack dad jokes,
                    give you a random number and also a basic calculator.
                    Ready to rock bro?''')
            elif 'stop' in command or 'exit' in command or 'bye' in command:
                talk("Goodbye bro!")
                break
            elif command:
                talk("I think i am getting dumb! sorry man i could not get that. sad emoji sad emoji #sad life")
    run_progb()