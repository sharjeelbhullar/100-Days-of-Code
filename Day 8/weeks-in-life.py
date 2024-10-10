def weeks_in_life(age):
    target_age = 90
    years_left = target_age - age
    weeks_left = years_left * 52
    print(f"You have {weeks_left} weeks left.")

age = int(input("Enter your current age: "))
weeks_in_life(age)