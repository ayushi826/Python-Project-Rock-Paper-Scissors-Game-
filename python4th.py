# list=["java","c","php","python"]
# print(sorted(list))

# tuple=("java","c","php","python")
# print(sorted(tuple))
# d={"a":11,"b":90,"b":3}
# print(d["a"])

# str="hello"
# print(str[:4])
# fg=()
# print(fg)

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

import random
import time

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors', 'special move']
    return random.choices(choices, weights=[0.33, 0.33, 0.33, 0.01])[0]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 'special move':
        return "You used the Special Move! Instant win!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors - Ultimate Edition!")
    user_score = 0
    computer_score = 0
    rounds = 3
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}...")
        time.sleep(1)
        user_choice = input("Enter rock, paper, scissors, or 'special move' (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in ['rock', 'paper', 'scissors', 'special move']:
            print("Invalid choice, try again.")
            continue
        
        computer_choice = get_computer_choice()
        print("Thinking...")
        time.sleep(1.5)
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if "win" in result:
            user_score += 1
        elif "Computer wins" in result:
            computer_score += 1
    
        print("\nFinal Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
    else:
        print("It's a draw! Play again to break the tie!")

    play_game()
    # VVV.choice(['rock', 'paper', 'scissors'])