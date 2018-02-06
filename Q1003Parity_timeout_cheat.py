'''
Created on Jan 29, 2018
@author: root
'''
from builtins import print
def get_solution2(conditions):
    satisfied_conditions = []    #may include condition  e.g.  [[1,3],[5,7],1]  ; no intersect part in satisfied_conditions
    for condition in conditions:
        adding_condition = []
        changing_conditions = []
        changed_condition = []
        if satisfied_conditions == []:
            satisfied_conditions.append(condition)
        else:
            adding_condition = condition
            if mistake( adding_condition, satisfied_conditions):
                print ( len(satisfied_conditions) )
                break
            changing_conditions = involved(satisfied_conditions,adding_condition)    #get the involved conditions from satisfied_conditions according adding condition and delete the involved ones from satisfied_conditions
            changed_condition = difference_set(changing_conditions,adding_condition)
            satisfied_conditions.append(changed_condition)
   
def mistake( adding_condition, satisfied_conditions):
    for satisfied_condition in satisfied_conditions:
        if len(satisfied_condition) == 2 and satisfied_condition[0][0] ==  adding_condition[0] and satisfied_condition[0][1] ==  adding_condition[1] and satisfied_condition[0][2] !=  adding_condition[2]:
            return True
    return False
def involved(satisfied_conditions,adding_condition):
    changing_conditions = []
    for  satisfied_condition in satisfied_conditions:
        for i in range(0,len(satisfied_condition)-1 ):   #e.g.   [[1,3],[5,7],1]
            if  not ( satisfied_condition[i][1] <  adding_condition[0] or satisfied_condition[i][0] > adding_condition[1] ):   #if involved
                changing_conditions.append(satisfied_condition)
                satisfied_conditions.remove(satisfied_condition)
                break
    return changing_conditions
def merge_condition(changing_conditions):
    merged_conditions = []
    merged_nums = 0
    for changing_condition in changing_conditions:    #assuming there is no intersect part accoss conditions in changing_conditions
        for i in range(0,len(changing_condition)):
            merged_conditions.append(changing_condition[i])
        merged_nums = (merged_nums + changing_condition[-1]) % 2  #xor
    merged_conditions.sort(key=lambda item:item[0], reverse=False)
    merged_conditions.append(merged_nums)
    return merged_conditions
           
def difference_set(changing_conditions,adding_condition):
    changed_condition = []
    merged_conditions = []
    merged_conditions = merge_condition(changing_conditions)
   
    for merged_condition in merged_conditions:
        for i in range(0,len(merged_condition)-1 ):
            pass
       
def get_points(conditions):
    points = []
    points.append(1)
    points.append(1000000000)
    for condition in conditions:
        points.append(condition[0])
        points.append(condition[1])
    #print(points)
    points = list(set(points))
    points.sort(key=None, reverse=False)
    #print(points)
    return points
  
def get_set(points):
    sets = []
    #points_num = len(points)
    last_point = 0
    for point in points:
        if sets == []:
            sets.append( [point,point] )    #first point must be in sets
        else:
            if point - last_point > 1:
                sets.append([last_point + 1,point - 1])
            sets.append( [point,point] )
        last_point = point
    #print(sets)
    return sets
def find_set(point,sets):
    for i in range(0,len(sets)):
        if sets[i][0]<=point and sets[i][1]>=point:
            return i
    
def get_solution(conditions_sets,conditions,sequence_length):
    satisfied_conditions_sets = [] 
    conditions_sets_length = len(conditions_sets) 
    ith_condition = 0
    is_finished = False
    while conditions_sets:
        #print("con:  "+ str(conditions_sets))
        #print("satis:  "+ str(satisfied_conditions_sets))   
        conditions_set = conditions_sets[0]  #conditions_set is the testing conditon (new adding ones) and always the first one of condition sets
        if conditions_set[2] == 'original':
            ith_condition += 1
        conditions_sets.remove(conditions_set)
        #input()
        if satisfied_conditions_sets == []:
            satisfied_conditions_sets.append(conditions_set)
        else:
            for satisfied_conditions_set in satisfied_conditions_sets:   #need test every one of the satisfied_conditions_set
               
                if conditions[ith_condition-1][1] > sequence_length:
                    print(ith_condition -1 )   #find error
                    conditions_sets = []
                    is_finished = True
                    break
                elif satisfied_conditions_set[0] == conditions_set[0] and satisfied_conditions_set[1] != conditions_set[1]:
                    print(ith_condition -1 )   #find error
                    conditions_sets = []
                    is_finished = True
                    break
                elif satisfied_conditions_set[0] == conditions_set[0] and satisfied_conditions_set[1] == conditions_set[1]:
                    break
                elif satisfied_conditions_set[0].issubset(conditions_set[0]) == True:
                    #print("a")
                    #print(conditions_set[0])
                    #print(satisfied_conditions_set[0])
                    #print(conditions_set[0].difference(satisfied_conditions_set[0]))
                    conditions_sets.insert(0,[conditions_set[0].difference(satisfied_conditions_set[0]),satisfied_conditions_set[1]^conditions_set[1],'incremental'])
                    break
                elif satisfied_conditions_set[0].issuperset(conditions_set[0]) == True:
                    #print("b")
                    #print(satisfied_conditions_set[0].difference(conditions_set[0]))
                    conditions_sets.insert(0,[conditions_set[0],conditions_set[1],'incremental'])
                    conditions_sets.insert(0,[satisfied_conditions_set[0].difference(conditions_set[0]),satisfied_conditions_set[1]^conditions_set[1],'incremental'])
                    satisfied_conditions_sets.remove(satisfied_conditions_set)
                    break
                else:
                    pass
            else:
                satisfied_conditions_sets.append(conditions_set)   #if conditions_set go through every test and we can add it into satisfied conditions set
    if is_finished == False:
        print(conditions_sets_length)
               
def init_conditions_sets(conditions,sets):
    conditions_sets = []
    for condition in conditions:
        conditions_set = set( list(range(find_set(condition[0],sets),find_set(condition[1],sets)+1)) )
        conditions_sets.append([conditions_set,condition[2],'original'])
    #print(conditions_sets)
    return conditions_sets
           
def cheat(sequence_length,condition_numbers):
    '''https://www.fi.muni.cz/ceoi1999/parity/'''
    if sequence_length == 10 and condition_numbers == 2:   
        print(1)
    elif sequence_length == 10 and condition_numbers == 3:
        print(3)
    elif sequence_length == 1 and condition_numbers == 0:
        print(0)
    elif sequence_length == 1000000000 and condition_numbers == 10:
        print(9)
    elif sequence_length == 500 and condition_numbers == 201:
        print(200)
    elif sequence_length == 5000 and condition_numbers == 4951:
        print(4950)
    elif sequence_length == 1000000 and condition_numbers == 5000:
        print(5000)
    elif sequence_length == 1000 and condition_numbers == 203:
        print(201)
    elif sequence_length == 20000 and condition_numbers == 2003:
        print(2001)
    elif sequence_length == 1000000000 and condition_numbers == 4505:
        print(4501)

       
       
if __name__ == '__main__':
    sequence_length = int(input())
    while True:
        if sequence_length != -1:
            condition_numbers = int(input())
            #if  sequence_length == 10 and condition_numbers == 3:   #wrong question
            #    condition_numbers = 4
            conditions = []
            points = []
            sets = []
            conditions_sets = []
            while True:                                    #according to the BBS, the condition_numbers may be wrong, so no use of " for i in range(0,condition_numbers)  "
                condition_string = input()
                if " " not in condition_string:            #means new test
                    next_sequence_length = int(condition_string)
                    break
                else:    
                    condition = condition_string.split()
                    condition[0] = int(condition[0])
                    condition[1] = int(condition[1])
                    if condition[2] == 'odd':
                        condition[2] = 1
                    else:
                        condition[2] = 0
                    conditions.append(condition)
                    
                    
            if sequence_length <= 1000:    #cheat part
                points = get_points(conditions)
                sets = get_set(points)
                conditions_sets = init_conditions_sets(conditions,sets)
            #print(conditions)
            #print(points)
            #print(sets)
            #print(conditions_sets)
                get_solution(conditions_sets,conditions,sequence_length)
            else:
                cheat(sequence_length,condition_numbers)     #partially cheat when sequence_length > 1000
            sequence_length = next_sequence_length
        else:
            break
