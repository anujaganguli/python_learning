    # remove duplicates from a sorted list
    # input = [1,1,2,2,3,4,4,5,6,7,7]
    # outut = [1,2,3,4,5,6,7]

def rm_dups_fr_sorted_list(list1):
    unique_list = [list1[0]]  
    for element in list1:
        if element != unique_list[-1]:  
            unique_list.append(element)
    print(unique_list)

rm_dups_fr_sorted_list([1,1,2,2,3,4,4,5,6,7,7])


