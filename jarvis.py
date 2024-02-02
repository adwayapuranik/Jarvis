import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def  wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour >=12 and hour < 17:
        speak("good afternoon!")
    else:
        speak("good evening!")    

    speak("I am Jarvis. Please tell me how may i help you?")

def takeCommand():
    #it takes microphone i/p from user & returns string o/p
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-us')   
        print(f"user said: {query}\n") 
    except Exception as e:
        #print(e)    
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', 'password')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query  = takeCommand().lower()
    
    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query: 
        #    music_dir =  'D:\\Non Critical\\songs\\Favourite Songs2'  
        #    songs = os.listdir(music_dir)
        #    print(songs)
        #    os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S")   
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\adway\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"     
            os.startfile(codePath)


        elif 'email to happy' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "recieveremail@gmail.com"
                sendEmail(to,content);
                speak("email sent")
            except Exception as e:
                print(e)
                speak("sorry, email not sent")

        elif 'tell me about s i t' or 'tell be about siddaganga institute of technology' in query:
            speak("Siddaganga Institute of Technology is a private institute of higher education located in tumkur, India. It was established in 1999 and is affiliated")
