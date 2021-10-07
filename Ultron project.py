import speech_recognition as sr
import pyaudio
import pywhatkit
from gtts import gTTS
from playsound import playsound


def speech(text):

    print(text)
    language= "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")
    speech("On it")

def get_audio():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio =recorder.listen(source)
        text = recorder.recognize_google(audio)
    print(f"You said: {text}")
    return text

text = get_audio()

if "youtube" and "play" in text.lower():
    pywhatkit.playonyt(text)
else:
    pywhatkit.search(text)
  
    