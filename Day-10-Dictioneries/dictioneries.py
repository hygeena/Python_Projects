# collection={"function":"peice of code which calls again and again",
#             "bug":"error in the program",
#             "intellicence":"werwerwerew"}

# # collection={"newadd":"asasdasdasd"}
# collection["newadd"]="new additon"
# print(collection)
# for i in collection:
#     print(collection[i])

#aution bid program
auction={}
auction_child={}
participant=True
while participant:
    name=input("enter name of the participant")
    bid=input("enter the amount")
    auction[name]=bid
    play=input("Do you want to add more particpants? yes or no")
    if play=="yes":
        participant=True
    else:
        participant=False
participant==False
highest_bid=0
if participant==False:
    for bid in auction:
        bid_amount=int(auction[bid])
        if bid_amount>highest_bid:
            highest_bid=bid_amount
print(highest_bid)

