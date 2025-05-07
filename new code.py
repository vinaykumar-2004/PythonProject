import random

def rock_paper_scissors():
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

def number_guess():
    number = random.randint(1, 100)
    tries = 0
    print("Guess a number between 1 and 100")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        tries += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You took {tries} tries.")
            break

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

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for turn in range(9):
        print_board(board)
        print(f"Player {player}'s turn")
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print("Invalid position. Try again.")
                continue
        except ValueError:
            print("Please enter valid numbers.")
            continue

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

def main():
    while True:
        print("\n=== Mini Games Pack ===")
        print("1. Rock Paper Scissors")
        print("2. Number Guessing")
        print("3. Tic-Tac-Toe")
        print("4. Exit")

        choice = input("Choose a game: ")

        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            number_guess()
        elif choice == "3":
            tic_tac_toe()
        elif choice == "4":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
