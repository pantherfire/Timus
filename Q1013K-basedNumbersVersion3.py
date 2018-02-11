'''
Created on Feb 8, 2018

@author: root
'''
import math

'''
S(n+2) = (k-1)( S(n+1) + S(n) )
'''


'''
|F_n    |   |k-1 k-1|^(n-1)   |F1|
|       | = |       |       x |  |
|F_{n-1}|   |1   0  |         |F0|

F1 = k-1
F0 = 1

the question is converting into anther question: F_n = a * F1 + b * F0

'''

def matrix_multiply_2_2(matrix1,matrix2,m):
    item00 = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]
    item01 = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
    item10 = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
    item11 = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]
    item00 = item00 % m
    item01 = item01 % m
    item10 = item10 % m
    item11 = item11 % m
    return [[item00,item01],[item10,item11]]

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    m = int(input())
    
    if n >= 2 and n <= pow(10,18) and m >= 2 and m <= pow(10,18) and k >= 2 and k <= pow(10,18):
    
        matrix_dicts = {}
        matrix_product = [[1,0],[0,1]]
        
        num = n - 1
        current_position = 0 #current position of the n (binary notation)
        while num:
            remainder  = num % 2
            num = (num - remainder) // 2  #PAY ATTENTION!!!  must use // other than /, otherwise will get wrong for big number eg. 36028797018963966/2
            current_position += 1
            if current_position == 1:
                matrix_dicts[1] = [[k-1,k-1],[1,0]]
            else:
                matrix_dicts[current_position] = matrix_multiply_2_2 ( matrix_dicts[current_position-1],matrix_dicts[current_position-1],m )
                
            if remainder:
                matrix_product = matrix_multiply_2_2 ( matrix_dicts[current_position],matrix_product,m )
                
            #print(matrix_dicts)    
            #print(matrix_product)
        
        f0 = 1
        f1 = k - 1
        
        fn = (matrix_product[0][0] * f1 + matrix_product[0][1] * f0) % m
        print( fn )

        
        
        
        
