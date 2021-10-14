import sys

import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib

import PySimpleGUI as sg
import cv2
import pandas


Array=[]
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    if(audio=="I hope you enjoyed with me, bye, see you later"):
        sys.exit()
    else:
        audio=str(audio)
        Array.append(audio+"\n")
        window.Element('_LISTBOX_').Update(values=Array)
        event = window.Read()

#speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said : {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

def wish():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <=12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am RIVA, the REAL TIME INTERACTING VIRTUAL SYSTEM, build by SAAHIL , SANGRAAM and NINAAD, there at your service, how can I help you ?")




def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("quickserve751@gmail.com","abcd1234@#as")
    server.sendmail("quickserve751@gmail.com ",to,content)
    server.close()

layout = [[sg.Image(filename="C:\\Users\\dell\\Downloads\\iron_back.png", key='key1', size=(500, 450))],[sg.Button('Read')],
              [sg.Text('Commands:')],
              [sg.Listbox(values=(), size=(50, 10), key='_LISTBOX_')]]


window = sg.Window('Alternative items', layout)

if __name__ == '__main__':

    print(1)

    event = window.Read()
    print(event)

    speak("Tell Your password")
    query=takecommand()
    if(query!="all is well"):
        speak("sorry Wrong password , bye ")
        sys.exit()
    else:

        wish()
        c=0
        while c!=1:
            query = takecommand().lower()

            if "open notepad" in query:
                npath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath)
            elif "open command prompt" in query:
                os.system("start cmd")


            elif "ip address" in query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in query:
                speak("Searching wikipedia...")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
                print(results)

            elif "open youtube" in query:
                webbrowser.open("www.youtube.com")

            elif "open google" in query:
                speak("Sir, what should I search on Google")
                cm = takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "show my meetings" in query:
                speak("Sir, Your upcoming meetings are ...")
                result = pandas.read_csv('AI.csv')
                df1 = result.iloc[0][1]
                df2= result.iloc[0][2]
                speak("Date is ")
                speak(df1)
                speak("and timming  is ")
                speak(df2)

            elif "update my mobile number" in query:
                speak("Say your number please.....")
                cm=takecommand()
                result = pandas.read_csv('AI.csv')
                df = result.iloc[0][0] # meeting_date
                df1 = result.iloc[0][1] # meeting_time

                d = {'Meeting_Date': [df], 'Meeting_Time': [df1], 'Mobile_num': [cm]}
                d1 = pandas.DataFrame(d, columns=['Meeting_Date', 'Meeting_Time', 'Mobile_num'])
                d1.to_csv('AI.csv')

            elif "tell my updated number" in query:
                speak("Sir, your number ...")
                result = pandas.read_csv('AI.csv')
                df3=result.iloc[0][3]
                speak(df3)

            elif "open camera" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    if(cv2.waitKey(1) & 0xFF == ord('q')):
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif "send message" in query:
                pywhatkit.sendwhatmsg("+919920581207","Hello Jarvis here",14,8)

            elif "bye" in query:
                c=1

            elif "play my sir video on youtube" in query:
                pywhatkit.playonyt("My SirG")

            elif "email to ninad" in query:
                try:
                    speak("what should I sent ?")
                    content = takecommand().lower()
                    to = "topaleninad01@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent to Ninad")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send this email")

            elif "what do you feel about alexa and siri" in query:
                speak("They are my role models , I want be like them")

        else:
            speak("I hope you enjoyed with me, bye, see you later")
            sys.exit()