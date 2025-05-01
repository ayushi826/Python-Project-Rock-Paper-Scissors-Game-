import random

def determine_winner(user_choice, computer_choice):                       #
  if (user_choice == 'rock' and computer_choice == 'scissors'or 
      user_choice == 'paper' and computer_choice == 'rock' or 
      user_choice == 'scissors' and computer_choice == 'paper'):
      return True
  return False

def main():
    user_score = 0
    computer_score = 0
    user = ""
    print("welcome to rock,paper scissors Game.")

    while user != "end":
        
        computer = random.choice(['rock', 'paper', 'scissors'])
        user = input("choose rock, paper, or scissors (or 'end' to exit):")
        user = user.lower().strip()
        
        if user == "end":
            print("Thanks for Playing!")
            print(f" Your Score: {user_score} - Computer Score: {computer_score}\n")
            if user_score > computer_score:
                print("YOU are a Champion!")
            else :
                 print("Computer is a Champion! Try again")
            break
        elif user not in ['rock', 'paper', 'scissors']:
            print("Invalid input, try again.")
            continue
        
        print(f"I chose {computer}.")

        if user == computer:
            print("Play aagain! It's a tie!")
        elif determine_winner(user, computer):     
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1

if __name__ == "__main__":
    main()

        











