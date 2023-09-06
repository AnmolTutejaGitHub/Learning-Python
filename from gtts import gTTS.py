from gtts import gTTS

# Text you want to convert to speech
text = "Hello, this is a test."

# Specify the language and voice
language = 'en'  # Language code (e.g., 'en' for English)
voice = 'com.google.android.tts:en-US-GBR-Wavenet-D'  # Use a specific voice

# Create a gTTS object with the selected voice
tts = gTTS(text, lang=language, tld=voice)

# Save the speech to an audio file (e.g., output.mp3)
tts.save("output.mp3")
