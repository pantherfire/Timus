'''
Created on Feb 5, 2018

@author: root
'''

def calc():
    a = 1
    b = 2
    return a,b

dictaa = {"a":1,"b":2}
if "a" in dictaa:
    print("hello")
    
i,j = calc()
print(str(i) + " "+ str(j))

lista = [1,2,3]
del(lista) = 0