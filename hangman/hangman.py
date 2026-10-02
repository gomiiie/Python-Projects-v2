from words import words
import random

l1 = [word for word in words
            if any(char > 'z' or char < 'a' for char in word)]

def get_word(w):
    word = random.choice(w)
    while any(char > 'z' or char < 'a' for char in word):
        word = random.choice(w)
    return word

def play(wL):
    word = get_word(wL).upper()
    ogWord = word
    wordLength = len(word)
    guessedList = []
    flag = False
    currWord = ["-"] * wordLength
    
    while wordLength != 0:
        print("You guessed these letters: ", end= "")
        for char in guessedList:
            print(char, end = " ")
            while char in word:
                currWord[word.index(char)] = char
                word = word.replace(char," ",1)
                wordLength = wordLength - 1

        if(wordLength == 0): break
        print("\nCurrent Word: ", end = "")
        for c in currWord:
            print(c, end = " ")
        print("\n")

        guess = input("Guess a letter: ").upper()
        guessedList.append(guess)
        if guess in word:
            print("Correct guess!")
            print("-"*10)


    print("\nCongrats! You guessed: " + ogWord + " successfully.")


play(words)
