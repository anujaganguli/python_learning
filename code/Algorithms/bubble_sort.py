'''
bubble sort: one of the simplest sorting algorithms that works by repeated swapping the last elements if they are in the
wrong order

example: 
arr: [5,6,1,3]
i = 0
i = 1 [5,1,6,3]
i = 2 [5,1,3,6]
i = 0 [1,5,3,6]

and repeat
'''

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sort([15,6,26,13,100,45,2,7]))