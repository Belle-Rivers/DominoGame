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
print("Bone Yard:", bone_yard)
print("Computer pieces:", computer_pieces)
print("Player pieces:", player_pieces)
print("Domino snake:", [snake])
print("Status:", "player" if len(player_pieces) > len(computer_pieces) else "computer")