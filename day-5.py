#Easy level
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for i in range(1, nr_letters +1):
    password += random.choice(letters)

for i in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for i in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

#Hard level
n1 = int(input("Enter a minimum of letters in your password: "))
n2 = int(input("Enter a minimum of symbols in your password: "))
n3 = int(input("Enter a minimum of numbers in your password: "))
password_list = []
for i in range(1, n1+1):
    password_list.append(random.choice(letters))

for i in range(1, n2+1):
    password_list.append(random.choice(symbols))

for i in range(1, n3+1):
    password_list.append(random.choice(numbers))


print(password_list)
random.shuffle(password_list)
print(f"Password after shuffling: {password_list}")

password = ""
for i in password_list:
    password += i

print(f"Your password is {password}")
