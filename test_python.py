'''
Created on Feb 5, 2018

@author: root
'''
import math

def calc():
    a = 1
    b = 2
    return a,b

dictaa = {"a":1,"b":2}
if "a" in dictaa:
    print("hello")
    
i,j = calc()
print(str(i) + " "+ str(j))


a = 31
b = math.floor(a)
print(b)
stra = bin(pow(10,18))
print (bin(pow(10,18)-1) )
print(stra[1])

print(3//2)