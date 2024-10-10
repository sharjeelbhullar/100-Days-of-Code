def calculate_love_score(name1, name2):
    full_name = (name1 + name2).upper()
    value1 = 0
    value2 = 0
    checker = "TRUE"
    for i in checker:        
        count = full_name.count(i)
        value1 += count
        print(f"{i} occurs {count} times")
    print(f"Total = {value1}")

    checker = "LOVE"
    for i in checker:        
        count = full_name.count(i)
        value2 += count
        print(f"{i} occurs {count} times")
    print(f"Total = {value2}")

    love_score = str(value1) + str(value2)
    print(f"Love score = {love_score}")

your_name = input("Enter your name: ")
partner_name = input("Enter your partner name: ")
calculate_love_score(your_name, partner_name)