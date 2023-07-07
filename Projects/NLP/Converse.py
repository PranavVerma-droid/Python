# pip install nltk

import nltk
from nltk.chat.util import Chat, reflections

# Define chat pairs
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1! How can I assist you?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) (hungry|thirsty)",
        ["I'm sorry to hear that. Can I help you find a restaurant?",]
    ],
    [
        r"quit",
        ["Goodbye! Take care.",]
    ],
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Bot: Hello! How can I assist you? Type 'quit' to exit.")
chatbot.converse()
