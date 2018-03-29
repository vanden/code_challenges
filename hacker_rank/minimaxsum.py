#!/bin/python3

# https://www.hackerrank.com/challenges/mini-max-sum/problem

import os
import sys

def miniMaxSum(arr):
    nums = sorted(arr)
    print( sum(nums[:4]), sum(nums[1:]))

