import random


def play():
    user = input("Enter 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    print(f"You chose {user}")
    print(f"Computer choose {computer}")
    if user == computer:
        return "TIE!"
    elif is_win(user, computer):
        return "You win!"
    else:
        return "Computer wins!"

def is_win(player, opponent):
    choices = {'r': 1,
               'p': 2,
               's': 3
               }

    if choices[player] > choices[opponent] or (player == 'r' and opponent == 's'):
        return True
    return False

print(play())