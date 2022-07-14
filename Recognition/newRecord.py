import pyaudio
import wave
import os
import numpy as np
import time
import os

import shutil

import numpy as np
   
from scipy.io.wavfile import read
from IPython.display import Audio, display, clear_output

from  sklearn import preprocessing
import python_speech_features as mfcc

import pickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture as GMM
from sklearn import preprocessing
#import GMM
#from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")



def sample(name):
    name=name.upper()
    

    msg=['happy holidays','good morning','say I am good','this is a sample voice','kung fu panda']

   

    
    
    #name=input("Your Name:")
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 3

    source = "./train/" + name

    #print(str(os.path.isdir(source)))

    
    if os.path.exists(source):
        shutil.rmtree(source)
    os.makedirs(source)

    #os.mkdir(source)

    
        

    
    for i in range(4):
        audio = pyaudio.PyAudio()
        ra=np.random.randint(0,5 , size = 1)
        if i == 0:
            j = 4
            while j>=0:
                time.sleep(1.0)
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Speak your name in {} seconds".format(j))
                j-=1
        elif i ==1:
            time.sleep(2.0)
            print(msg[ra[0]])
            time.sleep(1.5)

        elif i==2:
            time.sleep(2.0)
            print(msg[ra[0]])
            time.sleep(1.5)


        else:
            time.sleep(2.0)
            print(msg[ra[0]])
            time.sleep(1.5)
        # start Recording
        stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
        print("recording...")
        frames = []
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        # stop Recording
        stream.stop_stream()
        stream.close()
        audio.terminate()
        OUTPUT_FILENAME='s'+str(i+1)+".wav"
        #WAVE_OUTPUT_FILENAME=os.path.join("testing_set",OUTPUT_FILENAME)
        #trainedfilelist=open("testing_set_addition.txt",'a')
        #trainedfilelist.write(OUTPUT_FILENAME+"\n")
        
        # saving wav file of speaker
        waveFile = wave.open(source + '/s' + str((i+1)) + '.wav', 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(audio.get_sample_size(FORMAT))
        waveFile.setframerate(RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        print("Done")

    print("Your Voice has been registered")    
