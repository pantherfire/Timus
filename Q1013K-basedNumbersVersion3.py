'''
Created on Feb 8, 2018

@author: root
'''
import math

'''
S(n+2) = (k-1)( S(n+1) + S(n) )
'''

'''
|F_{n+1} F_n|  |k-1 1|^n  |k-1 1|
|           | =|     |  x |     |
|F_n F_{n-1}|  |k-1 0|    |1   0|
'''

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    m = int(input())
    
    sum_dicts = {}
    sum_dicts[2] = ( k * (k - 1) ) % m
    sum_dicts[3] = ( ( k - 1) * ( k - 1 ) * (k + 1) ) % m 
    if n >= 4:
        for i in range(4,n + 1):
            sum_dicts[i] = ( (k - 1) * (sum_dicts[i - 1] + sum_dicts[i - 2]) ) % m
    print(sum_dicts[n])