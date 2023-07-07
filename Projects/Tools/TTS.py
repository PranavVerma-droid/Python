# pip install gtts

from gtts import gTTS
import os

# Providing the text


input_text = input("Please Enter Some Code That You Want to Convert to Voice: ")

# Setting the language
language = "en"

# Passing to gtts engine
voice = gTTS(text=input_text, lang=language, slow=False)

# Creating and saving the audio file
voice.save("demo.mp3")

# Playing the file
os.system("start demo.mp3")