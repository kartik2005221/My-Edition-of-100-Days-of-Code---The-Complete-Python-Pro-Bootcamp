from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def blackjack():
    print('\n' * 100)
    print(logo)
    c1=random.choice(cards)
    c2=random.choice(cards)
    c3=random.choice(cards)
    user_hand = [c1, c2]
    computer_hand = [c3]

    # total_user = sum(user_hand)
    # total_computer = sum(computer_hand)
    print(f"Your Cards : {user_hand}, current score: {sum(user_hand)}")
    print(f"Computer's first card: {c3}")
    game = True

    while game:
        another_card = input("Type y to get another crd, type n to pass : ")
        if another_card == 'n':
            print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}")
            game = False
            if sum(user_hand) >21:
                print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                print("You are over 21, you loose")

            else:
                while sum(computer_hand) < 18:
                    c4 = random.choice(cards)
                    computer_hand.append(c4)
                print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                if sum(computer_hand) > 21:
                    print("Computer is over 21, You win")
                elif sum(user_hand) == 21:
                    print("User Wins as your score is blackjack")
                elif sum(computer_hand) == 21:
                    print("Computer wins as its score is blackjack")
                elif sum(computer_hand) > sum(user_hand):
                    print(f"Computer Wins as {sum(computer_hand)} > {sum(user_hand)}")
                elif sum(user_hand) > sum(computer_hand):
                    print(f"You Wins.. as as {sum(user_hand)} > {sum(computer_hand)}")
                elif sum(user_hand) == sum(computer_hand):
                    print("Draw")
                # else:
                #     print("Error")
        elif another_card == 'y':
            c5 = random.choice(cards)
            user_hand.append(c5)

            print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}")
            print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
            if sum(user_hand) >21:
                print(f"Computer's final hand: {computer_hand}, final score: {sum(computer_hand)}")
                print("You are over 21, you loose")
                game = False
            elif sum(computer_hand) > 21:
                    print("Computer is over 21, You win")
                    game = False
            elif sum(user_hand) == 21:
                print("User Wins as your score is blackjack")
                game = False
            elif sum(user_hand) == sum(computer_hand):
                print("Draw")
                # else:
                #     print("Error2")
                #     game = False

contd=True
while contd:
    k=input("Do You want to play a game of Blackjack? y/n : ")
    if k=='n':
        contd=False
    else:
        blackjack()
