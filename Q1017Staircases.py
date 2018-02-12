'''
Created on 2018 Feb 12

@author: surface
'''
import math

if __name__ == '__main__':
    n = int(input())
    
    stair_dicts = {}

    for i in range (1,n+1):     #initial the dicts and add the elements
        stair_dicts[i] = {1:1}

    for i in range(1,n+1):
        for j in range(2,n+1):
            stair_dicts[i][j] = 0    #initial the stair dicts 
            if j * (j + 1) / 2 <= i:
                #print(i)
                #print(j)
                #print(stair_dicts)
                stair_dicts[i][j] = stair_dicts[i - j][j] + stair_dicts[i - j][j - 1]
    
    q = 0          
    for i in range(2,n+1):
        q += stair_dicts[n][i]
    
    print(q)