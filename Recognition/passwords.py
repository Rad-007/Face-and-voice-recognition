import speech_recognition as sr
import pyttsx3
import pywhatkit
import salting


listener=sr.Recognizer()
engine=pyttsx3.init()


x=""

class Passwords:

    def __init__(self):
        self.password={}
     
    def check(self,name):
        data=open(r"C:\Users\dell\OneDrive\Codes\Recognition\data1.txt",'r')
        re=False
        for s in data:
            
            s.replace('\n','')
            #print(s)
            s=s.split("::")
            if s[0]==name.lower():
                re=True

                
        data.close()
        return re

    
    def add(self,key,value):
        
        
        key=key.lower()
        print()
        value=value.lower()
        #value=salting.encrypt(value)
        self.password[key]=value
        data=open(r"C:\Users\dell\OneDrive\Codes\Recognition\data1.txt",'a')
        s=key+"::"+value+'\n'
        data.write(str(s))
        data.close()
        
                

    def read_file(self):
        data=open(r"C:\Users\dell\OneDrive\Codes\Recognition\data1.txt",'r')
        
        for s in data:
            
            s.replace('\n','')
            #print(s)
            s=s.split("::")
            s1=s[1].replace('\n','')
            self.password[s[0]]= s1 #salting.decrypt(s1)
        data.close()




    def talk(self,text):
        engine.say(text)
        #engine.say(' I am Listening ')
        engine.runAndWait()




    def listen(self,name,ent):

        self.read_file()
        #print(self.password)
        x=name

        try:
            with sr.Microphone() as source:
                
                '''
                self.talk("SPEAK YOUR NAME")
                print("Listening")
                voice=listener.listen(source)
                name=listener.recognize_google(voice)
                name=name.lower()
                '''

                name=name.lower()
                print(name)
                

                self.talk("Say Password")
                print("Say Password")
                voice=listener.listen(source)
                code=listener.recognize_google(voice)
                code=code.lower()
                print(code)

                if (self.password[name]==code and ent==True):
                    
                    self.talk("You are in")
                    

        except:
            pass    

        #return command        



    #add()
    #add()
    #print(password)
    #listen()

#p1=Passwords()
#p1.add(key='kk',value='happy diwali')
#p1.listen(name='kk',ent=True)