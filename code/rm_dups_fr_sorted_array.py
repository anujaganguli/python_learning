#works for unsorted array aswell
def rm_dups_w_set(arr):
    my_set = set()
    ind = 0
    for i in range(len(arr)):
        if arr[i] not in my_set:
            my_set.add(arr[i])
            arr[ind] = arr[i]
            ind += 1
    return ind

#works only for sorted array
def rm_dups_without_set(arr):
    ind = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[ind] = arr[i]
            ind += 1
    return ind
arr = [1,2,2,3,3,4,5]
new_size = rm_dups_w_set(arr)
print("count of unique elements =", new_size)
print("unique elements", arr[:new_size])
newsize2 = rm_dups_without_set(arr)
print("count of unique elements =", new_size)
print("unique elements", arr[:new_size])