print("======================================================================================")
print("Heyo! Welcome to a final year undergrad making a mad libs game for no apparent reason.")
print("Without further a do, let's get started.")
print("======================================================================================\n")
print("""Press: 1 to choose a mad lib
       2 to exit""")

madlibList = {"1" : "Zoo Day (Available)", 
              "2": "Beep Boop", 
              "3": "Cum Adventures",
              "9": "Exit"
              }

def madLib1():
    word1 = input("Enter an adjective: ")
    word2 = input("Enter the name of an animal: ")
    word3 = input("Enter an adjective: ")
    word4 = input("Enter a verb ending in ing: ")
    word5 = input("Enter a noun: ")
    word6 = input("Enter an adjective: ")
    word7 = input("Enter a color: ")
    word8 = input("Enter a plural noun: ")
    print("\n")
    print("-" * 15 + "X" + "-" * 20)
    print(
f"""Yesterday, I went to the zoo with my [1] {word1} friend. 
We saw a giant [2] {word2} eating a [3] {word3} snack. 
It was [4] {word4} inside the monkey [5] {word5}! 
After that, we bought some [6] {word6} ice cream that turned my tongue [7] {word7},
and we rode the [8] {word8} all the way home."""
)
    print("-" * 15 + "X" + "-" * 20)

choice = input("Your choice: ")
while choice != "2":
    if choice == "1":
        print("*"*50 + "\n")
        for num, title in madlibList.items():
            print(num + ": " + title)
        madLibNum = input("Please enter the number of the story you wish to play: ")
        while madLibNum != 9:
            if (madLibNum == "1"):
                madLib1()
                madLibNum = input("Try another title or exit: ")
            elif (madLibNum == "9"):
                choice = "2"
                break
            elif (madLibNum == "2" or madLibNum == "3"):
                print("Coming soon...")
                madLibNum = input("Try a different title or exit: ")
            else:
                madLibNum = input("Invalid input. Please try again: ")
    elif choice == "2":
        break
    else:
        choice = input("Invalid input, please try again: ")

print("="*50)
print("Exiting...")
print("="*50)


