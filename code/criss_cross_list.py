def criss_cross(list1, list2):
    list3 = []
    i=0
    for i in range(len(list1)):
        list3.append(list1[i])
        list3.append(list2[i])
    return list3
    
print(criss_cross([3,2,1], [1,2,3]))