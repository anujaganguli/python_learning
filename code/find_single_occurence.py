# given a non-empty list of integers, every element appears twice except for one. find that single occurence.
# example: input = [2,2,3,3,10,10,9] , output = 9
def find_single_occurence(input_list):
    counts = {}
    for integer in input_list: 
        if integer in counts:
            counts[integer] +=1
        else:
            counts[integer] = 1
    for key, value in counts.items():
        if value ==1:
            return key
        
print(find_single_occurence([2,2,3,3,10,10,9]))
    
print(find_single_occurence([2,2,3,3,4,4]))
    
