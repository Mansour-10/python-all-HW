""" 
1 - Create a function named is_even that takes an integer
as a parameter and returns true if the number is even, otherwise false.

2 - Demonstrate the usage of this function by checking whether the number 22 is even or odd.   """


def is_even(check):
    if check % 2 == 0:
        return True
    else:
        return False

print(is_even(22)) 

