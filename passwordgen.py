import random
import string

def passwordgen(num, length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passwords = [''.join(random.choices(characters, k = length)) for i in range(num)]
    return passwords

pwNum = int(input("Enter the number of passwords: "))
length = int(input("Enter the desired password length: "))
passwords = passwordgen(pwNum, length)

print("The generated passwords are: ")
for password in passwords:
    print("- " + password)
