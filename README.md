# Learning-based modeling of non-verbal behavior between two chatbots.



The project aims to create an animated conversational agent with a human-like appearance that can communicate with human users through voice, gestures, facial expressions, etc. The agent will be integrated into the Greta virtual agent platform, and the dialogues will be improved by adding pauses and marking new information, and the models will be trained from oral corpora. The multimodal behaviors that correspond to the generated dialogues will be calculated automatically, and the deep learning models already integrated in Greta will be enhanced to take into account a greater richness of language acts. Different language and behavior styles will be defined for each of the chatbots in the interaction. The objectives of the project are:

*  To integrate such a conversational model into the Greta virtual agent platform.
*  To improve the dialogues obtained by adding pauses and marking new information; the models will be trained from oral corpora.
*  To automatically calculate the multimodal behaviors that correspond to the generated dialogues. The deep learning models already integrated in Greta will be enhanced to take into account a greater richness of language acts.
*  Define different language and behavior styles for each of the chatbots in the interaction.






# Installation
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
 
 
 
  
# Modèle conversationnel
Un modèle conversationnel est un système informatique conçu pour simuler une conversation
humaine. Il utilise des techniques d’apprentissage automatique pour comprendre et répondre aux
utilisateurs en utilisant le langage naturel. Les modèles conversationnels sont souvent utilisés pour
les assistants virtuels, les chatbots et les systèmes de dialogue pour des applications telles que les
services clients automatisés, les jeux et les outils de productivité.  

En tant que partie du projet, on a opté pour l’utilisation d’un modèle conversation prés entraîné
qui a été créé par la plate-forme OpenAI et qui s’appelle "ChatGPT".   


Développé par la plate-forme OpenAI, connu sous le nom de ChatGPT. Ce modèle de traitement
de langage naturel qui utilise des techniques d’apprentissage automatique pour générer des réponses
à des questions posées en langage naturel. Il a été développé en utilisant le modèle Davinci-003
de OpenAI. Le système ChatGPT a été intégré pour permettre une interaction avec un utilisateur
humain. Lorsque l’utilisateur parle, ChatGPT génère une réponse qui est ensuite transmise à la plate-
forme GRETA qui utilise NVBG pour associer une animation à la réponse et la jouer et prononcer
le speech de la réponse.  

Il est possible de personnaliser les réponses et le dialogue en utilisant des règles de détection de
modèle, mais il y a un risque que ChatGPT apprenne des réponses incorrectes en cas de mauvaise
utilisation. On peut aussi laisser ChatGPT apprendre des réponses à partir des dialogues avec
d’autres personnes, mais il y a alors un risque de ne pas contrôler les dialogues et d’aboutir à une
mauvaise utilisation de ChatGPT.  

Nous avons utilisé les fonctionnalités de détection de modèle pour adapter les réponses en fonction
des besoins spécifiques de notre projet.  

Nous avons intègre également une fonctionnalité de reconnaissance vocale qui permet de traduire
un dialogue en texte brut. Cette fonctionnalité est utilisée pour permettre à GRETA de prendre en
compte les phrases/mots prononcés par l’utilisateur lors des expériences. En somme, ChatGPT est
un système de traitement de langage naturel avancé qui permet de créer une interaction humaine-
machine en utilisant la reconnaissance vocale que nous avons rajouté ainsi que l’apprentissage auto-
matique pour générer des réponses pertinentes.  

Pour avoir accès a ChatGPT on a dû récupérer une clé pour pouvoir se connecter avec le Chatbot.
En utilisant ChatGPT, nous avons pu créer une expérience interactive pour les utilisateurs qui
permet une communication plus naturelle et fluide. Le modèle pré-entraîné de OpenAI nous a éga-
lement permis de gagner du temps et des ressources en nous évitant de devoir entraîner un modèle
de conversation à partir de zéro.

 
