from audioop import add, getsample
import threading

import speech_recognition as sr
import pyttsx3
import pywhatkit

import test
from passwords import Passwords
from passwords import Passwords
from newRecord import sample
from record import get_sample
from Entry import face_detect

listener=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
        engine.say(text)
        #engine.say(' I am Listening ')
        engine.runAndWait()

name=""
def startRec():

        
        
        

        try:
            with sr.Microphone() as source:
                
                #speak("ARE YOU A NEW USER")
                #speak("SPEAK YOUR NAME")
                #print("Listening")
                #voice=listener.listen(source)
                #ch=listener.recognize_google(voice)
                #print(ch)
                name,ch=face_detect()

                p=Passwords()
                
                if p.check(name)==False:

                    newName=input("Enter your name:")
                    newName=newName.upper()
                    speak("Say Your Name")
                    print("Say Name")
                    voice=listener.listen(source)
                    newName1=listener.recognize_google(voice)
                    newName1=newName1.upper()

                    



                    code1=input("Type Password:")
                    
                    code1=code1.lower()

                    speak("Say Password ")
                    print("Say Password")
                    voice=listener.listen(source)
                    code2=listener.recognize_google(voice)
                    code2=code2.lower()
                    print(code2)

                    if (code1==code2) and newName==newName1:
                        p2=Passwords()
                        if p2.check(newName)==False:
                            p2.add(newName.upper(),code1)
                            
                            sample(newName.upper())
                        else:    
                            speak("LOG ALREADY EXITS!")
                
                else:
                    #name=input("Enter your name:")
                    name=name.upper()

                    speak("Say Your Name")
                    print("Say Name")
                    voice=listener.listen(source)
                    name1=listener.recognize_google(voice)
                    name1=name.lower()
                    print(name)


                    start(name)

                
                    

        except:
            pass    

        #return command 
        # 
  
        #        

def start(name):
    
    p1=Passwords()
    ent=test.testmain(name)
    p1.listen(name,ent)


    #t1=threading.Thread(target=test.testmain,args=(name,))
    #t2=threading.Thread(target=p1.listen,args=(name,))
    #t1.start()
    #t2.start()
    #t1.join()
    #t2.join()
#name=input("Enter Name:")

while True:

    startRec()

    if 0xFF == ord('q'):
        break