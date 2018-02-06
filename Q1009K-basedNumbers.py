'''
Created on Feb 6, 2018

@author: root
'''

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    
    result_dicts = {}
    result_dicts[2] = {0:k-1, 1:(k-1)*(k-1)}    # 0 means num# of valid N digit K based numbers with ending 0 ; 1 for not 0
    if n > 2:
        for i in range(3,n+1):
            result_dicts[i] = {0:result_dicts[i-1][1] * 1 ,1: (result_dicts[i-1][0] + result_dicts[i-1][1]) * (k-1)   }
    print( result_dicts[n][0]+result_dicts[n][1] )
            