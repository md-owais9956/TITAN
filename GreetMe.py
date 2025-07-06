import pyttsx3
import datetime


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour<= 12:
        speak("Good Morning, sir")
    elif hour>12 and hour <=18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")

    speak("i am titan ,How can i help you ?")