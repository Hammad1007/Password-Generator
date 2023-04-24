# Code here for the password generator

# Generates a random password for your email id, facebook or for whatever purpose you want

import random       # random library to take in random values

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

password = []         # an empty list
str_password = " "    # an empty string

size_letters = int(input("Enter the number of letters you want in your password: "))
size_symbols = int(input("Enter the number of symbols you want in your password: "))
size_numbers = int(input("Enter the number of numbers you want in your password: "))

if size_letters + size_numbers + size_symbols < 8:
    print("The password length is not valid. Kindly enter a valid length for the password.\n")

else:
    for letter in range(1, size_letters + 1):
        char = random.choice(letters)
        password.append(char)
        
    for symbol in range(1, size_symbols + 1):
        char = random.choice(symbols)
        password.append(char)
        
    for number in range(1, size_numbers + 1):
        char = random.choice(numbers)
        password.append(char)

    random.shuffle(password)

    for char in password:
        str_password += char
        
    print("The password is:",str_password)
