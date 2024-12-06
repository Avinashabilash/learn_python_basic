import os 
#print("*******Welcome to the silent auction Program********")

#def silent_auction():
    #bids = {}
    #end_of_bidding = False

    #while not end_of_bidding:
        #name = input("What is your name?: ")
        #bid_amount = int(input("Enter your bid amount: $"))
        #bids[name] = bid_amount
        #option = input("Are there any other bidders? (y/n): ").lower()
        #if option == "n" or option == "no":
            #end_of_bidding = True
        #elif option =="yes" or "y":
           #os.system('cls') 

    #highest_bidder = max(bids, key=bids.get)
    #highest_bid = bids[highest_bidder]
    #print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")

#silent_auction()
#n=10
#factorial=1
#for i in range(1,n+1):
    #factorial*=i
    #print(f"{factorial}")

fibonacci=[0,1]
for i in range(1,10):
    s=fibonacci[-2]+fibonacci[-1]
    fibonacci.append(s)
    print(s)
