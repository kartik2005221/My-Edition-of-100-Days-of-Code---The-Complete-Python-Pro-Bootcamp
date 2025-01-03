import art
from game_data import data
import random

contd = True
score = 0
c1 = random.choice(data)

while contd:
    print(art.logo)
    if score == 0:
        print(f"Current score: {score}")
    else:
        print(f"You're Right! Current Score: {score}")
    c2 = random.choice(data)

    # {
    #         'name': 'Instagram',
    #         'follower_count': 346,
    #         'description': 'Social media platform',
    #         'country': 'United States'
    #     },

    print(f"Compare A: {c1["name"]}, a {c1["description"]}, from {c1["country"]}.")
    print(art.vs)
    print(f"Against B: {c2["name"]}, a {c2["description"]}, from {c2["country"]}.")
    kk = input("Who has more followers? A/B ::: ").lower()
    print('\n' * 100)
    if kk == 'a' and c1["follower_count"] > c2["follower_count"]:
        score += 1
        c1 = c2
    elif kk == 'b' and c1["follower_count"] < c2["follower_count"]:
        score +=1
        c1 = c2
    else:
        print(art.logo)
        print(f"You're Wrong!! Final Score {score}")
        contd = False
