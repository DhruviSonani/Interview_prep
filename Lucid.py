#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

# runs with all test cases and complexities
def minimumOperations(numbers):
    # Write your code here
    container = []
    min_opration =0
    
    for x in numbers:        
        index_l = bisect.bisect_left(container, x)
        index_r = bisect.bisect_right(container, x)
        
        index = index_l        
            
        bisect.insort_left(container, x)
        if index == 0 or index == len(container) - 1:
            min_opration += 1
        else:            
            k = min([ (len(container) - index_r -1 )*2 + 1,  (len(container) - index_l -1 )*2 + 1, index_r*2 + 1, index_l*2 + 1])
            min_opration += k            
    return min_opration

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = minimumOperations(numbers)

    fptr.write(str(result) + '\n')

    fptr.close()
