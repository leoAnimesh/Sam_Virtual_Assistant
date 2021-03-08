import subprocess
# subprocess.run("pip install pyttsx3",shell=True)
# subprocess.run("pip install speechrecognition",shell=True)
# subprocess.run("pip install wikipedia",shell=True)
# subprocess.run("pip install pyaudio",shell=True)
# subprocess.run("pip install wolframalpha",shell=True)
# subprocess.run("pip install pywhatkit",shell=True)
# subprocess.run("pip install pyautogui",shell=True)
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import wolframalpha
import pywhatkit
import pyautogui

app = wolframalpha.Client('LJ9V8R-TVT33TRV4Q')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')


def speak(audio):  # it enables the speech of the bot
    engine.say(audio)
    engine.setProperty('rate', 200)
    engine.runAndWait()


def wishMe():  # it repeats the comands given
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Hey Good Morning sir!")
        speak("hey  good  morning  sir !")
    elif hour >= 12 and hour <= 18:
        print("Hey Good Afternoon Sir!")
        speak("Hey Good  Afternoon  Sir!")
    else:
        print("Hey Good Evening Sir!")
        speak("Hey  Good  Evening  Sir!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("I am Listning Sir......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: "+query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    print("Sam at your service ")
    speak("Sam  at  your  service ")
    speak("what  can  i do  for  you  sir ")
    while True:
        query = takeCommand().lower()
        # logic for taking comands
        if "wikipedia" in query:
            print("Searching wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print("Acording to Wikipedia")
            speak("Acording to Wikipedia")
            print(result)
            speak(result)

        elif "take a note" in query:
            speak("tell what you want to write")
            r1 = sr.Recognizer()
            with sr.Microphone(device_index=1) as source:
                r1.pause_threshold = 1
                audio = r1.listen(source)
                print("Recognizing...")
                text = r1.recognize_google(audio, language='en-in')
                print("User said: "+text)
                f= open("notes.txt","w+")
                f.writelines(text)
                f.close()
                speak("note taken here you go")
                os.startfile('notes.txt')

        elif "who is" in query:
            print("Searching wikipedia")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif "what is" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif "who are you" in query:
            speak("hello myself sam")
            speak("im a voice assistant")

        elif "what can you do" in query:
            speak("i  can automate your tasks")
            speak("like checking mails")
            speak("Calculating stuffs ")
            speak("search for your queries")
            speak("tell you about the weather and many more things")

        elif "good morning" in query:
            print("Good Morning sir ")
            speak("Good Morning sir ")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"now it's {strTime}")

        elif "introduce yourself" in query:
            speak("Hey my name is sam ")
            speak("and i am a virtual assistant")
            speak("who can help out in your daily task")
            speak("I am here to minimize your effort")
            speak("and maximize your productivity")

        elif "i am getting bored" in query:
            speak("okh")
            speak("so you can read books or")
            speak("complete your project ")
            speak("or i can tell you a joke  or play a song for you")
            speak(" or else do you can take a break and chill out")

        elif "thank you" in query:
            speak("your most Welcome")

        elif "youtube" in query:
            query = query.replace("Youtube", "")
            print("opening Youtube...")
            speak("opening youtube please wait for a while sir")
            webbrowser.open("youtube.com")

        elif "google" in query:
            query = query.replace("google", "")
            print("opening Google ...")
            speak("opening Google please wait for a while sir")
            webbrowser.open("google.co.in")

        elif "facebook" in query:
            query = query.replace("facebook", "")
            print("opening Facebook ...")
            speak("opening facebook please wait for a while sir")
            webbrowser.open("facebook.com")

        elif "instagram" in query:
            query = query.replace("instagram", "")
            print("opening Instagram ...")
            speak("opening instagram please wait for a while sir")
            webbrowser.open("instagram.com")

        elif "mails" in query:
            query = query.replace("mails", "")
            print("opening Gmail ...")
            speak("opening gmail please wait for a while sir")
            webbrowser.open("mail.google.com")

        elif "whatsapp" in query:
            query = query.replace("whatsapp", "")
            print("Opening Whatsapp...")
            speak("opening whatsapp please wait for a while sir")
            webbrowser.open("web.whatsapp.com")

        elif "stack overflow" in query:
            query = query.replace("stack overflow", "")
            print("Openning Stack Overflow...")
            speak("opening stack over flow please wait for a while sir")
            webbrowser.open("stackoverflow.com")

        elif "geeks for geeks" in query:
            query = query.replace("geeks for geeks", "")
            print("Openning geeks for geeks...")
            speak("opening geeks for geeks please wait for a while sir")
            webbrowser.open("www.geeksforgeeks.org")

        # pyautogui

        elif "switch window" in query or "change window" in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')

        elif "take a screenshot" in query:
            pyautogui.press('printscreen')

        elif "copy" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')
            speak("copied")
            
        elif "paste" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            speak("pasted")

        elif "select all" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('a')
            pyautogui.keyUp('ctrl')
            speak("all element selected")

        # pywhatkit

        elif "play" in query:
            query = query.replace("play", "")
            print("playing "+query)
            speak("playing "+query)
            pywhatkit.playonyt(query)

        elif "search" in query:
            query = query.replace("search", "")
            print("Searching google"+query)
            speak("Searching google"+query)
            pywhatkit.search(query)

        elif "shut down" in query:
            pywhatkit.shutdown(time=60)
            speak("shutting down your Pc in 60 seconds")

        elif "cancel shutdown" in query:
            pywhatkit.cancelShutdown()
            speak("Cancelling sheduled shutdown")

        # pywhatkit

        elif "time" in query:
            query = query.replace("time", "")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        # wolframalpha

        elif "weather" in query:
            query = query.replace("Weather ", "")
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)

        elif "meaning of" in query:
            query = query.replace("meaning ", "")
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)

        elif "calculate" in query:
            query = query.replace("calculate ", "")
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)

        elif "tell me a joke" in query:
            # query= query.replace("tell me joke","")
            res = app.query(query)
            print(next(res.results).text)
            speak(next(res.results).text)

        # wolframalpha

        elif "code" in query:
            query = query.replace("code", "")
            webbrowser.open("https://www.jdoodle.com/python3-programming-online/") 
            print("Opening JDoodle.com ..")
            speak("Opening jdoodle.com Please wait for a while sir")

        elif "document" in query:
            query = query.replace("document", "")
            print("Opening Google Docs..")
            speak("Opening Google docs Please wait for a while sir")
            webbrowser.open("https://docs.google.com/document/u/0/")
        elif "excel sheet" in query:
            query = query.replace("excel sheet", "")
            print("Opening Gooogle sheets..")
            speak("Opening google sheets Please wait for a while sir")
            webbrowser.open("https://docs.google.com/spreadsheets/u/0/")

        elif "presentation" in query or "ppt" in query or "google slides" in query:
            query = query.replace("presentation", "")
            print("Opening Google slides..")
            speak("Opening google slides Please wait for a while sir")
            webbrowser.open("https://docs.google.com/presentation/u/0/")

        elif "browser" in query:
            query = query.replace("browser", "")
            code_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            print("Opening Browser..")
            speak("Opening Chrome Please wait for a while sir")
            os.startfile(code_path)

        elif "deactivate sam" in query:
            print("Ok Bye sir")
            print("Happy to help you sir")
            print("Have a Good day sir")
            speak("happy to help you sir")
            speak("have a good day sir")
            exit()
