'''
Created on Feb 6, 2018

@author: root
'''

from math import floor,ceil

'''
def get_pq():
    p_percent = None
    q_percent = None
    got_num = 0
    while got_num < 2:
        line_without_space = input().replace(" ", "")
        if line_without_space != "":
            if got_num == 0:
                p_percent = round(float(line_without_space),2)/100
            elif got_num == 1:
                q_percent = round(float(line_without_space),2)/100
            got_num += 1
    return p_percent,q_percent
'''
def get_pq():

    line_without_space = input()
    if  " " in line_without_space:
        p_raw = line_without_space.split()[0]
        q_raw = line_without_space.split()[1]
    else:
        p_raw = line_without_space
        q_raw = input()
    p_percent = float(p_raw)/100 +0.000000000001    #key
    q_percent = float(q_raw)/100 -0.000000000001
    return p_percent,q_percent
    


def print_conductors_num(p_percent, q_percent):
    
    n = 1
    while True:
        lower_bound = n/q_percent
        upper_bound = n/p_percent
        
        if floor(upper_bound) == upper_bound and ceil(lower_bound) == lower_bound :    #both upper_bound & lower_bound are int
            if  floor(upper_bound) - ceil(lower_bound) >= 2:
                m = ceil(lower_bound) + 1
                break
        elif floor(upper_bound) == upper_bound:  #only upper_bound is int
            if  floor(upper_bound) - lower_bound > 1:
                m = ceil(lower_bound) 
                break
        elif ceil(lower_bound) == lower_bound:   #only lower_bound is int
            if  upper_bound - ceil(lower_bound) > 1:
                m = ceil(lower_bound) + 1
                break
        else:
            if floor(upper_bound) - ceil(lower_bound) >= 0:  #both upper_bound & lower_bound are not int
                m = ceil(lower_bound)
                break
        
        n += 1
    print(m)    

if __name__ == '__main__':
    
    
    p_percent, q_percent = get_pq()
    
    print_conductors_num(p_percent, q_percent)
    
    
    


            
                
                 