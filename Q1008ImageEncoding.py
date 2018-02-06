'''
Created on Feb 5, 2018

@author: root
'''
def get_pixes_dicts(blk_pixes_nums):
    pixes_dicts = {}
    min_x = None
    lowest_y = None

    for i in range(0,blk_pixes_nums):
    
        pix = input().split()
        x_value = int(pix[0])
        y_value = int(pix[1])

    
        if min_x == None :      #when no value in min_x
            min_x = x_value
            lowest_y = y_value
        elif x_value < min_x:   
            min_x = x_value      #get smaller x first
            lowest_y = min(lowest_y, y_value)   #get smaller y for given x
        
        if x_value not in pixes_dicts:
            pixes_dicts[x_value] = {y_value:0}
        else:
            pixes_dicts[x_value][y_value] = 0

    return pixes_dicts,min_x,lowest_y


def test_xy(pixes_dicts,pending_xy,x_value,y_value):
    if x_value in pixes_dicts:
        if y_value in pixes_dicts[x_value]:
            if pixes_dicts[x_value][y_value] == 0:
                pixes_dicts[x_value][y_value] = 1
                pending_xy.append([x_value,y_value])
                #print(pixes_dicts)
                #print(pending_xy)
                return 1
    return 0
         
     
 
def print_image_code(pixes_dicts,min_x,lowest_y) :
    pending_xy = [[min_x,lowest_y]]   #init the pengding list
    pixes_dicts[min_x][lowest_y] = 1
    while pending_xy:
        directions = ""
        
        processing_xy = pending_xy[0]
        del(pending_xy[0])
        x_value = processing_xy[0]
        y_value = processing_xy[1]
        
        if test_xy(pixes_dicts,pending_xy,x_value + 1,y_value):   #R
            directions += "R"
        if test_xy(pixes_dicts,pending_xy,x_value,y_value + 1):   #T
            directions += "T"
        if test_xy(pixes_dicts,pending_xy,x_value - 1,y_value):   #L
            directions += "L"
        if test_xy(pixes_dicts,pending_xy,x_value,y_value - 1):   #B
            directions += "B"  
        #print(x_value,y_value)
        if directions == "" and  pending_xy == []:
            print(".")
        else:
            print(directions+",")

def xy2code(first_line):
    blk_pixes_nums = int(first_line)
    pixes_dicts,min_x,lowest_y = get_pixes_dicts(blk_pixes_nums)
    #print(pixes_dicts)
    print(str(min_x) + " " + str(lowest_y))
    print_image_code(pixes_dicts,min_x,lowest_y)

def get_code_lists():
    
    code_lists = []
    
    while True:
        input_line = input()
        if input_line == '.':
            code_lists.append([])
            break
        else:
            code = []
            for i in range(0,len(input_line)):
                if input_line[i] == ',':
                    break
                else:
                    code.append(input_line[i])
            code_lists.append(code)        
    
    return code_lists

def sort_and_print(chosen_xys):
    xy_lists = []
    for x,y_values in chosen_xys.items():
        xy_lists.append([x,sorted(y_values)])
    xy_lists.sort(key=lambda xys:xys[0], reverse=False)
    for xy in xy_lists:
        for y in xy[1]:
            print( str(xy[0]) + " " + str(y))


def print_xys(code_lists,init_x,init_y):
    print( len(code_lists) )
    #print(str(init_x) + " " + str(init_y))
    
    pending_xys = [[init_x,init_y]]
    chosen_xys = {}
    
    while pending_xys:
        x_value = pending_xys[0][0]
        y_value = pending_xys[0][1]
        del(pending_xys[0])
        
        
        if x_value not in chosen_xys:
            chosen_xys[x_value] = [y_value]
        else:
            chosen_xys[x_value].append(y_value)
                    
                    

        code_list = code_lists[0]
        del(code_lists[0])
        for code in code_list:
            if code == 'R':
                pending_xys.append([x_value + 1,y_value])
            elif  code == 'L':
                pending_xys.append([x_value - 1,y_value])
            elif code == 'T':
                pending_xys.append([x_value,y_value + 1])
            elif  code == 'B':
                pending_xys.append([x_value,y_value - 1])
    #print(chosen_xys)
    sort_and_print(chosen_xys)
        
    
def code2xy(first_line):
    first_line_xy = first_line.split()
    init_x = int(first_line_xy[0])
    init_y = int(first_line_xy[1])
    code_lists = get_code_lists()  
    #print(code_lists)  
    print_xys(code_lists,init_x,init_y)     
   
first_line = input()
if ' ' not in first_line:
    xy2code(first_line)
else:
    code2xy(first_line)
    
