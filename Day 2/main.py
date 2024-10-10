from typing import final

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# total_tip = (tip/100) * bill
# final_bill = bill + total_tip

# Or
total_tip = (1 + tip/100)
final_bill = round(bill * total_tip, 3)


print(f"Total bill = ${final_bill}")

split_bill = round(final_bill / people, 3)

print(f"Each person should pay: ${split_bill}")

