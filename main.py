import random
from game_data import data
import os


def game_hl(A, B):
    # Variables to modify respect the answer of the user
    global score
    global no_mistakes

    # User enters his answer
    answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()

    # The terminal cleans the screen
    os.system('cls')
    if answer == 'A':
        if A > B:
            print("Correct")
            score += 1
            print(f"Current score: {score}")
        else:
            print("Incorrect")
            no_mistakes = False

    elif answer == 'B':
        if B > A:
            print("Correct")
            score += 1
            print(f"Current score: {score}")
        else:
            print("Incorrect")
            no_mistakes = False
    else:
        print("You don't choose a valid option.")
        no_mistakes = False


print("HIGHER LOWER GAME")
no_mistakes = True
# Initial score
score = 0
# The game starts
while no_mistakes:
    # Choice the data
    compareA = random.choice(data)
    compareB = random.choice(data)

    # Take the score
    followerA = compareA['follower_count']
    followerB = compareB['follower_count']

    # Check the answer have different data
    if compareB == compareA:
        compareA = random.choice(data)

    # print(compareA)
    # Show the information
    print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}.")
    # print(compareB)
    print(f"Against B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}.")

    game_hl(followerA, followerB)

print(f"Your final score {score}")
