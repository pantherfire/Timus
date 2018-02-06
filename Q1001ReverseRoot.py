import math

def reverse_root():
    nums = []
    while True:
        try:
            line = input()
            if line == "EOF":     #simulate the EOF when debugging since cannot input EOF in console
                break
            else:
                line_nums = line.split()
        except:
            break
        
        for line_num in line_nums:
            nums.append( int(line_num) )
    while nums:
        num = int(nums.pop())
        print( str( math.sqrt( num ) ) )   
         
         
reverse_root()
