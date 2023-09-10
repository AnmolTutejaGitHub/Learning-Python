from gtts import gTTS
import os

# Text you want to convert to speech
text = "Hello, this is a text-to-speech example in Python."

# Create a gTTS object
tts = gTTS(text)

# Save the audio to a file
tts.save("output.mp3")

# Play the audio
#os.system("mpg321 output.mp3")  # On Linux
# Alternatively, you can use other audio players depending on your system
# On Windows: os.system("start output.mp3")
os.system("afplay output.mp3")  #on MacOS
