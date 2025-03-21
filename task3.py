import random
import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?", "I'm great! How are you?"]
    ],
    [
        r"(.*) your name ?",
        ["I'm a chatbot created to chat with you!", "You can call me ChatBot."]
    ],
    [
        r"what can you do ?",
        ["I can chat with you, answer simple questions, and keep you entertained!"]
    ],
    [
        r"(.*) (created|made) you ?",
        ["I was created by a programmer to have fun conversations!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ],
    [
        r"(.*)",
        ["I'm not sure how to respond to that. Can you ask me something else?", "Interesting! Tell me more."]
    ]
]

def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
