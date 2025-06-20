'''
sorts an array by repeatedly selecting the smallest or the largest element from the unsorted portion and swapping it 
with the first unsorted element
start from the first element at index 0 
find the smallest element in the rest of the array
swap the smallest element with the current element
example:
arr = (64, 25, 12, 22, 11)
swap 64 with 11 
move to next element and repeat
'''

# length of array: len(arr)
# iterating an array: for i in range(n-1) where n is the size of the array
# accessing element at an index: arr[i]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        print("Iteration:", arr)
        placeholder = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = placeholder
    return arr

print("Original array:", [64,25,12,22,11])
print("Sorted array:", selection_sort([64, 25, 12, 22, 11]))

