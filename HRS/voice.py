from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import speech_recognition as sr
import time
import pyttsx3

service = Service('"C:\\Users\\HP\\Downloads\\Project of 327\\Project of 327\\HRS\HRS\\chromedriver.exe"')
driver = webdriver.Chrome(service=service)
driver.get('http://127.0.0.1:8000/login/RentPost/')


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

recognizer = sr.Recognizer()
microphone = sr.Microphone()

def speak(query):
    engine.say(query)
    engine.runAndWait()

def recognize_speech():
    with microphone as source:
        audio = recognizer.listen(source, phrase_time_limit=5)
    response = ""
    speak("Noted")
    try:
        response = recognizer.recognize_google(audio)
    except:
        response = "Error"
    return response
time.sleep(3)
speak("Hello master! ")
while True:
    speak("Enter your area")
    voice = recognize_speech().lower()
    print(voice)

    
    speak("Enter Rent")
    voice = recognize_speech().lower()
    print(voice)
    
    speak("Enter Details of your house")
    voice = recognize_speech().lower()
    print(voice)
    
    speak("Enter Rent")
    voice = recognize_speech().lower()
    print(voice)
    
    speak("Enter Squarefeet")
    voice = recognize_speech().lower()
    print(voice)
    
    speak("Enter your phone number")
    voice = recognize_speech().lower()
    print(voice)
    
    
    
  
    if 'exit' in voice:
        speak('Goodbye Master!')
        driver.quit()
        break
    else:
        speak('Not a valid command. Please try again.')
    time.sleep(2)