import feedbackManager as fm
from datetime import date

def musicReturn():
    with open("Rental.txt", "r") as f:
        rentals = [line.strip().split(",") for line in f]

    record_id = input("Enter the record ID you are returning: ")

    #to find rental for a record.
    rental = next((r for r in rentals if r[0] == record_id and r[2] == ""), None)

    #  to check if the record is rented
    if not rental:
        print(f"Error: Record {record_id} is not currently rented.")
        return

    # to give ratings and comments on records
    rating = input("Enter your star rating (1-5): ")
    comments = input("Enter comments (optional, press Enter to skip): ")
    if not comments:  # If comments are empty
        comments = "No comment provided"
    # fm.add_feedback(record_id, rating, comments)
    with open("Music_Feedback.txt","a") as f:
        f.write("{record_id},{rating},{comments}")

    # To update return on record
    rental[2] = str(date.today())

    # Append updated rentals back to the rental text file
    with open("Rental.txt", "a") as f:
        for r in rentals:
            f.write(",".join(r) + "\n")
            print(f"Success: Record {record_id} has been returned.")

musicReturn()




