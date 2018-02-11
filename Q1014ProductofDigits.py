'''
Created on Feb 11, 2018

@author: root
'''

import math

def generate_prime_lists(n):
    
    primes = []
    
    if n == 1:
        return primes
    elif n == 2:
        primes = [2]
        return primes

if __name__ == '__main__':
    n = int(input())
    sqrt_n = math.floor( math.sqrt(n) )
    
    primes = generate_prime_lists(sqrt_n)
    get_and_print_q(primes,n)
        