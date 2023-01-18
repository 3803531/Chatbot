#!/usr/bin/env python
# coding: utf-8

 

from tkinter import *
import speech_recognition as sr
import time

#pour récupérer le texte de l 'utulisateur'
def getText():
    #enregistrer le texte entreer
    fichier = open("question.txt", "a")
    fichier.write(text.get(1.0,END))
    fichier.close()
    
    #pause de la f pour avoir la reponce de gpt
    #time.sleep(10)
    #pour inserer de texte, repone
    g = open("reponse.txt", "r")
    text.insert( END,"\n"+g.read())
    g.close()

def continuer():
    text.delete(1.0,END)
    
#pour l enregistrement d'audio
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




#creer une premiere fenetre
window = Tk()
#personnaliser cette fenetre
window.title("Chatbot")
window.geometry("1000x620")
window.minsize(480,360)
window.iconbitmap("chat.ico")
window.config(background='#bfbecb')

#creer la frame
frame = Frame(window, bg='#bfbecb',bd=1,relief = SUNKEN)
# l 'ajout d'un texte

label_message = Label(window,text="Bienvenue!", font = ('courrier',20),bg='#bfbecb')
label_message.pack()

#la zone de texte
text=Text(window,height=10,width=100)
text.pack()
#pour valider l 'entrer de texte 
paned1 =PanedWindow(window,orient=HORIZONTAL)
paned1.pack(side = TOP)
#txt_button =Button(paned1,text='ASK',font=("courrier",15),bg='white',fg='black',command=getText)
txt_button =Button(paned1,text="?",font=("courrier",20),bg='white',fg='black',command=getText)
ef_button =Button(paned1,text='⤻',font=("courrier",15),bg='white',fg='black',command=continuer)
qt_button =Button(paned1,text='x',font=("courrier",15),bg='white',fg='black',command=getText)

paned1.add(txt_button)
paned1.add(ef_button)
paned1.add(qt_button)
paned1.pack()



           
# les bouton de l enregistremen de la voix
paned =PanedWindow(window,orient=HORIZONTAL)
paned.pack(side = TOP)

en_button = Button(paned, text="⏩", font=("courrier",15),bg='white',fg='black',command=start_recording)
ar_button = Button(paned, text="⏯", font=("courrier",15),bg='white',fg='black',command=stop_recording)
sv_button = Button(paned, text="🔄", font=("courrier",15),bg='white',fg='black',command=save_file)

paned.add(en_button)
paned.add(ar_button)
paned.add(sv_button)
paned.pack()
#afficher
window.mainloop()


 
