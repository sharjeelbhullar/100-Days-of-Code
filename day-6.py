# #Simple function without parameter/argument
# def greetings():
#     name = input("Enter your name please: ")
#     print(f"Hello {name}")

# greetings()

# #Function with parameters
# def full_name(first_name, last_name):
#     print(first_name + " " + last_name)

# first_name = input("Enter your first name : ")
# sur_name = input("Enter your sur name: ")
# full_name(first_name, sur_name)



num = int(input("Enter the total number of people in the group: "))
age = []
for i in range(0, num):
    entry = int(input("Enter your age: "))
    age.append(entry)

print(age)

ticket = 0
def get_ticket_price(age):
    if age < 12 and age > 0:
        ticket = 5
        return ticket
    elif age >= 12 and age <= 64:
        ticket = 10
        return ticket
    elif age >= 65:
        ticket = 7
        return ticket
    else:
        print("Please enter a valid age.")

total_bill = 0
for i in age:
    total_bill += get_ticket_price(i)

print(total_bill)