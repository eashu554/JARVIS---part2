import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
import psutil
import pyjokes
import pyautogui
from news import speak_news, getNewsUrl
from diction import translate
from loc import weather
from youtube import youtube
import psutil
import pyjokes
from sys import platform
import os
import getpass

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print(voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Eashwar thank you creating me")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Eashwar thank you creating me")

    else:
        speak('Good Evening Eashwar thank you creating me')

    weather()
    speak('I am JARVIS. Please tell me how can I help you Eashwar?')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()



if __name__ == '__main__':

    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif platform == "win32":
        chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)

    webbrowser.register(
        'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'youtube downloader' in query:
            exec(open('youtube_downloader.py').read())

        elif ' change voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Eashwar, I have switched my voice. How is it?")

        if 'jarvis are you there' in query:
            speak("Yes Eashwar, at your service")

        elif 'open youtube' in query:

            webbrowser.get('chrome').open_new_tab('https://youtube.com')

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'open google' in query:
            webbrowser.get('chrome').open_new_tab('https://google.com')

        elif 'open stack overflow' in query:
            webbrowser.get('chrome').open_new_tab('https://stackoverflow.com')

        elif 'play music' in query:
            os.startfile("D:\\RoiNa.mp3")

        elif 'search youtube' in query:
            speak('What you want to search on Youtube?')
            youtube(takeCommand())
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Eashwar, the time is {strTime}')

        elif 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.get('chrome').open_new_tab(
                url)
            speak('Here is What I found for' + search)

        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

        elif 'who created you' in query:
            if platform == "win32" or "darwin":
                speak('Eashwar is my master. He created me couple of days ago')
            elif platform == "linux" or platform == "linux2":
                name = getpass.getuser()
                speak(name, 'is my master. He is running me right now')

        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')
        elif 'open code' in query:
            if platform == "win32":
                os.startfile(
                    "C:\\Users\\mvven\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('code .')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'github' in query:
            webbrowser.get('chrome').open_new_tab(
                'https://github.com/eashu554')



        elif 'remember that' in query:
            speak("what should i remember Eashwar")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif 'dictionary' in query:
            speak('What you want to search in your intelligent dictionary?')
            translate(takeCommand())

        elif 'news' in query:
            speak('Ofcourse Eashwar..')
            speak_news()
            speak('Do you want to read the full news...')
            test = takeCommand()
            if 'yes' in test:
                speak('Ok Eashwar, Opening browser...')
                webbrowser.open(getNewsUrl())
                speak('You can now read the full news from this website.')
            else:
                speak('No Problem Eashwar')

        elif 'email to friend' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'email'
                sendEmail(to, content)
                speak('Email has been sent!')

            except Exception as e:
                speak('Sorry Eashwar, Not able to send email at the moment')