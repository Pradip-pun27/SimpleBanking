# Top Bidder finder Program
import os
def winner(bidder_info):
    mxm=0;
    win=""
    for bidder in bidder_info:
        bidding_price=bidder_info[bidder]
        if(bidding_price>mxm):
            mxm=bidding_price
            win=bidder
    print(f"Bidder's name with their Bidding price are\n{bidder_info}")
    print(f"The Winner is {win} with a bid price of {mxm}")

Bidder_data={}
end_bidding=True

while  end_bidding:
    name =input("Enter yrs Auspicious name : ")
    price=int(input("Enter yrs bid(Rs):"))
    Bidder_data[name]=price
    more=input("Are there more Bidder? Type  'yes' and  'no' : ").lower()
    if(more=='no'):
        end_bidding=False
        winner(Bidder_data)
    elif(more=='yes'):
        os.system('cls')