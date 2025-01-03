# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
print(logo)

data = {}

contd = True
while contd:
    name = input("name : ")
    bid = int(input("bid : "))

    data[name] = bid
    if int(input("press 0 to exit and 1 to continue : ")) ==0:
        contd = False
    print("\n"*100)

max=0
max_index=0
for key in data:
    if max<data[key]:
        max=data[key]
        max_index = key

print(f"winner is {max_index} with a bid of {max}")
