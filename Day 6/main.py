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


#Total number of people
num = int(input("Enter the total number of people in the group: "))
age = []
#Loop for taking entry of age from the user
for i in range(1, num+1):
    entry = int(input(f"Enter the age of person {i}: "))
    age.append(entry)

ticket = 0
#Function to check age and select the price of ticket
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
#Function calling and making total bill of the ticket
for i in age:
    total_bill += get_ticket_price(i)

print(f"Total cost for the group: ${total_bill}")