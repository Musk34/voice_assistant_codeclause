import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good morning')

    elif hour>=12 and hour<17:
        speak('Good afternoon')
        
        speak('I am zoya Mam. Please tell me how may i help you')
    else:
        speak('Good evening')

        speak('I am zoya Mam. Please tell me how may i help you')

def takeCommand():

    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
       print("say that again please...")
       return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
    
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open Google' in query:
            webbrowser.open("https://Google.com")

        elif 'open spotify' in query:
            webbrowser.open("https://www.spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam,The time is{strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\singh\\Downloads"
            os.startfile(codepath)

        elif 'quit' in query or 'exit' in query:
            speak('Ok Goodbye!')
            break      