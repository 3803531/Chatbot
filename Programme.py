"Code Python"

import openai
import tkinter as tk
from tkinter import simpledialog
import subprocess
import tempfile


""" 
Développement de code de base pour instancier chatGPT
"""
ROOT = tk.Tk()
ROOT.withdraw()


def askGPT(text):
    # entrer la nouvelle clé
    openai.api_key = "clé API"
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

reponse = "Ask me a question" 

fichier = open("VALEURS.txt", "w")
fichier.write("Comment allez vous?")
fichier.write("\n#")
fichier.write("\nReponse")
fichier.close()

while True:
        
        fichier = open("VALEURS.txt", "r")
        Valeurs = fichier.read()
        fichier.close()

        n = 0
        Texte_1 = ""
        Texte_2 = ""

        for i in Valeurs:
            if i != "#":
                if n == 0:
                    Texte_1 += i
                else:
                    Texte_2 += i
            else:
                n = 1
        
        USER_INP = Texte_1.strip()
        Ancienne_rep = ""
        Ancienne_rep_pre = ""

        fichier = open("DERNIERS.txt", "r")
        Valeurs_2 = fichier.read()
        fichier.close()

        for i in Valeurs_2:
            Ancienne_rep_pre += i

        Ancienne_rep = Ancienne_rep_pre.strip()
        if Ancienne_rep != USER_INP:
            fichier = open("DERNIERS.txt", "w")
            fichier.write(USER_INP)
            fichier.close()

             # the input dialog
            # USER_INP = simpledialog.askstring(title="Interface", prompt=reponse)
            print("You:")
            print(USER_INP)
            print('\n')
            reponse = askGPT(USER_INP) 
            print(reponse)
            print('\n')

            fichier = open("VALEURS.txt", "w")
            fichier.write(USER_INP)
            fichier.write("\n#")
            fichier.write(reponse)
            fichier.close()

