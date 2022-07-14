
n='7 13 5 23'
#salt={'7':'g','13':'m','5':'e','23':'w'}
salt='gmew'

def shift(s,i):
    n=""
    for char in s:
        n+=chr(ord(char)+i)

    return(n+salt)    

def encrypt(s):
    y=""
    
    x=s.split(' ')
    for i in x:
        y=y+salt+shift(i,7)+" "

    print(y)
    return (y)
def decrypt(s):
    s=s.replace('gmew','')
    
    y=""
    
    x=s.split(' ')
    for i in x:
        y=y+shift(i,-7)+" "

    return(y)    

    #print(y.replace('gmew',''))


#e=encrypt('happy diwali')        
#decrypt(e)