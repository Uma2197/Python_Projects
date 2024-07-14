import art

print(art.logo)
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with highest bid ${highest_bid} ")


while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("How much is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
