'''
Created on Feb 11, 2018

@author: root
'''

import math

def remove_factor(n,f,factors_dicts):
    while True:
        if n % f != 0:
            return n
            break
        else: 
            n = n // f
            factors_dicts[f] = factors_dicts[f] + 1

def merge_some_factor(factors_dicts,k):
    if k == 8:
        factors_dicts[8] = factors_dicts[2] // 3
        factors_dicts[2] %= 3
    if k == 4:
        factors_dicts[4] = factors_dicts[2] // 2
        factors_dicts[2] %= 2
    if k == 6:
        min_num = min(factors_dicts[2],factors_dicts[3])
        factors_dicts[6] = min_num
        factors_dicts[2] -= min_num
        factors_dicts[3] -= min_num
    if k == 9:
        factors_dicts[9] = factors_dicts[3] // 2
        factors_dicts[3] %= 2
    
        

def merge_factors(factors_dicts):
    single_factor = 0
    merge_some_factor(factors_dicts,8)
    #print(factors_dicts)
    if ( factors_dicts[2] + factors_dicts[3] ) % 2 == 1 and factors_dicts[2] > 0:    #if odd number 2s and 3s, put a single 2 aside,and merge the left into 4s, 6s, 9s
        factors_dicts[2] -= 1
        single_factor = 2
        
            
    merge_some_factor(factors_dicts,4)
    merge_some_factor(factors_dicts,6)
    merge_some_factor(factors_dicts,9)
    
    if single_factor == 2:
        factors_dicts[2] = 1

    
   
def print_factors(factors_dicts):
    factor_string = ""
    factors = []
    
    for k,v in factors_dicts.items():
        for i in range(0,v):
            factors.append(k)
            
    factors.sort(key=None, reverse=False)
    
    for factor in factors:
        factor_string += str(factor)
        
    print(factor_string)


if __name__ == '__main__':
    n = int(input())
    factors_dicts = {2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    
    if n == 0:
        print(10)
    elif n == 1:
        print(1)
    else:
        n = remove_factor(n,2,factors_dicts)
        n = remove_factor(n,3,factors_dicts)
        n = remove_factor(n,5,factors_dicts)
        n = remove_factor(n,7,factors_dicts)
        
        if n >= 10:
            print(-1)
        else:
            merge_factors(factors_dicts) 
            print_factors(factors_dicts)
                
    
    
    
        