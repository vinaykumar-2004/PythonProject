# mini_games_pack/main.py

def main():
    while True:
        print("\n=== Mini Games Pack ===")
        print("1. Rock Paper Scissors")
        print("2. Number Guessing")
        print("3. Tic-Tac-Toe")
        print("4. Exit")

        choice = input("Choose a game: ")

        if choice == "1":
            import rock_paper_scissors
            rock_paper_scissors.play()
        elif choice == "2":
            import number_guess
            number_guess.play()
        elif choice == "3":
            import tic_tac_toe
            tic_tac_toe.play()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


# mini_games_pack/rock_paper_scissors.py
import random

def play():
    choices = ["rock", "paper", "scissors"]
    user = input("Enter rock, paper, or scissors: ").lower()
    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("You lose!")


# mini_games_pack/number_guess.py
import random

def play():
    number = random.randint(1, 100)
    tries = 0
    print("Guess a number between 1 and 100")

    while True:
        guess = int(input("Your guess: "))
        tries += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You took {tries} tries.")
            break


# mini_games_pack/tic_tac_toe.py
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for turn in range(9):
        print_board(board)
        print(f"Player {player}'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))

        if board[row][col] != " ":
            print("Spot already taken, try again.")
            continue

        board[row][col] = player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a tie!")
