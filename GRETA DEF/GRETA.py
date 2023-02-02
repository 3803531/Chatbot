#!/usr/bin/env python
# coding: utf-8



from tkinter import *
import speech_recognition as sr
import time
import openai
import Boundaries as bd
import os

# entrer la nouvelle clé
openai.api_key = "clé"

fichier = open("question.txt", "w")
fichier.write("")
fichier.close()

fichier = open("reponse.txt", "w")
fichier.write("")
fichier.close()

#---------------------------------------Les Fonctions Ecrites--------------------------------------------------#
# Greta ne sait pas dire & , faire qqchose !

def askGPT(question):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = question,
        temperature = 0.6,
        max_tokens = 150,
    )
    return response.choices[0].text

def chat():

    question = text.get('end -1 lines',END)
    reponse = askGPT(question).strip()

    fichier = open("question.txt", "w")
    fichier.write(question)
    fichier.close()

    fichier = open("reponse.txt", "w")
    fichier.write(reponse)
    fichier.close()

    text.insert( END,"\n" + "\n Chat :" + reponse + "\n" + "\n")

    ## LIAISON AVEC GRETA FML
    
    with open("Modelo.xml", "r") as file:
        greta_file = file.readlines()

    greta_file.insert(7, reponse)
            
    file = open("ChatGpt.xml", "w")
    contents = "".join(greta_file)
    file.write(contents)
    file.close()

    bd.main(["ChatGpt.xml","Results"])

    ## LIAISON AVEC GRETA BML       <tm id="tm0"/>

    with open("Modelo_BML.xml", "r") as file:
        greta_BML_file = file.readlines()
    
    mot = ""
    reponse_BML = []

    for lettre in reponse:
        if (lettre != " ") and (lettre != ".") and (lettre != "?") and (lettre != "!"):  # Changer pour ajouter ? ! 
            mot = mot + lettre
        else:
            reponse_BML.append(mot)
            print(mot)
            mot = ""


    for i in range(len(reponse_BML)):
        greta_BML_file.insert(3+i, "\n" + "<tm id=" + '"tm' + str(i) + '"/>' + reponse_BML[i] )
    greta_BML_file.insert(3+len(reponse_BML), "\n" + "<tm id=" + '"tm' + str(len(reponse_BML)) + '"/>.<tm id=' + '"tm' + str(len(reponse_BML) + 1) + '"/>')
    
            
    file = open("ChatGpt_BML.xml", "w")
    contents_BML = "".join(greta_BML_file)
    file.write(contents_BML)
    file.close()

def stop_chat():
    n = 1

    while os.path.exists("Results\Conversation_" + str(n)):
        n += 1

    file = open("Results\Conversation_" + str(n) + ".txt","w")
    file.write(text.get(1.0,END))
    file.close()
    text.delete(1.0,END)

#---------------------------------------Les Fonctions Audio--------------------------------------------------#

## Si le programme Crash, cela peut être du a que votre micro n'est pas detecté
## Pour le detecter, lancez ce code au début du programme

## for index, name in enumerate(sr.Microphone.list_microphone_names()):
##    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

## Retrouvez le device index de votre micro, et changez le numero 17 par le votre
def start_recording():
    r = sr.Recognizer()
    with sr.Microphone() as source:         #with sr.Microphone(device_index=17) as source
        audio = r.listen(source)
    try:
        question=r.recognize_google(audio,language='fr-FR')
        #save la qst apres la treanscpt
        fichier = open("question.txt", "w+")
        fichier.write(question)
        text.insert(END,"\n"+"vous: "+question)
        fichier.close()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def stop_recording():
    chat()
    
def new_recording():
    text.delete(1.0,END)


#---------------------------------------L'interface--------------------------------------------------#


#creer une premiere fenetre
window = Tk()

#personnaliser cette fenetre
window.title("Chatbot")
window.geometry("1000x620")
window.minsize(650,500)
window.iconbitmap("chat.ico")
window.config(background='#4169E1')

#creer la frame
frame = Frame(window, bg='#4169E1',bd=1,relief = SUNKEN)
# l 'ajout d'un texte

label_message = Label(window,text="Welcome!", font = ('courrier',20),bg='#4169E1')
label_message.pack()

#la zone de texte
text=Text(window,height=23,width=500,font=("Georgia",13),bg='#87CEFA',fg='black')
text.pack(padx=15, pady=10)
#pour valider l 'entrer de texte 
paned1 =PanedWindow(window,orient=HORIZONTAL,bg='#4169E1')
paned1.pack(side = TOP)

txt_button =Button(paned1,text="Send question",font=("courrier",13),bg='#87CEFA',fg='black',command=chat)
ef_button =Button(paned1,text='New question',font=("courrier",13),bg='#87CEFA',fg='black',command=stop_chat)
qt_button =Button(paned1,text='Delete',font=("courrier",13),bg='#87CEFA',fg='black',command=stop_chat)

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

 
