# End of studies' project 
This represents our deliverable for our End of Study Project: Modeling by learning the verbal and non-verbal behavior of a virtual agent.

Group members :
Cherif IGUI 
Sara NAIT ATMAN 
Haoyu WANG 
Enzo LOPENZ  





# Learning-based modeling of non-verbal behavior between two chatbots.



The project aims to create an animated conversational agent with a human-like appearance that can communicate with human users through voice, gestures, facial expressions, etc. The agent will be integrated into the Greta virtual agent platform, and the dialogues will be improved by adding pauses and marking new information, and the models will be trained from oral corpora. The multimodal behaviors that correspond to the generated dialogues will be calculated automatically, and the deep learning models already integrated in Greta will be enhanced to take into account a greater richness of language acts. Different language and behavior styles will be defined for each of the chatbots in the interaction. The objectives of the project are:

*  To integrate such a conversational model into the Greta virtual agent platform.
*  To improve the dialogues obtained by adding pauses and marking new information; the models will be trained from oral corpora.
*  To automatically calculate the multimodal behaviors that correspond to the generated dialogues. The deep learning models already integrated in Greta will be enhanced to take into account a greater richness of language acts.
*  Define different language and behavior styles for each of the chatbots in the interaction.






# Installation

**Greta** => https://github.com/isir/greta.git  

$ pip install --upgrade openai 


# Linux users
 
$ export OPENAI_API_KEY="<OPENAI_API_KEY>"    
$ pip3 install pydub  
$ pip3 install PyAudio   
$ pip3 install SpeechRecognition  


# Window users

$ set OPENAI_API_KEY="<OPENAI_API_KEY>"    
$ pip install pydub  
$ pip install PyAudio  
$ pip install SpeechRecognition  
 
 
 
  
# Conversational model
A conversational model is a computer system designed to simulate a human conversation. It uses machine learning techniques to understand and respond to users using natural language. Conversational models are often used for virtual assistants, chatbots, and dialogue systems for applications such as automated customer service, games, and productivity tools.

As part of the project, we opted to use a pre-trained conversational model created by the OpenAI platform called "ChatGPT". Developed by OpenAI, known as ChatGPT. This natural language processing model uses machine learning techniques to generate responses to questions asked in natural language. It was developed using the OpenAI Davinci-003 model. The ChatGPT system was integrated to allow interaction with a human user. When the user speaks, ChatGPT generates a response which is then transmitted to the GRETA platform which uses NVBG to associate an animation with the response and play and pronounce the speech of the response.

It is possible to customize the responses and dialogue using model detection rules, but there is a risk that ChatGPT will learn incorrect responses in the case of misuse. It is also possible to let ChatGPT learn responses from dialogues with other people, but there is then a risk of not controlling the dialogues and ending up with a misuse of ChatGPT.

We used the model detection features to adapt the responses to the specific needs of our project. We also integrated a speech recognition feature that allows a dialogue to be translated into raw text. This feature is used to allow GRETA to take into account the phrases/words spoken by the user during the experiments. In short, ChatGPT is an advanced natural language processing system that allows for creating a human-machine interaction using the speech recognition feature that we added as well as the machine learning to generate relevant responses.

To access ChatGPT, we had to retrieve a key to be able to connect to the Chatbot. Using ChatGPT, we were able to create an interactive experience for users that allows for more natural and fluid communication. The pre-trained model from OpenAI also allowed us to save time and resources by avoiding having to train a conversation model from scratch.

 
# Programme:
Les fichiers gpt.py et interface.py sont les premières versions. Le premier permet de communiquer avec le chat via un terminal d'éditeur de texte, tandis que le second offre une interface graphique. Veuillez exécuter le programme de GRETA DEF.
