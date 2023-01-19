#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import speech_recognition as sr
import time
import openai

openai.api_key = "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"

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
    f.truncate()
    f.write(strConversation + '\n')
    f.close() 

def Chat():

    # saugarder la reponse de chat
    f= open("reponse.txt","w+")
    #pour les question
    g=open("question.txt","r")
    #print('GPT: Ask me a question\n')
    text=g.read()
    reponce=Response(text)
    saveConversation(f,str(reponce))

#-------------------------------------------récupérer le texte de l 'utulisateur'-------------------------------------
def getText():
    #enregistrer le texte entreer
    fichier = open("question.txt", "w+")
    #fichier.truncate()
    fichier.write(text.get(1.0,END))
    fichier.close()
    
    #pause de la f pour avoir la reponce de gpt
    #time.sleep(10)
    #pour inserer de texte, repone
    Chat()
    g = open("reponse.txt", "r")
    text.insert( END,"\n"+g.read())
    g.close()

def continuer():
    fichier = open("question.txt", "w+")
    #fichier.truncate()
    fichier.close()
    g = open("reponse.txt", "w+")
    #g.truncate()
    g.close()
    text.delete(1.0,END)
    
#----------------------------------pour l enregistrement d'audio-------------------------------------------------#
def start_recording():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Enregistrement en cours...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        #print("Texte reconnu : " + text)
        text_label.configure(text=text)
    except Exception as e:
        print("Erreur de transcription : " + str(e))

def stop_recording():
    print("Enregistrement arrêté.")

def save_file():
    
    fichier = open("question.txt", "a")
    fichier.write(text_label["text"])
    fichier.close()

#---------------------------------------l'inetrefaec--------------------------------------------------#


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
label_message.pack(padx=15, pady=20)

#la zone de texte
text=Text(window,height=20,width=500)
text.pack(padx=15, pady=20)
#pour valider l 'entrer de texte 
paned1 =PanedWindow(window,orient=HORIZONTAL)
paned1.pack(side = TOP)
#txt_button =Button(paned1,text='ASK',font=("courrier",15),bg='white',fg='black',command=getText)
txt_button =Button(paned1,text="Ask_me",font=("courrier",20),bg='white',fg='black',command=getText)
ef_button =Button(paned1,text='New question',font=("courrier",15),bg='white',fg='black',command=continuer)
qt_button =Button(paned1,text='x',font=("courrier",15),bg='white',fg='black',command=getText)

paned1.add(txt_button)
paned1.add(ef_button)
paned1.add(qt_button)
paned1.pack(padx=15, pady=20)



           
# les bouton de l enregistremen de la voix
paned =PanedWindow(window,orient=HORIZONTAL)
paned.pack(side = TOP,padx=15, pady=20)

en_button = Button(paned, text="Start Recording", font=("courrier",15),bg='white',fg='black',command=start_recording)
ar_button = Button(paned, text="Stop Recording", font=("courrier",15),bg='white',fg='black',command=stop_recording)
sv_button = Button(paned, text="Save Recording", font=("courrier",15),bg='white',fg='black',command=save_file)

paned.add(en_button)
paned.add(ar_button)
paned.add(sv_button)
paned.pack(padx=15, pady=20)
#afficher
window.mainloop()


# In[ ]:




