import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "draw"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_num = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game!")

    while True:
        print(f"\n--- Round {round_num} ---")
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "draw":
            print("It's a draw!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Scores → You: {user_score} | Computer: {computer_score}")

        # Ask if user wants to continue
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\n🎉 Final Scores:")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        round_num += 1

# Run the game
play_game()
