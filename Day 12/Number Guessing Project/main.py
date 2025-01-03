from art import logo2
print(logo2)
import random

random_number = random.randint(1,100)
level = int(input("easy(1),,,hard(2) ::: "))

if level == 1:
    lives = 10
    print("You got 10 lives")
else:
    lives = 5
    print("You got 5 lives")

contd = True

while contd:
    guess = int(input("Guess ::: "))
    if guess > random_number:
        print("Too High!")
        lives -= 1
        print(f"You have {lives} lives left\n")
    elif guess < random_number:
        print("Too Low!")
        lives -= 1
        print(f"You have {lives} lives left\n")
    elif guess == random_number:
        print("Win")
        contd = False
    if lives == 0:
        print("All lives are finished\nYou Lose\n")
        print(f"The actual number you are trying to guess is [[[{random_number}]]]")
        contd = False

