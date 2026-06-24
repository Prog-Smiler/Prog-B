import speech_recognition as sr
import time
import datetime
import webbrowser
import os
import random
import pyjokes
import asyncio
import edge_tts
import pygame

# Initialize the recognizer and TTS engine
listener = sr.Recognizer()


def talk(text):
    print(f"Prog B: {text}")

    async def _say():
        voice = "en-US-AriaNeural"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save("voice.mp3")

    asyncio.run(_say())
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    os.remove("voice.mp3")


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
    except:
        command = ""
    return command


def run_progb():
    talk("Hello, I'm Prog B. How can I help you?")

    while True:
        command = take_command()

        if 'hello' in command:
            talk("Hi bro! How are you?")

        elif 'how are you' in command:
            talk("I'm just a program, but thanks for asking! How can I assist you today?")

        elif "purpose" in command or "what can you do" in command:
            talk(
                "Hi! I’m Prog B, your personal AI assistant, built to help you with everyday tasks and make your digital life smoother. I can play your favorite music, answer questions, manage notes, give you useful information, and assist with your school projects or research. My goal is to be your reliable, intelligent companion—ready to support you anytime you need help or want to explore something new. Just speak, and I’m here to respond.")
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"Current time is {time}")

        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            talk("Opening YouTube.")

        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            talk("Opening Google.")


        elif "open wikipedia" in command:
            webbrowser.open("https://www.wikipedia.org")
            talk("Opening Wikipedia.")

        elif "date" in command:
            date = datetime.datetime.now().strftime('%Y-%m-%d')
            talk(f"Today's date is {date}")

        elif "who made you" in command:
            talk("I was created by Pragyanam Mahat who loves coding.")

        elif "notes" in command:
            talk("Opening Notepad for you.")
            os.system('notepad.exe')

        elif "thankyou" in command or "thank" in command or "thank you" in command or "thanks" in command:
            talk("You're welcome! If you need anything else, just let me know.")

        elif "google" in command:
            talk("What do you want to search for?")
            search_query = take_command()
            talk(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")


        elif "open" in command:
            talk("Enter the name of the website you want to open with its domain")
            website = input("Enter the name of the website you want to open with its domain (e.g., example.com): ")
            webbrowser.open("www." + website)

        elif "joke" in command or "make me laugh" in command:
            joke = pyjokes.get_joke(language='en', category='neutral')
            talk(joke)


        elif "random number" in command:
            talk("Yo quick thing, can you give me a lowest number and a highest number to select between? ")
            low = int(input("Enter the lowest number: "))
            high = int(input("Enter the highest number: "))
            number = random.randint(low, high)
            talk(f"Here is a random number for you: {number}")



        elif "game" in command:
            game_choice = input("Enter the game you want to play? 1)Prog Dozer(online)\n2)Astro warrior(online)\n:")
            talk("Starting the game. Have fun!")
            if game_choice == '1':
                webbrowser.open("https://prog-smiler.itch.io/prog-doze")
            elif game_choice == '2':
                webbrowser.open("https://tic80.com/play?cart=4218")
            else:
                talk("Invalid choice, please try again.")


        elif "calculator" in command:
            talk("Calculator mode on ")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")
            if operation == '+':
                result = num1 + num2
                talk(f"The result is {result}")
            elif operation == '-':
                result = num1 - num2
                talk(f"The result is {result}")
            elif operation == '*':
                result = num1 * num2
                talk(f"The result is {result}")
            elif operation == '/':
                result = num1 / num2
                talk(f"The result is {result}")
            else:
                result = "Invalid operation"
                talk(result)
            talk("Calculator mode off")

        elif "what is" in command:
            webbrowser.open(f"https://www.google.com/search?q={command}")

        elif 'stop' in command or 'exit' in command or 'bye' in command:
            talk("Goodbye bro!")
            break

        elif command:
            talk("Sorry, I didn't get that.")



run_progb()