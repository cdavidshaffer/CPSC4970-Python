import nim
import unittest


class NimTest(unittest.TestCase):
    def test_is_game_over(self):
        self.assertFalse(nim.is_game_over([1, 1, 0]))
        self.assertFalse(nim.is_game_over([0, 1, 1]))
        self.assertFalse(nim.is_game_over([1, 0, 1]))
        self.assertTrue(nim.is_game_over([1, 0, 0]))
        self.assertTrue(nim.is_game_over([0, 1, 0]))
        self.assertTrue(nim.is_game_over([0, 0, 1]))

    def test_next_turn(self):
        self.assertEqual(2, nim.next_turn(1))
        self.assertEqual(1, nim.next_turn(2))
