def print_message(message, repeat_count=1):

  for i in range(repeat_count):
    print(message)



message = input("Enter a message: ")
repeat_count = int(input("Enter a repeat count (optional): "))



print_message(message, repeat_count)
