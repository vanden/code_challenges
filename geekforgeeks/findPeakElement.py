# https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

def findPeak(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[-1] >= arr[-2]:
        return arr[-1]
    return findPeak(arr[1:-1])


def findPeak2(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]

    mid = int(len(arr) / 2)

    if arr[mid] >= arr[mid + 1] and arr[mid] >= arr[mid - 1]:
        return arr[mid]

    if arr[mid] < arr[mid + 1]:
        return findPeak2(arr[mid +1:])
    else:
        return findPeak2(arr[:mid])



print(findPeak2([5, 10, 20, 15]))# 20
print(findPeak2([10, 20, 15, 2, 23, 90, 67])) # 20 or 90
