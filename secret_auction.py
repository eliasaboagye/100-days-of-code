import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Welcome to the Secret Auction Program.")

bids = {}
while True:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'.\n")
    if more_bidders.lower() == "no":
        break
    clear()

highest_bid = 0
highest_bidder = ""
for name in bids:
    if highest_bid < bids[name]:
        highest_bid = bids[name]
        highest_bidder = name

print(f"This winner is {highest_bidder} with a bid of ${highest_bid}")