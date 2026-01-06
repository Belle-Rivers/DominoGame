from random import shuffle
from itertools import combinations_with_replacement
DOM = list(combinations_with_replacement(range(0, 7), 2))
DOM = [list(x) for x in DOM]
shuffle(DOM)
coefficient = len(DOM) // 2
bone_yard = DOM[:coefficient]
computer_pieces = DOM[coefficient:int(coefficient * 1.5)]
player_pieces = DOM[int(coefficient * 1.5):]
snake = max([[x, y] for x, y in computer_pieces + player_pieces if x == y])
computer_pieces.remove(snake) if snake in computer_pieces else player_pieces.remove(snake)
player_turn = "It is your turn! Enter your move"
computer_turn = "Computer is making a move. Press Enter to continue..."
print('=' * 70)
print('Bone Yard:', len(bone_yard))
print('Computer pieces:', len(computer_pieces), '\n')
print(snake, '\n')
print("Your pieces:")
for num, piece in enumerate(player_pieces):
    print(f"{num + 1}: {piece}")
print("\nStatus:", player_turn if len(player_pieces) > len(computer_pieces) else computer_turn)


