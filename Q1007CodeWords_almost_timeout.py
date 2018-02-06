'''
Created on 2018 Feb 1st
@author: surface
'''






def format_code(code):
    formatted_code = ""
    for i in range(0,len(code)):
        if code[i] != " ":
            formatted_code += code[i]
    return formatted_code

def init_code(original_code):
    code_info = []
    sum = 0
    count = 0
    for position in range(1,len(original_code)+1):
        reverse_position = len(original_code) + 1  - position    #from the last one
        if original_code[reverse_position -1] == '1':
            sum += reverse_position             #sum is the sum of rest position which is after this postion (including its self)
            count += 1
        else:
            pass
        code_info.append([reverse_position,original_code[reverse_position-1],sum,count])
    code_info.sort(key=lambda combination:combination[0], reverse=False)
    #print(code_info)
    return code_info

def print_code(code_info):
    #print(code_info)
    code = ""
    for i in range(0,len(code_info)):
        code = code + code_info[i][1]
    print(code)
    
def replace_fix(code_info,word_length):
    sum = code_info[0][2]
    if sum % (word_length + 1) == 0:       # no need to fix
        print_code(code_info)
        return 

    cut_value = (sum % (word_length + 1))

    cut_position = cut_value

    if cut_position <= word_length and cut_position >= 1  and code_info[cut_position-1][1] == '1':   #   1 -> 0
        code_info[cut_position-1][1] = '0'
        print_code(code_info)
        return 
    else:
        return
    
       
def fill_fix(code_info,word_length):
    sum = code_info[0][2]
    if (sum + word_length) % (word_length + 1) == 0:         # add 1 at the end of code
        code_info.append( [str(word_length),"1",None,None] )
        print_code(code_info)
        return 
    elif (sum ) % (word_length + 1) == 0:          # add 0 at the end of code
        code_info.append( [str(word_length),"0",None,None] )
        print_code(code_info)
        return 
    for position in range(1,len(code_info) + 1):
        if ( sum + position + code_info[position - 1][3] ) % (word_length + 1) == 0:
            code_info.insert(position-1 ,[str(position)+"a","1",None,None] )
            print_code(code_info)
            return 
        elif ( sum +  code_info[position - 1][3] ) % (word_length + 1) == 0:
            code_info.insert(position-1 ,[str(position) + "a","0",None,None] )
            print_code(code_info)
            return 
    return
        
def cut_fix(code_info,word_length):
    sum = code_info[0][2]
    for position in range(1,len(code_info) + 1):
        #print(position)
        #print(code_info[position - 1][3])
        if ( sum - position - ( code_info[position - 1][3] -1) ) % (word_length + 1) == 0 and code_info[position-1][1] == '1':   # removing a "1" will compensate moving the rest 1s left
            del(code_info[position-1] )
            print_code(code_info)
            return 
        elif ( sum  - code_info[position - 1][3]  ) % (word_length + 1) == 0 and code_info[position-1][1] == '0':
            del(code_info[position-1] )
            print_code(code_info)
            return 
    return 


                              
word_length = int(input())
while True:
    try:
        #formatted_code = format_code(input())   #removing any extra spaces in code input
        formatted_code = input().replace(" ", "")    #no idea why replace() is faster than my format_code()
        if formatted_code == "":                 #ignore the blank lines
            continue
        elif formatted_code == "EOF":
            break
        #print(" ")
        #print(formatted_code)
        code_info = init_code(formatted_code)      
        #print(code_info)
        if len(formatted_code)  == word_length:     #if the len of code is equal to word length, we need to check  if 1->0
            replace_fix(code_info,word_length)
        elif len(formatted_code) < word_length:    #if the len of code is smaller than word length, we need to add a 0/1 to it
            fill_fix(code_info,word_length)
        elif len(formatted_code) > word_length:    #if the len of code is bigger than word length, we need to cut a 0/1 to it
            cut_fix(code_info,word_length)
    except:
        break
