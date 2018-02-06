if __name__ == '__main__':
    num_stones = input()
    stone_string = input()
    stones_string = stone_string.split()
    stones_int = []
    sum = 0
    for stone_string in stones_string:
        stones_int.append(int(stone_string))
        sum += int(stone_string)
   
    #stones_int.sort()   
    #print(stones_int)
   
   
    sum_set = set([])
   
    while stones_int:
        sum_set_adding = set([])
        stone_chosen = stones_int.pop()
        if len(sum_set) == 0:
            if stone_chosen <= sum / 2:
                sum_set_adding.add(stone_chosen)
        else:
            for sum_element in sum_set:
                if sum_element + stone_chosen <= sum / 2:
                    sum_set_adding.add(sum_element + stone_chosen)
        sum_set = sum_set.union(sum_set_adding)
        #print(sum_set)
   
    if len(sum_set) == 0:
        print (sum)
    else:   
        print ( sum - 2 * max(list(sum_set)))               
