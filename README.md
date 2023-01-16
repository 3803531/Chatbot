# Chatbot

Learning-based modeling of non-verbal behavior between two chatbots.

An animated conversational agent is a software entity with a human-like appearance that can communicate with human users through voice, gestures, facial expressions, etc. These verbal and nonverbal behaviors are highly correlated, linked to the intentions and emotions to be communicated (a smile as a sign of joy, a pointing finger to indicate a point in space) and to vocal prosody (a raised eyebrow to mark emphasis). In recent years, there have been significant developments in conversational models (e.g. Google LaMDA). Conversations with chatbots have become much more natural. The objectives of the project are:

To integrate such a conversational model into the Greta virtual agent platform
To improve the dialogues obtained by adding pauses and marking new information; the models will be trained from oral corpora.
To automatically calculate the multimodal behaviors that correspond to the generated dialogues. The deep learning models already integrated in Greta will be enhanced to take into account a greater richness of language acts.
Define different language and behavior styles for each of the chatbots in the interaction.






# Installation
pip install --upgrade openai  
export OPENAI_API_KEY="<OPENAI_API_KEY>"  
 
 
 
 #*****************************************************************************************************************************************************#
 # Remarque:
 A propos des deux fichier "Programme" et "Test"  
 Le programme python fonctionne bien tout seul (il faut d'abord le lancer) et il crée deux fichiers texte, où la question de l'utilisateur et la réponse, s'il y en a une, sont stockées. Ainsi, si vous modifiez manuellement la question dans le fichier texte, ChatGPT devrait répondre automatiquement via python et enregistrer la réponse. Java, par contre, peut modifier un fichier texte (pour mettre à jour la question) mais lorsque les deux s'exécutent en même temps, il y a un problème. La question n'est pas sauvegardée correctement. Je pense que c'est parce que Java élimine ou enregistre le texte à modifier avant de modifier le fichier texte, ce qui fait que python se lance avec une question nulle.On dois travailler sur ce problème.

 
