""" 
1 - Create a function named is_vowel that takes
a character (a single letter) as a parameter and returns 
true if it's a vowel (a,e,i,o,u both uppercase and lowercase),
otherwise false.

2 - Demonstrate  the usage of this function by chechking 
'a' , 'b' , 'E' and 'Z' are vowels """



def is_vowel(letters):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if letters in vowels:
      return True
    else:
      return False
    
print(is_vowel('a'))  
print(is_vowel('b')) 
print(is_vowel('E'))
print(is_vowel('Z'))    