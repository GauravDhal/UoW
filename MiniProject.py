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