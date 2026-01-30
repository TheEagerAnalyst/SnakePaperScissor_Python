import random

rand_no = random.randint(1,3)

if rand_no == 1:
    computer = "r"
elif rand_no == 2:
    computer = "p"
else:
    computer = "s"
    
print("Computer's turn: Rock(r), Paper(p), Scissors(s):" )
print(f"Computer chose: {computer}")
user = input("Your turn: Rock(r), Paper(p), Scissors(s): "). lower()

if computer == user:
    print("It's a tie!")
elif computer == "r" and user == "s":
    print("Computer wins!")
elif computer == "r" and user == "p":
    print("You win!")
elif computer== "s" and user == "p":
    print("Computer wins!")
elif computer == "s" and user == "r":
    print("You win!")   
elif computer == "p" and user == "r":
    print("Computer wins!")
elif computer == "p" and user == "s":
    print("You win!")   
else:
    print("Invalid input! Please choose r, p, or s.")