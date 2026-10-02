import random

start = 1
end = 10

def guess(a, b):
    count = 0
    num = random.randint(start, end)
    flag = False
    while (not flag):
        guess = int(input("Please guess a number within 1 to 10, inclusive: "))
        count = count + 1
        if(guess == num):
            print(f"Congrats! You guessed correctly in {count} guesses!")
            flag = True
        elif(guess < num):
            print("Beep Boop! Too low")
        elif(guess > num):
            print("beep Boop! Too high")


def computer_guess(a, b):
    count = 0
    feedback = "H"
    while feedback != "c":
        if (a == b):
            a = guess
        else:
            guess = random.randint(a, b)
        count = count + 1

        print(f"I'm guessing {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            b = guess - 1
        elif feedback == "l":
            a = guess + 1
            
    print(f"Amount of guesses: {count}")


#guess(start, end)
computer_guess(1, 10)
