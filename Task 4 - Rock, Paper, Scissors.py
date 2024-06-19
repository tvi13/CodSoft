from streamlit import *
from random import *

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
    title("Rock-Paper-Scissors Game")
    if 'user_score' not in session_state:
        session_state.user_score = 0
    if 'computer_score' not in session_state:
        session_state.computer_score = 0

    write("Choose Rock, Paper, or Scissors:")
    user_choice = radio("Your choice", ("Rock", "Paper", "Scissors"))
    
    if button("Play"):
        computer_choice = choice(["Rock", "Paper", "Scissors"])
        result = determine_winner(user_choice, computer_choice)
        if result == "You win!":
            session_state.user_score += 1
        elif result == "You lose!":
            session_state.computer_score += 1
        write(f"Your choice: {user_choice}")
        write(f"Computer's choice: {computer_choice}")
        write(result)
        write(f"Your score: {session_state.user_score}")
        write(f"Computer's score: {session_state.computer_score}")

    if button("Reset Scores"):
        session_state.user_score = 0
        session_state.computer_score = 0

if __name__ == "__main__":
    main()