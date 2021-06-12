import unittest
from nim.engine.nim import Nim


class NimTest(unittest.TestCase):

    INITIAL_BOARD = [2, 6, 5]

    def setUp(self):
        super().setUp()
        self.game = Nim(self.INITIAL_BOARD.copy())

    def tearDown(self):
        super().tearDown()
        pass     # free any resources that were allocated

    @staticmethod
    def execute_move(game, pile, stones):
        game.execute_move((pile, stones))

    def test_player_one_goes_first(self):
        self.assertEqual(1, self.game.get_turn())

    def test_player_two_follows_valid_move_by_player_one(self):
        self.execute_move(self.game, 1, 2)
        self.assertEqual(2, self.game.get_turn())

    def test_is_game_over(self):
        g1 = Nim([1, 0, 0])
        g2 = Nim([1, 1, 0])

        self.assertTrue(g1.is_game_over())
        self.assertFalse(g2.is_game_over())

    # Not a test!
    def execute_move_ignores_invalid_moves(self, move):
        self.execute_move(self.game, move[0], move[1])
        self.assertEqual(1, self.game.get_turn())
        self.assertSequenceEqual(self.INITIAL_BOARD, self.game.get_piles())

    def test_execute_move_ignores_invalid_moves(self):
        for move in [(0, 10), (0, 0), (4, 1), (4, 0), (1, 3)]:
            self.execute_move_ignores_invalid_moves(move)

    def test_execute_move_takes_stones(self):
        self.execute_move(self.game, 1, 2)
        self.assertEqual([0, 6, 5], self.game.get_piles())
