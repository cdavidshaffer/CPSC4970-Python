class Nim:
    def __init__(self, piles=[15, 7, 9]):
        self._piles = piles
        self._turn = 1

    def is_valid_move(self, move):
        pile, stones_to_remove = move
        return 0 < pile < 4 \
            and self._piles[pile - 1] >= stones_to_remove \
            and sum(self._piles) - stones_to_remove >= 1

    def is_game_over(self):
        return sum(self._piles) == 1

    def get_next_turn(self):
        return 3 - self._turn

    def execute_move(self, move):
        if not self.is_valid_move(move):
            return
        pile, stones_to_remove = move
        self._piles[pile - 1] -= stones_to_remove
        self._turn = self.get_next_turn()

    def get_piles(self):
        return self._piles

    def get_turn(self):
        return self._turn
