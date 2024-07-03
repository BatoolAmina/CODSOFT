
import random


Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("WELCOME TO THE PYPASSWORD GENERATOR!")

length = int(input("Please provide the Length of the Password: "))
NLetters = int(input("How many letters would you like in your password?: "))
NSymbols = int(input("How many symbols would you like in your password?: "))
NNumbers = int(input("How many numbers would you like in your password?: "))

if length != (NLetters+NNumbers+NSymbols):
    print("Incorrect Input")
else:
    passwordList = []
    while(len(passwordList) != length):
        for char in range(1, NLetters + 1):
            passwordList.append(random.choice(Letters))
            
        for char in range(1, NSymbols + 1):
            passwordList.append(random.choice(Symbols))
            
        for char in range(1, NNumbers + 1):
            passwordList.append(random.choice(Numbers))
    
    random.shuffle(passwordList)
    
    password = ""
    
    for char in passwordList:
        password += char
        
    print(f"Your password is: {password}")