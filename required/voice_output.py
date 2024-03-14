
import pyttsx3
import requests

def speak(text):
    engine = pyttsx3.init()
    # Set properties for more natural-sounding voice
    engine.setProperty('rate', 220)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # List available voices
    voices = engine.getProperty('voices')
    # Use the first available voice (you can change the index)
    engine.setProperty('voice', voices[1].id)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()
