#!/usr/bin/env python
# coding: utf-8

from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import time
import openai

#mettre la clé open ai
openai.api_key = "clé"


#le modele gpt
def Response(text):
    
    response=openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

#pour stocker les reponses de chat
def saveConversation(f,strConversation):
    f.write(strConversation + '\n')
    f.close() 

def Chat():

    # saugarder la reponse de chat
    f= open("reponse.txt","a+")
    #pour les question
    g=open("question.txt","r")
    #print('GPT: Ask me a question\n')
    text=g.read()
    reponce=Response(text)
    saveConversation(f,str(reponce))
    return str(reponce)

#-------------------------------------------récupérer le texte de l 'utulisateur'-------------------------------------
def getText():
    #enregistrer le texte entreer
    fichier = open("question.txt", "w+")
    fichier.write(text.get(1.0,END))
    fichier.close()
    #pour inserer de texte, repone
    #Chat()
    #g = open("reponse.txt", "r")
    #text.insert( END,"\nchat: "+g.read())
    #g.close()
    text.insert( END,"\nchat: "+ Chat())

def continuer():
    fichier = open("question.txt", "w+")
    fichier.close()
    #g = open("reponse.txt", "w+")
    #g.truncate()
    #g.close()
    text.delete(1.0,END)
    
#----------------------------------pour l enregistrement d'audio-------------------------------------------------#
def start_recording():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        question=r.recognize_google(audio,language='fr-FR')
        #save la qst apres la treanscpt
        fichier = open("question.txt", "w+")
        fichier.write(question)
        text.insert(END,"\n"+"vous: "+question)
        fichier.close()

    except sr.UnknownValueError:
        print("Error","Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def stop_recording():
    v=Chat()
    text.insert( END,"\nchat: "+ v)
    #f = open("reponse.txt", "r")
    #f.close()
    
    

def new_recording():
    text.delete(1.0,END)



#---------------------------------------l'inetrefaec--------------------------------------------------#


#creer une premiere fenetre
window = Tk()
#personnaliser cette fenetre
window.title("Chatbot")
window.geometry("1000x620")
window.minsize(650,500)
#window.iconbitmap("chat.ico")
window.config(background='#4169E1')

#creer la frame
frame = Frame(window, bg='#4169E1',bd=1,relief = SUNKEN)
# l 'ajout d'un texte

label_message = Label(window,text="Bienvenue!", font = ('courrier',20),bg='#4169E1')
label_message.pack()

#la zone de texte
text=Text(window,height=23,width=500,font=("Georgia",13),bg='#87CEFA',fg='black')
text.pack(padx=15, pady=10)
#pour valider l 'entrer de texte 
paned1 =PanedWindow(window,orient=HORIZONTAL,bg='#4169E1')
paned1.pack(side = TOP)
#txt_button =Button(paned1,text='ASK',font=("courrier",15),bg='white',fg='black',command=getText)
txt_button =Button(paned1,text="Send question",font=("courrier",13),bg='#87CEFA',fg='black',command=getText)
ef_button =Button(paned1,text='New question',font=("courrier",13),bg='#87CEFA',fg='black',command=continuer)
qt_button =Button(paned1,text='Delete',font=("courrier",13),bg='#87CEFA',fg='black',command=continuer)

paned1.add(txt_button)
paned1.add(ef_button)
paned1.add(qt_button)
paned1.pack(padx=15, pady=10)



           
# les bouton de l enregistremen de la voix
paned =PanedWindow(window,orient=HORIZONTAL,bg='#4169E1')
paned.pack(side = TOP,padx=15, pady=10)

en_button = Button(paned, text="Start Recording", font=("courrier",13),bg='#87CEFA',fg='black',command=start_recording)
ar_button = Button(paned, text="Stop Recording", font=("courrier",13),bg='#87CEFA',fg='black',command=stop_recording)
sv_button = Button(paned, text="New Recording", font=("courrier",13),bg='#87CEFA',fg='black',command=new_recording)

paned.add(en_button)
paned.add(ar_button)
paned.add(sv_button)
paned.pack(padx=15, pady=10)
#afficher
window.mainloop() 


