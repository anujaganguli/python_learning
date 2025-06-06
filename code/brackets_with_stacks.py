def push(element):
    my_list.append(element)

def is_empty():
    if my_list == []:
        return True
    else:
        return False
    
def pop():
    if is_empty():
        return "The list is empty."
    else:
        last_element = my_list[-1]
        del my_list[-1]
        return last_element

my_list = []
expression = "((9+2)*5-9(7-0))-19)"

for char in expression:
    push(char)
    
print(my_list)

def check_bracket():
    open = 0 
    closed = 0
    while not is_empty():
        element = pop()
        if element == '(':
            open += 1 
        elif element == ')':
            closed += 1 
    return open == closed

print(check_bracket())


