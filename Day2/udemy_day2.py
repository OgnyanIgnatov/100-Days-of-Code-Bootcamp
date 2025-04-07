import random

choices=["rock", "paper", "sciscors"]
yourChoice=int(input("0: Rock, 1: Paper, 2: Sciscors : "))
computerChoice=random.randint(0,2)
print(f"Computer choice: {choices[computerChoice]}")

if choices[yourChoice]=="rock" :

    if choices[computerChoice]=="rock" :
        print("Draw")
    elif choices[computerChoice] == "paper":
        print("You lose")
    else:
        print("You win")

elif choices[yourChoice] == "paper":

    if choices[computerChoice]=="rock" :
        print("You win")
    elif choices[computerChoice] == "paper":
        print("Draw")
    else:
        print("You lose")

else:
    if choices[computerChoice]=="rock" :
        print("You lose")
    elif choices[computerChoice] == "paper":
        print("You win")
    else:
        print("Draw")





