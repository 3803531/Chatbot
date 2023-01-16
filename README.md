# Chatbot
Modélisation par apprentissage du comportement non verbal  entre deux chatbots.



# Installation
pip install --upgrade openai  
export OPENAI_API_KEY="<OPENAI_API_KEY>"  
 
 
 
 
 # Remarque:
 Le programme python fonctionne bien tout seul (il faut d'abord le lancer) et il crée deux fichiers texte, où la question de l'utilisateur et la réponse, s'il y en a une, sont stockées. Ainsi, si vous modifiez manuellement la question dans le fichier texte, ChatGPT devrait répondre automatiquement via python et enregistrer la réponse. Java, par contre, peut modifier un fichier texte (pour mettre à jour la question) mais lorsque les deux s'exécutent en même temps, il y a un problème. La question n'est pas sauvegardée correctement. Je pense que c'est parce que Java élimine ou enregistre le texte à modifier avant de modifier le fichier texte, ce qui fait que python se lance avec une question nulle.On dois travailler sur ce problème.

 
