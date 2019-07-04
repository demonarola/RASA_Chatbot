# Chatbot using RASA

## What is RASA?
Rasa is an open source machine learning framework for building contextual AI assistants and chatbots.
Rasa has two main modules:
1. NLU for understanding user messages
2. Core for holding conversations and deciding what to do next

# PROJECT INTRODUCTION   :
    Python Version  : Python 3.7.2
    RASA Version    : 1.0.6
    RASA-SDK        : 1.0.0  


## Defination  :

    Create the pizza order bot with RASA which provides the order online pizza facility to customer. in this bot customer 
    select the pizza in two main category : (1) Veg Pizza, (2) Non-veg Pizza. As per customer selection it's shows the sub-
    category of pizza. This bot also provides the facility like customization of pizza. After all conversation are done it 
    shows the pizza details and customer details.

## Steps to create Pizza Bot   :
    

To run on ui :
    rasa run -m models --enable-api --cors "*" --debug
