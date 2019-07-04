# Chatbot using RASA

## What is RASA?
Rasa is an open source machine learning framework for building contextual AI assistants and chatbots.
Rasa has two main modules:
1. NLU for understanding user messages
2. Core for holding conversations and deciding what to do next

# Getting Started  :
   The System requires 
   Python 3.7.2, RASA     : 1.0.6, RASA-SDK        : 1.0.0  
   
# Prerequisites
Remaining all dependencies are added into requirements.txt enter into project directory and simply use below command to install it.

pip install -r requirements.txt

# Running the test server:
open 3 different terminal

in 1 terminal :

    python app.py 

in 2 terminal 

    rasa run actions
    
    
in 3 terminal

    rasa run -m models --enable-api --cors "*" --debug
   
 ## screenshots
 
<div align="center">
    <img src="/static/Screenshot_2019-07-04 Pizz Bot.png"</img> 
</div>
