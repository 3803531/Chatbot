# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:41:42 2023

@author: IGUI

Il existe plusieurs bibliothèques Python pour la reconnaissance vocale
 (speech-to-text). L'une des plus populaires est SpeechRecognition, qui 
 prend en charge plusieurs moteurs de reconnaissance vocale, notamment *
 Google Speech Recognition, Microsoft Bing Voice Recognition, et Houndify.
Voici un exemple de code qui utilise SpeechRecognition pour transcrire 
de l'audio enregistré en utilisant le moteur de reconnaissance de Google :
"""

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

text = r.recognize_google(audio, language='fr-FR')
print(text)
