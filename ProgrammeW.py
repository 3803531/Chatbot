"Code Python"

import openai
import tkinter as tk
from tkinter import simpledialog
import subprocess
import tempfile
import speech_recognition as sr
import pyttsx3



# Ajoutez votre clé API OpenAI ici
openai.api_key = "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"

def askGPT(text):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

reponse = "Ask me a question" 

try:
    r = sr.Recognizer()
    # Recognize audio input
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    text = r.recognize_google(audio, language='fr-FR')
    print("You:", text)

    # Send text to GPT and get response
    reponse = askGPT(text)
    print("ChatGPT:", reponse)

    # Speak the response using pyttsx3
    engine = pyttsx3.init()
    engine.say(reponse)
    engine.runAndWait()

    # write the conversations to a text file
    with open("VALEURS.txt", "a") as f:
        f.write("User: " + text + "\n")
        f.write("ChatGPT: " + reponse + "\n")

except sr.UnknownValueError:
    print("Sorry, I didn't understand that.")
except sr.RequestError as e:
    print("Error; {0}".format(e))
