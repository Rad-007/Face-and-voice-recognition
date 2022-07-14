from __future__ import division 
import numpy as np 
from scipy.io.wavfile import read 
from LBG import EUDistance 
from mel import mfcc 
from LPC import lpc 
from train import training 
from record import get_sample

def testmain(name):

    name=name.upper()
    ent=False


    get_sample(name)

    nSpeaker = 4
    nfiltbank = 12 
    orderLPC = 15 
    (codebooks_mfcc, codebooks_lpc) = training(nfiltbank, orderLPC,name) 
    directory = 'C:/Users/dell/OneDrive/Codes/Recognition/test' 
    directory=directory+'/'+name
    fname = str() 
    nCorrect_MFCC = 0 
    nCorrect_LPC = 0 

    def minDistance(features, codebooks):
        


        speaker = 0 
        distmin = np.inf 
        for k in range(np.shape(codebooks)[0]): 
            D = EUDistance(features, codebooks[k,:,:]) 
            dist = np.sum(np.min(D, axis = 1))/(np.shape(D)[0]) 
            if dist < distmin: 
                distmin = dist 
                speaker = k 
        return speaker 
    names=['AAYUSH','JAKE','REMO','SOHAM']
    for i in range(nSpeaker): 
        fname = '/s' + str(i+1) + '.wav'
        print ('Now speaker ', str(i+1), 'features are being tested') 
        (fs,s) = read(directory + fname) 
        mel_coefs = mfcc(s,fs,nfiltbank) 
        lpc_coefs = lpc(s, fs, orderLPC) 
        sp_mfcc = minDistance(mel_coefs, codebooks_mfcc) 
        sp_lpc = minDistance(lpc_coefs, codebooks_lpc) 

        print ('Speaker', (i+1), ' in test matches with speaker ', (sp_mfcc+1), 'in train for training with MFCC' )
        print ('Speaker', (i+1), ' in test matches with speaker ', (sp_lpc+1), 'in train for training with LPC' )

        if i == sp_mfcc: 
            nCorrect_MFCC += 1 
        if i == sp_lpc: 
            nCorrect_LPC += 1 


    plpc=percentageCorrect_MFCC = (nCorrect_MFCC/nSpeaker)*100 
    print ('Accuracy of result for training with MFCC is ', percentageCorrect_MFCC, '%' )
    pmfcc=percentageCorrect_LPC = (nCorrect_LPC/nSpeaker)*100 
    print ('Accuracy of result for training with LPC is ', percentageCorrect_LPC, '%')    

    re=(plpc+pmfcc)//2

    if(re>=25):
        ent=True

        print ("Match",re,"%")
    return(ent)

#testmain('AAYUSH')        