from gtts import gTTS
import os

# Text you want to convert to speech
text = "https://github.com/coqui-ai/TTS"

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=text, lang=language)

# Saving the converted audio in a file
tts.save("output.mp3")

# Playing the saved audio file
os.system("start output.mp3")  # For Windows
# os.system("afplay output.mp3")  # For macOS
# os.system("mpg123 output.mp3")  # For Linux (install mpg123 if needed)
