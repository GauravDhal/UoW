unchecked=list(range(100))
#print(len(unchecked))

def bracelet(num1,num2):
    x = [num1,num2]
   
    while True:
        place = x[-2]*10+x[-1]
        unchecked[place]="g"
        i = ( x[-2] + x[-1] ) % 10
        x.append(i)
        if( x[-2] == num1 and x[-1] == num2 ):
            break

    print(x)
    print("Length =",len(x)-2)
    
    
bracelet(1,2)
bracelet(0,2)
bracelet(1,3)
bracelet(2,6)
bracelet(0,5)
bracelet(0,0)

print(unchecked)
