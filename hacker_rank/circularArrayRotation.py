#!/bin/python3

# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, m):
    arr = a[len(a)-(k%len(a)):] + a[:len(a)-(k%len(a))]
    results = []
    for index in m:
        results.append(arr[index])
    return results
