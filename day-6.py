#Simple function without parameter/argument
def greetings():
    name = input("Enter your name please: ")
    print(f"Hello {name}")

greetings()

#Function with parameters
def full_name(first_name, last_name):
    print(first_name + " " + last_name)

first_name = input("Enter your first name : ")
sur_name = input("Enter your sur name: ")
full_name(first_name, sur_name)

