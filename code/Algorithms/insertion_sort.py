'''
insertion sort: start with the second element of the array as the first element is assumed to be sorted

compare the second element with the first element 
if the second element is smaller than the first element then swap them
move to the third element
compare it with the first two elements 
put it in its correct position
repeat until entire array is sorted

example:
initially: [23,1,10,5,2]
first pass: [1,23,10,5,2]
second pass: [1,10,23,5,2]
third pass: [1,5,10,23,2]
fourth pass: [1,2,5,10,23]

Hint: key = the one ur pivoting
'''

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        idx = i-1
        while idx >= 0 and arr[idx] > key:
            arr[idx+1] = arr[idx]
            idx -= 1
        arr[idx+1] = key
        print("Iteration:", arr)
    return arr

print(insertion_sort([23,1,10,5,2]))