import numpy as np
from turtle import *
n=50
def prime_check(num):
  factors  = range(2,num)
  if(num==1):
    return False
  for i in factors:
    if(num%i==0):
      return False
  return True


num = 0
for i in range(1,n): 
    for _ in range (i):
        num+=1
        prime = prime_check(num)
        if prime:
            dot(5,"blue")
        else:
            dot(3, "black")
        forward(10)
    left(90)
    
    for _ in range (i):
        num+=1
        prime = prime_check(num)
        if prime:
            dot(7, "blue")
        else:
            dot(3, "black")
        forward(10)
    left(90)
    
color("white")
while True:
    forward(1)
