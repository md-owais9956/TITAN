import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)
engine.setProperty("rete",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commanPrompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vs code":"code","powerpoint":"powerpnt"}

def openappweb(query):
    speak(f"ok sir, launching.")
    if ".com" in query or ".co.in"in query or ".org" in query:
        query = query.replace("open","")
        query = query.replace("titan","")
        query = query.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("closing, sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("both tabs are closed, sir")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak(" tabs are closed, sir")
    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak(" tabs are closed, sir")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        pyautogui.sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak(" tabs are closed, sir")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f/im{dictapp[app]}.exe")