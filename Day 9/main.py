#Blind Auction Project
from art import logo

def find_highest_bidder(bidding_collection):
    highest_bid = 0
    winner = ""
    for bidder in bidding_collection:
        bid_amount = bidding_collection[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


print(logo)
print("Welcome to the secret auction program.")
wanna_run_again = True
bidding_data = {}
while wanna_run_again:
    name = input("What is your name?: ")
    bid_price = int(input("What's your bid: $"))

    bidding_data[name] = bid_price

    bidders = input("Are there are any other bidders? Type 'yes' or 'no'.").lower()
    if bidders == "yes":
        wanna_run_again = True
        print("\n" * 100)
    else:
        wanna_run_again = False
        print("")
        find_highest_bidder(bidding_collection=bidding_data)

# top_bidder = max(bidding_data, key=bidding_data.get)
# highest_bid = bidding_data[top_bidder]




