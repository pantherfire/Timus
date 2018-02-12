'''
Created on Feb 12, 2018

@author: root
'''

def rotate_level_180(dice):     #level rotate the dice with 180 degree
    dice_target = ['0','0','0','0','0','0']
    dice_target[0] = dice[1]
    dice_target[1] = dice[0]
    dice_target[3] = dice[5]
    dice_target[5] = dice[3]
    dice_target[2] = dice[2]
    dice_target[4] = dice[4]
    for i in range(0,6):
        dice[i] = dice_target[i]

def rotate_level_90(dice):    #level rotate the dice with 90 degree
    dice_target = ['0','0','0','0','0','0']
    dice_target[0] = dice[3]
    dice_target[1] = dice[5]
    dice_target[2] = dice[2]
    dice_target[3] = dice[1]
    dice_target[4] = dice[4]
    dice_target[5] = dice[0]
    for i in range(0,6):
        dice[i] = dice_target[i]

def rotate_ver_90(dice):     #vertilize rotate the dice with 180 degree
    dice_target = ['0','0','0','0','0','0']
    dice_target[0] = dice[0]
    dice_target[1] = dice[1]
    dice_target[2] = dice[5]
    dice_target[3] = dice[2]
    dice_target[4] = dice[3]
    dice_target[5] = dice[4]
    for i in range(0,6):
        dice[i] = dice_target[i]


def rotate_for_one(dice):

    if dice[0] != '1' and dice[1] != '1':
        while dice[3] != '1':
            rotate_ver_90(dice)
        rotate_level_90(dice)
    elif dice[1] == '1':
        rotate_level_180(dice)


def rotate_for_next_min(dice):

    if dice[1] == '2':
        sec_min = '3'
    else:
        sec_min = '2'
    while dice[2] != sec_min :
        rotate_ver_90(dice)

def setup_standard_dice_strings(dice_lists,i):
    standard_dice_string = dice_lists[i][1][0] + dice_lists[i][1][1] + dice_lists[i][1][2] + dice_lists[i][1][3] + dice_lists[i][1][4] + dice_lists[i][1][5]
    if standard_dice_string not in  standard_dice_strings:
        standard_dice_strings[standard_dice_string] = [i+1]
    else:
        standard_dice_strings[standard_dice_string].append(i+1)

             
def print_dices(standard_dice_combinations):
    print(len(standard_dice_combinations))
    for standard_dice_combination in standard_dice_combinations:
        standard_dice_combination.sort()
        dice_string = ""
        for dice in standard_dice_combination:
            if dice_string == "":
                dice_string = str(dice)
            else:
                dice_string = dice_string + " " + str(dice)
        print(dice_string)
                   

if __name__ == '__main__':
    dice_num = int(input())
    dice_lists = []
    
    for i in range(0,dice_num):
        dice = input().split()
        dice_lists.append([i+1,dice,0])
    #print(dice_lists)

    standard_dice_strings = {}
    standard_dice_combinations = []
    
    for i in range(0,dice_num):

        rotate_for_one(dice_lists[i][1])            #put 1 for the left of the dice
        rotate_for_next_min(dice_lists[i][1])       #put 2 or 3 for the top of the dice 
        setup_standard_dice_strings(dice_lists,i)   #set up dict for dices, putting different dice into one list
        
    #print(dice_lists) 
    for dices in standard_dice_strings.values():
        standard_dice_combinations.append(dices)     #set up dice combinations 
        
    standard_dice_combinations.sort(key= lambda dice_combination:dice_combination[0], reverse=False)   #sort the dice combinations according to first element in it
    
    #print(standard_dice_combinations)
    print_dices(standard_dice_combinations)
    