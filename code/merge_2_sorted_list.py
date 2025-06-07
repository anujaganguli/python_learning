def easy_merge(list1, list2):
    # concatinating 2 lists
    print(list1 + list2)
    # merging 2 lists and sorting
    print("merged_list:" , sorted(list1+list2))
 
def merge_2_lists_with_logic(list1, list2):
    i = 0 
    j = 0
    list_merge = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list_merge.append(list1[i])
            i+=1
        else:
            list_merge.append(list2[j])
            j+=1

    list_merge.extend(list1[i::])
    list_merge.extend(list2[j::])
    

    print("merged list:", list_merge)

easy_merge([1,2,7], [3,4,5])

merge_2_lists_with_logic([1,2,7], [3,4,5])