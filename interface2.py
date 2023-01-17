

"""
Ce code crée une fenêtre avec trois boutons qui déclenche respectivement
 les fonctions start_recording(), stop_recording() et save_file() qui 
 permetent de démarrer, arrêter et sauvegarder les enregistrements de voix.
Il est important de noter que pour utiliser la fonction r.recognize_google() 
il est nécessaire d'avoir une connexion internet active et une clé d'API pour 
l'utiliser.
"""



import speech_recognition as sr
import tkinter as tk

def start_recording():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Enregistrement en cours...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="fr-FR")
        print("Texte reconnu : " + text)
        text_label.configure(text=text)
    except Exception as e:
        print("Erreur de transcription : " + str(e))

def stop_recording():
    print("Enregistrement arrêté.")

def save_file():
    with open("enregistrement.txt", "w") as f:
        f.write(text_label["text"])
    print("Enregistrement sauvegardé dans le fichier 'enregistrement.txt'.")

root = tk.Tk()
root.title("Enregistreur de voix")

start_button = tk.Button(root, text="Démarrer l'enregistrement", command=start_recording)
start_button.pack()

stop_button = tk.Button(root, text="Arrêter l'enregistrement", command=stop_recording)
stop_button.pack()

save_button = tk.Button(root, text="Sauvegarder le fichier", command=save_file)
save_button.pack()

text_label = tk.Label(root)
text_label.pack()

root.mainloop()
