#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a python program to find the largest number in a list
numbers = [10,2,4,7,5]

def largest_num(numbers):
    print("Largest number in list =", max(numbers)) 
    
largest_num(numbers)


# In[10]:


#Write a function called hexagon_area that takes the length of a side of a regular hexagon as a parameter and returns the area of hexagon
import math

def hex_area(side):
    area = ((3*math.sqrt(3))*side*side)/2
    print('area of hexagon =', area, 'square units')
    
hex_area(5)


# In[11]:


#Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.

import re

def is_valid_email(email):
    # Define a regular expression pattern for a valid email address
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9._%+-]{0,63}@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email) and len(email) <= 256:
        return True
    else:
        return False

# Example usage:
email_address = "user@example.com"
if is_valid_email(email_address):
    print(f"The email address {email_address} is valid.")
else:
    print(f"The email address {email_address} is not valid.")


# In[12]:


#Create a function called encrypt that takes some text(String) and a Shift(Integer)and
#then encrypts the text using the Caesar Cipher algorithm, returning the encrypted text.

#Create a second function to decrypt an encrypted string, using the same input
#parameters and returning the decrypted text.

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


# In[13]:


text = "Hello, World!"
shift = 3

encrypted_text = encrypt(text, shift)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted:", decrypted_text)


# In[14]:


#Create a function called get_palindromes that is given a string and returns a list of all
#the palindromes in the string.
def get_palindromes(s):
    # Function to check if a substring is a palindrome
    def is_palindrome(sub):
        return sub == sub[::-1]

    palindromes = []
    s = s.lower()  # Convert the string to lowercase for case-insensitive comparison
    words = s.split()  # Split the string into words

    for word in words:
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                substring = word[i:j]
                if is_palindrome(substring) and len(substring) > 1:  # Check if substring is a palindrome
                    palindromes.append(substring)

    return palindromes


# In[15]:


string = "abba racecar madam level hello anna noon"
palindrome_list = get_palindromes(string)
print("Palindromes:", palindrome_list)


# In[ ]:




