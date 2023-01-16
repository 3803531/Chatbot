# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 02:38:58 2023

  

Il existe  pyttsx3, une bibliothèque qui utilise les moteurs
 de synthèse de la plateforme pour générer la synthèse vocale.
"""

import pyttsx3

engine = pyttsx3.init()
engine.say("Bonjour, je m'appel cherif ?")
engine.runAndWait()


