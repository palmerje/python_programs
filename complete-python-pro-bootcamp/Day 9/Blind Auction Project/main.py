import art

print(art.logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bidding_auction = {}
any_other_bidders = "yes"

while any_other_bidders == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid?  $"))
    any_other_bidders = input("Are there any other bidders? type yes or no  ")
    bidding_auction[name] = bid
    if any_other_bidders == "yes":
        print("\n"*100)


winning_bidder = ""
winning_bid = 0
for bidder in bidding_auction:
    if bidding_auction[bidder] > winning_bid:
        winning_bidder = bidder
        winning_bid = bidding_auction[bidder]
print(f"The winner is {winning_bidder} with a bid of ${winning_bid}!!")

