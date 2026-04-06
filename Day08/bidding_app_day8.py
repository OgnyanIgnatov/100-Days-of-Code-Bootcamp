
def biddingApp():
    print("Welcome to the Bid Auction!")
    people_available = True

    bidders = {}
    max_bid = 0

    while people_available: 
        name = input("What is your name?: ")
        bid = float(input("How much would you like to bid?: $"))

        if bid > max_bid:
            max_bid = bid

        bidders[name] = bid
        other_people = input("Are there any other people? Y/N: ")

        if other_people == 'N':
            people_available = False
        elif other_people == "Y":
            print("\n" * 100)

    for person in bidders:
        if bidders[person] == max_bid:
            print(f"The winner is {person} with bid of ${max_bid}")

biddingApp()
    
     

    

    

