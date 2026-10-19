# Rock Paper Scissors - play against the computer
import random

OPTIONS = ["rock", "paper", "scissor"]


def get_choices():
    """Ask the player for a valid choice and pick one for the computer."""
    while True:
        player_choice = input("Enter a choice (Rock, Paper, Scissor): ").strip().casefold()
        if player_choice in OPTIONS:
            break
        print("Invalid choice, please try again.")
    computer_choice = random.choice(OPTIONS)
    return {"player": player_choice, "computer": computer_choice}


def check_win(player, computer):
    """Return the result message and 'win', 'lose' or 'tie'."""
    print("You chose " + player + " and the computer chose " + computer)
    if player == computer:
        return "It's a tie!", "tie"
    if player == "rock":
        if computer == "scissor":
            return "Rock destroys scissor! -- YOU WIN --", "win"
        return "Paper covers rock! -- YOU LOSE --", "lose"
    if player == "paper":
        if computer == "rock":
            return "Paper covers rock! -- YOU WIN --", "win"
        return "Scissor cuts paper! -- YOU LOSE --", "lose"
    if computer == "paper":
        return "Scissor cuts paper! -- YOU WIN --", "win"
    return "Rock destroys scissor! -- YOU LOSE --", "lose"


def main():
    wins = losses = ties = 0
    while True:
        choice = get_choices()
        message, outcome = check_win(choice["player"], choice["computer"])
        print(message)
        if outcome == "win":
            wins += 1
        elif outcome == "lose":
            losses += 1
        else:
            ties += 1
        print(f"Score -> Wins: {wins}  Losses: {losses}  Ties: {ties}")
        again = input("Play again? (y/n): ").strip().casefold()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
