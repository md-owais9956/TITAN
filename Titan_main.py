import datetime
import pyttsx3
import speech_recognition
import pyaudio
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rete",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source,0,4)

    try:
        print("Understanding ...")
        query = r.recognize_google(audio,language = 'en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that Again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "titan" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if"bye titan" in query:
                    speak("bye sir, you can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                
                elif "i am fine" in query:
                    speak("that's great, sir")

                elif "Thank you" in query:
                    speak("It's my pleasure ,sir")
                
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                    

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
                
                elif "temperature" in query:
                    search = "temperature in shahjahanpur"
                    url = f"https://www.bing.com/search?pglt=299&q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search = "temperature in shahjahanpur"
                    url = f"https://www.bing.com/search?pglt=299&q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div",class_ = "BNeaWE").text
                    speak(f"current{search} is {temp}")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                
                elif"Finally sleep" in query:
                    speak("bye sir, going to sleep.")
                    exit()
 

        