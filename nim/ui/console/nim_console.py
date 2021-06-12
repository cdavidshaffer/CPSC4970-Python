from ...engine.nim import Nim


def read_move(game):
    move = input(f"Player {game.get_turn()}, enter your move (pile,stones): ")
    pile = int(move[0])
    stones_to_remove = int(move[2:])
    return pile, stones_to_remove


def read_valid_move(game):
    move = read_move(game)
    while not game.is_valid_move(move):
        print("Invalid move, try again")
        move = read_move(game)
    return move


def display_game(game):
    print(f"Piles: {game.get_piles()}")


def main():
    game = Nim()

    while not game.is_game_over():
        display_game(game)
        move = read_valid_move(game)
        game.execute_move(move)

    print(f"\n\nFinal piles: {game.get_piles()}")
    print(f"Player {game.get_next_turn()} is the winner!")
    print("Thanks for playing")

