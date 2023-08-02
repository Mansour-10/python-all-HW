""" Default parameter value
1 - Create a py function names print_message that takes 
a parameter message and a parameter repeat_count value of 1.

2 - the function should print he message the number of times specified 
by repeat_count.

3 - Prompt the user to enter a message and a repeat count(optional).

4 - call the print_message function with the user-provided values or using the default value. """


def print_message(message, repeat_count=1):

  for x in range(repeat_count):
    print(message)



message = input("Hello, Welcome to UCA (please press enter) ")
repeat_count = input("What is you're name:")