import random

from . import constants, templates


def get_rounds_range(max_rounds):
    """Get rounds range string.

    Display possible options depending on the limit of the maximum
    number of rounds.
    It's needed just to make the case with the limit=1 prettier, i.e.
    instead of displaying "1-1", show just "1".
    """
    return '1' if max_rounds == 1 else '1-' + str(max_rounds)


def parse_round_count(max_rounds, rounds_input):
    """Parse round count.

    Try to convert a string to a number of rounds. If the string
    is invalid, return None for subsequent handling outside of
    this function.
    """
    if not rounds_input.isdigit():
        return None

    round_count = int(rounds_input)
    if 1 <= round_count <= max_rounds:
        return round_count

    return None


def print_greeting_and_get_round_count():
    """Ask user to specify a number of rounds.

    Properly handle a case when a string is invalid and ask to
    specify it again.
    """
    rounds_range = get_rounds_range(constants.MAX_ROUNDS)
    print(templates.GREETING.format(
        symbols=constants.GAME_SYMBOLS, rounds_range=rounds_range), end='')
    while True:
        rounds_input = input()
        round_count = parse_round_count(constants.MAX_ROUNDS, rounds_input)
        if round_count is not None:
            return round_count

        print(templates.INVALID_ROUND_COUNT.format(
            rounds_input=rounds_input,
            rounds_range=rounds_range,
        ), end='')


def validate_user_symbol(options, user_symbol):
    """Validate user symbol.

    Entered game symbol must be the one from the available options.
    """
    return user_symbol in options


def print_round_intro_and_get_user_symbol(round_number, round_count):
    """Parse specified user symbol.

    Ask a user to specify a game symbol and repeat it if the entered
    string is not a valid choice.
    """
    print(templates.SYMBOL_CHOICE.format(
        symbols=constants.GAME_SYMBOLS,
        round_number=round_number,
        round_count=round_count,
    ), end='')
    while True:
        user_symbol = input()
        if validate_user_symbol(constants.GAME_SYMBOLS, user_symbol):
            return user_symbol

        print(templates.INVALID_SYMBOL.format(
            user_symbol=user_symbol,
            symbols=', '.join(constants.GAME_SYMBOLS),
        ), end='')


def calc_winner(precedence, user, computer, score):
    """Determine the winner of the round.

    Depending on the game symbols of the user and the computer,
    determine who won the round, update the score and return a
    message reflecting the game result.
    """
    user_idx = precedence.index(user)
    computer_idx = precedence.index(computer)

    if user_idx == computer_idx:
        score['user'] += 1
        score['computer'] += 1
        return 'Draw'

    # If computer's choice comes right after the user's one in the
    # order of game symbols.
    if (user_idx + 1) % 3 == computer_idx:
        score['user'] += 1
        return 'You won'

    score['computer'] += 1
    return 'You lost'


def main():
    """The entrypoint of the game."""
    round_count = print_greeting_and_get_round_count()
    score = {'user': 0, 'computer': 0}

    for i in range(round_count):
        user_symbol = print_round_intro_and_get_user_symbol(i + 1, round_count)
        computer_symbol = constants.GAME_SYMBOLS[random.randint(0, 2)]
        result = calc_winner(
            constants.GAME_SYMBOLS, user_symbol, computer_symbol, score)
        print(templates.ROUND_FINISHED.format(
            computer_symbol=computer_symbol,
            result=result,
            **score,
        ), end='')
        # Ask user to press Enter explicitly to draw his attention
        # to the result before moving on to the next round.
        input()

    print(templates.GAME_OVER.format(**score), end='')
    # Ask user to press Enter explicitly to draw his attention
    # to the final score before exiting the game.
    input()
