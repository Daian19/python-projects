while True:
    import random
    import sys
    moves = ["", "rock", "paper", "scissors" ]
    def play_game():
        def player_move():
            while True:
                print("---------------------------------------------")
                print("---              1.ROCK                   ---")
                print("---              2.PAPER                  ---")
                print("---              3.SCISSORS               ---")
                print("---              q.QUIT                   ---")
                print("---------------------------------------------")
                play_again = input('Enter a number : ').lower()
                if play_again not in ["1", "2", "3", "q"]:
                    print("Please enter a valid data!")
                    continue
                elif play_again == "q":
                    sys.exit("Thank you for play our game | bye")
                else:
                    return play_again
        def computer_move():
            return random.choice(["rock", "paper", "scissors"])

        computer = computer_move()
        player = player_move()

        if (player == "1" and computer == "rock") or (player == "2" and computer == "paper") or (player == "3" and computer == "scissors"):
            print('Its a tie!')
            print(f"Your move is {moves[int(player)]} | computer move is {computer}")

        elif (player == "1" and computer == "paper") or (player == "3" and computer == "rock") or (player == "2" and computer == "scissors"):
            print("You are a loser!")
            print(f"Your move is {moves[int(player)]} | computer move is {computer}")

        else:
            print("You are a winner!")
            print(f"Your move is {moves[int(player)]} | computer move is {computer}")
        play_game()
    play_game()


