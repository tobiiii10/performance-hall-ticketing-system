import matplotlib.pyplot as plt
from collections import Counter

def identify_unpopular():
    with open ("Rental.txt") as f:
        rentals = [line.strip().split(",")[0] for line in f]

    # Count number of rentals
    rentalcounts = Counter(rentals)
    unpopular = [rec for rec, count in rentalcounts.items() if count < 3]

    labels, values = zip(*rentalcounts.items())
    plt.bar(labels , values)
    plt.title("Number of Rentals")
    plt.show()

    print(unpopular)

identify_unpopular()