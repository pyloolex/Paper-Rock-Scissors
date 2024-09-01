GREETING = (
    """Welcome to a game "{symbols[0]}-{symbols[1]}-{symbols[2]}"!

It's a game for two players. Now you are playing versus computer.
You pick one game symbol and a computer picks one game symbol.

Available options:
* {symbols[0]}
* {symbols[1]}
* {symbols[2]}

The winner is determined by the following schema:
* {symbols[0]} beats {symbols[1]}
* {symbols[1]} beats {symbols[2]}
* {symbols[2]} beats {symbols[0]}

Please, specify how many rounds you would like to play and press "Enter".
(Available options: {rounds_range})
Number of rounds: """
)
INVALID_ROUND_COUNT = (
    """Invalid choice: "{rounds_input}". Available options: {rounds_range}
Number of rounds: """
)
SYMBOL_CHOICE = (
    """-----
Round {round_number}/{round_count}:
Please, pick one of the game symbols, type your choice and press "Enter":
- {symbols[0]}
- {symbols[1]}
- {symbols[2]}
Your choice: """
)
INVALID_SYMBOL = (
    """Invalid choice "{user_symbol}". Available options: {symbols}
Your choice: """
)
ROUND_FINISHED = (
    """Computer's choice: {computer_symbol}
{result}! Current score: You {user}:{computer} Computer
Press "Enter" to continue."""
)
GAME_OVER = (
    """*****
Game over. The final score: You {user}:{computer} Computer.
Press "Enter" to exit."""
)
