import subscriptionManager as sm
from datetime import date

def RentMusic():
    #to validate customer subscription
    customer_id = input("Please enter your customer ID?: ")

    subscriptions = sm.load_subscriptions()  # to load subcription data
    if not sm.check_subscription(customer_id, subscriptions):
        print(f"Error: Customer {customer_id} does not have an active subscription.")
        return
    
    record_id = input("What record are you trying to rent? ")

    with open("Music_info.txt") as f:
        records = [line.strip().split(",") for line in f]
    with open("Rental.txt") as f:
        rentals = [line.strip().split(",") for line in f]


    if any(rental[0] == record_id and rental[2] == "" for rental in rentals):
        print(f"Error: Music record {record_id} does not exist.")
        return    
    
    if any(rental[0] == record_id and rental[2] == "" for rental in rentals):
        print(f"Error: Music record {record_id} is already rented.")
        return
    
    with open("Rental.txt", "a") as f:
        f.write(f"\n{record_id},{date.today()},,{customer_id}")
        print(f"Success: Record {record_id} rented.")

RentMusic()

     

 
    