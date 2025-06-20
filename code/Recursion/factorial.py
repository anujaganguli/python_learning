'''
Recursion refers to a function calling itself.
It always has a base case that returns a value. 
In addition to the base case, the code includes recursive calls to the same function.

Internally, the compiler uses stack to implement recursion.
'''

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)



print("Answer", factorial(10))