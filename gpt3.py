# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 01:10:55 2023

@author: shse
"""
# On importe les bibliothèques nécessaires
import openai

#def prompt_format(text,format):
   # return str(f"affiche{format} interpretable en python : {text}")

# On définit la fonction de conversation avec le modèle GPT-3
def  GPT(text):
    # On utilise le modèle GPT-3 de OpenAI pour générer une réponse en fonction de l'input donné
    openai.api_key = "La clé "
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text ,#prompt_format(text,  "dict{'str(nom)','int(valeur)'}"),
        temperature = 0.6,
        max_tokens = 150,
    )
    # On retourne la réponse générée par le modèle
    return print(response.choices[0].text)



while True:
        print('GPT: Ask me \n')
        print('vous: ')
        myQst  = input()
        GPT(myQst)
        print('\n')

