import numpy as np

#checking for the series thingy (strategy 3)
sum=0
r=2;
while(sum<=2):
    sum=sum+1/r
    print(r,sum)
    r=r+1
    
print(r-1)  



#checking for the series thingy (improving bounds)
sum=0
r=2;
while(sum<=1):
    sum=sum+1/r
    print(r,sum)
    r=r+1
    
print(r-1)    

#randomly filling
n=6
glasses = np.zeros(n)
win=False #Ali wins
while(win!=True):
    l = 0.5 #liquid remaining
    attempt = np.zeros(n)
    for i in range(0,n-1):
        attempt[i] = np.random.uniform(0,l)
        l = l-attempt[i]
     
    attempt[n-1]=l
    glasses = glasses + attempt
    print("Ali's turn",glasses)

    #check if overflowing
    if(np.max(glasses) >1):
        win=True
    
    #emptying glasses
    glasses[np.argmax(glasses)]=0
    glasses[ (np.argmax(glasses)-1) % n ]=0

    print("Beth's turn",glasses)