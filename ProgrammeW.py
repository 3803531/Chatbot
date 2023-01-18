"Code Python"

import openai
import tkinter as tk
from tkinter import simpledialog
import subprocess
import tempfile
import speech_recognition as sr
import pyttsx3



# Ajoutez votre clé API OpenAI ici
openai.api_key = "clé API"

def askGPT(text):
    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

reponse = "Ask me a question" 

try:
    # initialisation pour la reconnaissance vocale
    r = sr.Recognizer()
    print("Say something!")
    with sr.Microphone() as source:
        audio = r.listen(source)
    text = r.recognize_google(audio, language='fr-FR')
    print(text)
except Exception as e:
    print("Error :  {0}".format(e))

while True:
    USER_INP = input("You: ")
    Ancienne_rep = ""
    Ancienne_rep_pre = ""
    try:
        if Ancienne_rep != USER_INP:
            Ancienne_rep = USER_INP
            reponse = askGPT(USER_INP)
            print("ChatGPT :" + reponse)
            engine = pyttsx3.init()
            engine.say(reponse)
            engine.runAndWait()
    except Exception as e:
        print("Error :  {0}".format(e))
