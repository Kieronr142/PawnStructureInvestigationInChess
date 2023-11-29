import chess.engine
import chess.pgn

# Function to play a game
def play_game(fen):
    # Initialize the chess board to the desired endgame setup
    board = chess.Board(fen)

    # Start the chess engine
    engine = chess.engine.SimpleEngine.popen_uci("./stockfish/stockfish-windows-x86-64-avx2.exe")

    # Set the number of threads (replace '2' with the number of threads you want to use)
    engine.configure({"Threads": 10})

    # Play the game
    while not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=1.00))
        board.push(result.move)

        # Print the board state after each turn
        print(board)
        print("")

    # Close the engine
    engine.quit()

    # Return the result of the game
    return board.result()

# Function to run multiple games and save the results
def run_experiment(fen, num_games):
    # Open the results file
    with open("results.txt", "a") as results_file:
        # Write the FEN string as a header
        results_file.write(fen + "\n")

        # Play the games
        for i in range(num_games):
            result = play_game(fen)
            results_file.write(result + "\n")

            # Print a message after each game
            print(f"Game ({i+1}/{num_games}) complete. {result}.")

        # Write a separator
        results_file.write("\n")


# Run the experiment
fen = "4k3/5r2/2p3p1/8/2P5/3P4/1R6/4K3 w - - 0 1"
run_experiment(fen, 30)
