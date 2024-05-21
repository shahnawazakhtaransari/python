"""Write a Python program that creates all possible strings
 using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once."""
import random
letters =['a','e','i','o','I']
random.shuffle(letters)
print(''.join(letters))#concatenates all the characters in the letters list into one string. 
#The '' (empty string) is the separator, meaning the characters are joined without any separator between them.



#==========this is used to print all possible combinations from 1 digit to 5 with repetition=====================
# import itertools
# letters =['a','e','i','o','I']
# for i in range(1,5+1):
#     print(list(itertools.combinations(letters, i))) 
