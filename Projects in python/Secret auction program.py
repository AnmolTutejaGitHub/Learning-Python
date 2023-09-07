# from replit import clear
#tou can call clear() to clear the output on the console.
import os

#from art import logo
#print(logo)

bids={} #dictionary to store bidders name and price
def find_highest_bidder(bidding_record):
 highest_bid=0
 winner=''
 #bidding_record is dictionary
 for bidder in bidding_record:
  bid_amount=bidding_record[bidder]
  if bid_amount>highest_bid:
   highest_bid=bid_amount
   winner=bidder
 print(f"The winner is {winner} with bid of ${highest_bid}")
  
bidding_finished=False
while not bidding_finished:
 name=input("What is your name?")
 price=int(input("what is your bid? $"))
 bids[name]=price #dictionary[key]=value
 should_continue=input("Are there any other bidders?Type 'yes' or 'no' ").lower()
 if should_continue=="no":
  bidding_finished=True
  find_highest_bidder(bids)
 elif should_continue=="yes":
  #clear()
  os.system('clear')
 