# Search for music record
mMatrix = []
try:
    with open("Music_info.txt", "r") as f:
        f.readline()
        for line in f:
            s = line.strip()
            if not s:
                continue
            fields = s.split(",")
            if len(fields) < 5:
                continue
            mMatrix.append([item.strip() for item in fields])
except FileNotFoundError:
    print("Error: 'Music_info.txt' not found.")
    exit()
# Display options on the menu
def display_menu():
    print("Menu")
    print("h) say Hi!")
    print("b) say Bye!")
    print("a) Search music by artist")
    print("g) Search music by genre")
    print("q) Quit")

# Search artist from the text file
def getArtist():
    sArtist = input("Which artist are you after? ").strip().lower()
    found = False
    for i in range(len(mMatrix)):
        if mMatrix[i][1].lower() == sArtist:
            print("Record_ID =", mMatrix[i][0],
                  "Medium =", mMatrix[i][3],
                  "Title =", mMatrix[i][2],
                  "Genre =", mMatrix[i][4])
            found = True
    if not found:
        print("Artist does not exist in the record.")

# Search for genre from the text file
def getGenre():
    sGenre = input("What genre are you after? ").strip().lower()
    found = False
    for i in range(len(mMatrix)):
        if mMatrix[i][4].lower() == sGenre:
            print("Record_ID =", mMatrix[i][0],
                  "Medium =", mMatrix[i][3],
                  "Title =", mMatrix[i][2],
                  "Artist =", mMatrix[i][1])
            found = True
    if not found:
        print("Genre does not exist.")

def CLI_menu():
    while True:
        display_menu()
        option = input("Please enter your option: ").strip().lower()
        if option == "h":
            print("Hi")
        elif option == "b":
            print("Bye")
        elif option == "a":
            getArtist()
        elif option == "g":
            getGenre()
        elif option == "q":
            print("Bye bye, end of the program.")
            break
        else:
            print("Invalid option. Please select a valid menu option.")

CLI_menu()
