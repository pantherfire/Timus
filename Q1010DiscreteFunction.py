'''
Created on Feb 6, 2018

@author: root
'''

'''
the key point of this quesiton is that the result must be 2 continous numbers
'''


def get_point_dicts(points_num):
    points_dicts = {}
    for i in range(1,points_num + 1):
        y_value = int(input())
        points_dicts[i] = y_value
    return points_dicts

def print_pair(points_dicts,points_num):
    largest_inclination = None
    min_x_value = 1
    for i in range(2,points_num + 1):
        inclination = abs(points_dicts[i] - points_dicts[i-1])
        if largest_inclination == None:
            largest_inclination = inclination
            min_x_value = i - 1
        else:
            if inclination > largest_inclination:
                largest_inclination = inclination
                min_x_value = i - 1
    print(str(min_x_value) + " " + str(min_x_value + 1))
                
            

if __name__ == '__main__':
    points_num = int(input())
    points_dicts = get_point_dicts(points_num)
    print_pair(points_dicts,points_num)