# Given an array of positive or negative integers

# I= [i1,..,in]

# you have to produce a sorted array P of the form

# [ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

# P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

# Example:

# I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
# [2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

# Notes:

# It can happen that a sum is 0 if some numbers are negative!
# Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
import math
from collections import defaultdict 

def isPrime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def find_prime_factors(number):
    factors = [i for i in range(2, int(number/2 + 1)) if number % i == 0 and isPrime(i)]
    if isPrime(number):
        factors.append(number)
    return factors

def sum_for_list(lst):
    sum_list = defaultdict(int)
    for number in lst:
        for factor in find_prime_factors(abs(number)):
            # if factor in sum_list.keys():
            sum_list[factor] += number
            # else:
            #     sum_list[factor] = number
    return sorted(list(map(list, sum_list.items())))

print(sum_for_list([200, -21, -60, -130, -92, 135, -133, -86, -131, -122, 16, -145, -124, -93, -96]))