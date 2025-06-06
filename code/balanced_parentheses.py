def check_balance_parentheses(my_string):
    open_paren = 0
    closed_paren = 0
    for char in my_string:
        if (char == '('):
            open_paren += 1 
        elif (char == ')'):
            closed_paren += 1
    return (open_paren == closed_paren)
    
print(check_balance_parentheses('(5+3))+2'))