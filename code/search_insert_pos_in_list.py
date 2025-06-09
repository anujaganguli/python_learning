# given a sorted array of integers and a target value retun the index if target is found, else return -1
# example: nums = (1,3,5,5,6,7), target = 5, output = 2

def search_target_value_in_list(input_list, target_value):
    i=0
    while i < len(input_list):
        if input_list[i] == target_value:
            return i
        else:
            if i == len(input_list) - 1:
                return -1
            else:
                i+=1

def insert_target_value_in_list(input_list, target_position, target_value):
    output_list = []
    i = 0
    while i < target_position:
        output_list.append(input_list[i])
        i+=1
    output_list.append(target_value)
    print(output_list)
    print(i)
    output_list.extend(input_list[i::])
    return output_list
    

input_list = (1,3,5,5,6,7)
target_value = 8
search_index = search_target_value_in_list(input_list, target_value)
print("target value found in position:", search_index)

target_value = 3
search_index = search_target_value_in_list(input_list, target_value)
print("target value found in position:", search_index)

insert_value = 2

print("new list after insert:", insert_target_value_in_list(input_list,search_index, insert_value))


        