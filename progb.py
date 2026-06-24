import speech_recognition as sr
import datetime
import webbrowser
import os
import random
import pyjokes
import asyncio
import edge_tts
import subprocess



# Initialize the recognizer and TTS engine
listener = sr.Recognizer()
running = False

log_callback = print


def log(message):
    log_callback(message)

mic = sr.Microphone()



with mic as source:
    print("Calibrating microphone...")
    listener.adjust_for_ambient_noise(source, duration=2)


def talk(text):
    log(f"Prog B: {text}")
    async def _say():
        voice = "en-US-AriaNeural"
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save("voice.mp3")

    asyncio.run(_say())

    subprocess.run([
        "mpv",
        "--no-video",
        "--really-quiet",     # hides mpv progress spam
        "voice.mp3"
    ])

    os.remove("voice.mp3")


def take_command():
    try:
        with mic as source:
            log("Listening..")

            audio = listener.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            command = listener.recognize_google(audio)
            command = command.lower()
            log(f"You said: {command}")

            return command

    except Exception as e:
        log(f"Error: {e}")
        return ""


def run_progb():
    global running
    running = True
    talk("Hey! Welcome back! ")

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
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"Current time is {current_time}")

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



        elif "what is" in command:
            webbrowser.open(f"https://www.google.com/search?q={command}")

        elif 'stop' in command or 'exit' in command or 'bye' in command:
            talk("Goodbye bro!")
            break

        elif command:
            talk("Sorry, I didn't get that.")

def stop_progb():
    global running
    running = False
