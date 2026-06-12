#Importing packages

import speech_recognition as sr
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
    from playsound import playsound