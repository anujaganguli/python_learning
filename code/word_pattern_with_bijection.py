# input pattern = "ABBA", string = "dog cat cat dog"
# output = true
# bijection in the above example is established as "A" maps to "dog" and "B" maps to "cat"

def word_pattern_with_bijection(pattern, input_string):
    mapping = {}
    input_list = input_string.split()
    i=0
    output_list = []
    print(input_list)
    for letter in pattern:
        mapping[letter] = input_list[i]
        i+=1
        output_list.append(mapping[letter])
    print(mapping)
    print(output_list)
    output_string = ' '.join(output_list)
    print(output_string)
    if output_string == input_string:
        return True
    else:
        return False
print(word_pattern_with_bijection("ABBA", "dog cat cat dog")) 