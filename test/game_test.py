#!/usr/bin/env python3

import unittest

from game_package import constants
import game_package.solution as game


class GetRoundsRangeTest(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual('1-3', game.get_rounds_range(3))

    def test_one(self):
        self.assertEqual('1', game.get_rounds_range(1))

    def test_with_the_constant(self):
        self.assertEqual(
            '1-5',
            game.get_rounds_range(constants.MAX_ROUNDS),
        )


class ParseRoundCountTest(unittest.TestCase):
    def test_in_range(self):
        self.assertEqual(8, game.parse_round_count(10, '8'))

    def test_min(self):
        self.assertEqual(1, game.parse_round_count(18, '1'))

    def test_max(self):
        self.assertEqual(18, game.parse_round_count(18, '18'))

    def test_one(self):
        self.assertEqual(1, game.parse_round_count(1, '1'))

    def test_with_the_constant(self):
        self.assertEqual(5, game.parse_round_count(constants.MAX_ROUNDS, '5'))
        self.assertIsNone(game.parse_round_count(constants.MAX_ROUNDS, '6'))

    def test_zero(self):
        self.assertIsNone(game.parse_round_count(4, '0'))

    def test_negative_number(self):
        self.assertIsNone(game.parse_round_count(4, '-2'))

    def test_too_big_number(self):
        self.assertIsNone(game.parse_round_count(4, '9'))

    def test_not_a_number(self):
        self.assertIsNone(game.parse_round_count(8, 'hello'))

    def test_empty_string(self):
        self.assertIsNone(game.parse_round_count(14, ''))


class ValidateUserSymbolTest(unittest.TestCase):
    def test_valid_choice(self):
        self.assertTrue(game.validate_user_symbol(
            ['first', 'second', 'third'], 'first'))
        self.assertTrue(game.validate_user_symbol(
            ['first', 'second', 'third'], 'second'))
        self.assertTrue(game.validate_user_symbol(
            ['first', 'second', 'third'], 'third'))

    def test_with_the_constant(self):
        self.assertTrue(game.validate_user_symbol(
            constants.GAME_SYMBOLS, 'paper'))
        self.assertFalse(game.validate_user_symbol(
            constants.GAME_SYMBOLS, 'fire'))

    def test_wrong_choice(self):
        self.assertFalse(game.validate_user_symbol(
            ['first', 'second', 'third'], 'fourth'))

    def test_empty_string(self):
        self.assertFalse(game.validate_user_symbol(
            ['first', 'second', 'third'], ''))


class CalcWinnerTest(unittest.TestCase):
    def test_neighbouring_options(self):
        score = {'user': 20, 'computer': 15}
        result = game.calc_winner(
            ['first', 'second', 'third'],
            'first', 'second',
            score,
        )
        self.assertEqual('You won', result)
        self.assertDictEqual(
            {'user': 21, 'computer': 15},
            score,
        )

    def test_edge_options(self):
        score = {'user': 0, 'computer': 1}
        result = game.calc_winner(
            ['first', 'second', 'third'],
            'third', 'first',
            score,
        )
        self.assertEqual('You won', result)
        self.assertDictEqual(
            {'user': 1, 'computer': 1},
            score,
        )

    def test_computer_won(self):
        score = {'user': 10, 'computer': 1}
        result = game.calc_winner(
            ['first', 'second', 'third'],
            'third', 'second',
            score,
        )
        self.assertEqual('You lost', result)
        self.assertDictEqual(
            {'user': 10, 'computer': 2},
            score,
        )

    def test_draw(self):
        score = {'user': 2, 'computer': 4}
        result = game.calc_winner(
            ['first', 'second', 'third'],
            'second', 'second',
            score,
        )
        self.assertEqual('Draw', result)
        self.assertDictEqual(
            {'user': 3, 'computer': 5},
            score,
        )

    def test_with_the_constant(self):
        score = {'user': 3, 'computer': 2}
        result = game.calc_winner(
            constants.GAME_SYMBOLS,
            'rock', 'scissors',
            score,
        )
        self.assertEqual('You won', result)
        self.assertDictEqual(
            {'user': 4, 'computer': 2},
            score,
        )
        result = game.calc_winner(
            constants.GAME_SYMBOLS,
            'paper', 'scissors',
            score,
        )
        self.assertEqual('You lost', result)
        self.assertDictEqual(
            {'user': 4, 'computer': 3},
            score,
        )


if __name__ == '__main__':
    unittest.main()
