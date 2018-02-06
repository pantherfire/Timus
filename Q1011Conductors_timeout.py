'''
Created on Feb 6, 2018

@author: root
'''

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
    p_percent = None
    q_percent = None
    line_without_space = input()
    if  " " in line_without_space:
        p_raw = line_without_space.split()[0]
        q_raw = line_without_space.split()[1]
    else:
        p_raw = line_without_space
        q_raw = input()
    p_percent = round(float(p_raw),2)/100   
    q_percent = round(float(q_raw),2)/100 
    return p_percent,q_percent
    

    


def print_conductors_num(p_percent, q_percent):
    conductors_dicts = {1:0}    #conductors_dicts {m:n} shows if m citizen in the city and m/n <= p%  and (m+1)/n >= q%
    
    if p_percent < 1/2 and q_percent > 1/2:
        print(2)
        return
    elif  q_percent <= 1/2:
        conductors_dicts[2] = 0
    elif p_percent >= 1/2:
        conductors_dicts[2] = 1
    

    
    
    testing_conductor_nums = 3

    
    while True:
        for i in range( conductors_dicts[testing_conductor_nums-1] + 1  , testing_conductor_nums ):
            if i/testing_conductor_nums <= p_percent:
                pass
            elif i/testing_conductor_nums > p_percent and i/testing_conductor_nums < q_percent:
                print(testing_conductor_nums)
                return
            elif i/testing_conductor_nums >= q_percent:
                conductors_dicts[testing_conductor_nums] = i - 1
                testing_conductor_nums += 1
                break                
        

if __name__ == '__main__':
    
    
    p_percent, q_percent = get_pq()
    
    print_conductors_num(p_percent, q_percent)
    
    
    


            
                
                 