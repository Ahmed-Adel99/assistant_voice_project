import shutil
import speech_recognition as sr
import datetime
import webbrowser
import time
import os
from time import ctime
import pyttsx3
from news import *


r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate',150)


def gender_select():
    gender = input("what you want Male or Female Assistant ?")
    if gender == 'male':
     engine.setProperty('voice', voices[0].id)
    elif gender == 'female':
      engine.setProperty('voice', voices[1].id)
    else:
        print("please type male or Female")
        speak("please type male or Female")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query




def username():
    print("What should i call you sir")
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("_______________________________________".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("_______________________________________".center(columns))

    speak("How can i Help you, Sir")



def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        print("Good Morning Sir !")
        speak("Good Morning Sir !")


    elif hour >= 12 and hour < 18:
        print("Good Afternoon Sir !")
        speak("Good Afternoon Sir !")

    else:
        print("Good Evening Sir !")
        speak("Good Evening Sir !")



    print("I am your spark voice Assistant")
    speak("I am your spark voice Assistant")





def rec_audio(ask = False):

    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I did not get that')
            speak('Sorry, I did not get that')

        except sr.RequestError:
            print('Sorry, my speech service is down')
            speak('Sorry, my speech service is down')
        return voice_data


def respond(voice_data):

    if 'what time now' in voice_data:
        print(ctime())
        speak(ctime())

    if 'search' in voice_data:
        search = rec_audio('what do you want me to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('here is what i found for ' + search)
        speak('here is what i found for ' + search)

    if 'find location' in voice_data:
        location = rec_audio('what is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('here is the location of ' + location)
        speak('here is the location of ' + location)

    if 'open audio' in voice_data:
        print("The audio now Open")
        speak("The audio now Open")
        codePath = r"1.mp3"
        os.startfile(codePath)

    if 'news' in voice_data:
        print("sure sir, Now I will read news for you")
        speak("sure sir, Now I will read news for you")
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    if "who are you" in voice_data:
        print("I am your spark assistant created by Ahmed Adel ")
        speak("I am your spark assistant created by Ahmed Adel ")

    if 'how are you' in voice_data:
        print("I am fine, Thank you")
        print("How are you, Sir")
        speak("I am fine, Thank you")
        speak("How are you, Sir")

    if 'fine' in voice_data or "good" in voice_data:
        print("It's good to know that your fine")
        speak("It's good to know that your fine")

    if 'go to sleep' in voice_data:
        print('bye bye')
        speak('bye bye')
        exit()


gender_select()
wishMe()
username()
time.sleep(1)
while 1:
    voice_data = rec_audio()
    respond(voice_data)
