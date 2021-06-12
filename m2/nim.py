def is_game_over(piles):
    return sum(piles) == 1


def next_turn(turn):
    return 3 - turn


def read_move(turn):
    move = input(f"Player {turn}, enter your move (pile,stones): ")
    pile = int(move[0])
    stones_to_remove = int(move[2])
    return pile, stones_to_remove


def execute_move(move, piles):
    pile = move[0]
    stones_to_remove = move[1]
    piles[pile - 1] = piles[pile - 1] - stones_to_remove


def display_game(piles):
    print(f"Piles: {piles}")


def main():
    board = [12, 9, 13]
    turn = 1

    while not is_game_over(board):
        display_game(board)
        move = read_move(turn)
        execute_move(move, board)
        turn = next_turn(turn)

    print(f"\n\nFinal piles: {board}")
    print(f"Player {next_turn(turn)} is the winner!")
    print("Thanks for playing")


if __name__ == '__main__':
    main()
