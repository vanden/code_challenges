#!/bin/python3

# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    zero_count, positive_count = 0, 0
    for num in arr:
        if num == 0:
            zero_count += 1
        elif num > 0:
            positive_count += 1
    negative_count = len(arr) - (zero_count + positive_count)
    print('%.6f' %(positive_count/len(arr)))
    print('%.6f' %(negative_count/len(arr)))
    print('%.6f' %(zero_count/len(arr)))
