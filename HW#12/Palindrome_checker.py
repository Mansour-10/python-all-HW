def is_palindrome(tandf):
  if tandf == tandf[::-1]:
    return True
  else:
    return False
  
print(is_palindrome("radar")) 
print(is_palindrome("Python"))  