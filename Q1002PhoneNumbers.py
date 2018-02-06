'''
Created on Jan 24, 2018

@author: root
'''

def phone_dict_input(phonestring):
    dict_line_num = int (input())
    dicts = {}
    for i in range(0,dict_line_num):
        transformed_word = transform(input())
        dicts[transformed_word[0]] = transformed_word[1]
    phone_with_dicts =  { phonestring : dicts }  
    return phone_with_dicts   
    
def transform(word):
    transformed_word = ''
    for i in range(0,len(word)):
        letter = word[i]
        #print (letter)
        if letter in 'ij':
            num = '1'
        elif   letter in 'abc':
            num = '2'
        elif   letter in 'def':
            num = '3'
        elif   letter in 'gh':
            num = '4'  
        elif   letter in 'kl':
            num = '5'
        elif   letter in 'mn':
            num = '6'
        elif   letter in 'prs':
            num = '7'
        elif   letter in 'tuv':
            num = '8'
        elif   letter in 'wxy':
            num = '9'
        elif   letter in 'oqz':
            num = '0'   
        transformed_word = transformed_word + num
        
    return   [transformed_word, word]           


def match(phone_string,dict_keys):
    '''return all the substr combination of phone_string according to dict_keys
    '''
    num_combinations = []
    num_combination = []

    for dict_key in dict_keys:
        if dict_key > phone_string:
            break
        if phone_string.startswith(dict_key) == True:
            if phone_string == dict_key:
                num_combination = [[dict_key]] 
            else:
                num_combination = listadd( [[dict_key]] , match(phone_string[len(dict_key):] ,dict_keys[:]) )

            if num_combinations == []:
                num_combinations = num_combination
            else:     
                num_combinations = num_combinations + num_combination
    return num_combinations


def listadd( clist1s,clist2s):
    clist3s = []
    for clist1 in clist1s:
        for clist2 in clist2s:
            clist3s.append( clist1 + clist2 )
    return  clist3s       


def get_dict_keys(dicts):
    '''get dict_keys from dicts'''
    dict_keys = []
    for dict in dicts.keys():
        dict_keys.append(dict)
    return dict_keys

def get_solution(num_combinations,dicts):
    if  num_combinations == []:
        print ( "No solution.")
        pass
    else:
        '''get the minimal combination from all the possible combinations'''
        min_num_combination = num_combinations[0]
        for num_combination in num_combinations:
            if len(num_combination) < len(min_num_combination):
                min_num_combination = num_combination
        
        '''transform the min_number combination into words'''        
        transformed_words = ""
        for num in min_num_combination:
            if transformed_words == "":
                transformed_words = dicts[num]
            else:
                transformed_words = transformed_words + " " + dicts[num]
        print (transformed_words)  

if __name__ == '__main__':
    #print ('0342a'[2:])
    #print ( match( '03421',['0','2','1','34','3','4','421'] ) )
    #print ( match( '0342',['0','4','2','3'],0 ) )
    
    while True:
        phonestring = input()
        if phonestring != '-1':
            '''get "phonestring & dicts"  (DICT) from input'''
            phone_with_dicts = phone_dict_input(phonestring)
            #print (phone_with_dicts)
            '''get dicts (DICT) from (phonestring & dicts) (DICT)'''
            dicts =  phone_with_dicts[phonestring]
            #print (dicts)
            '''get dict keys (LIST) from dicts (DICT)'''
            dict_keys = get_dict_keys(dicts)
            dict_keys.sort()
            #print (dict_keys)
            '''get possible number combination [[LIST]] from phonestring according to dict_keys'''
            num_combinations = match (phonestring, dict_keys) 
            
            get_solution(num_combinations,dicts)
                  
        else:
            break
    