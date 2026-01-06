from random import shuffle, choice
from itertools import combinations_with_replacement
def turn_func(func_input, func_pieces):
    if int(func_input) == 0 and len(bone_yard) == 0:
        return None
    elif int(func_input) == 0 and len(bone_yard) > 0:
        func_pieces.append(bone_yard[-1])
        bone_yard.remove(bone_yard[-1])
        return None
    if len(func_input) == 1:
        snake.append(func_pieces[int(func_input) - 1])
        func_pieces.remove(func_pieces[int(func_input) - 1])
    else:
        snake.insert(0, func_pieces[-int(func_input) - 1])
        func_pieces.remove(func_pieces[-int(func_input) - 1])
def win_snake(func_snake):
    if func_snake[0][0] == func_snake[-1][-1] and sum(x.count(func_snake[0][0]) for x in func_snake) == 8:
        return True
DOM = list(combinations_with_replacement(range(0, 7), 2))
DOM = [list(x) for x in DOM]
shuffle(DOM)
coefficient = len(DOM) // 2
bone_yard = DOM[:coefficient]
computer_pieces = DOM[coefficient:int(coefficient * 1.5)]
player_pieces = DOM[int(coefficient * 1.5):]
snake = [max([[x, y] for x, y in computer_pieces + player_pieces if x == y])]
computer_pieces.remove(snake[0]) if snake[0] in computer_pieces else player_pieces.remove(snake[0])
player_turn = "It is your turn! Enter your move"
computer_turn = "Computer is making a move. Press Enter to continue..."
turn_num = 0 if len(player_pieces) > len(computer_pieces) else 1
while True:
    print('=' * 70)
    print('Bone Yard:', len(bone_yard))
    print('Computer pieces:', len(computer_pieces), '\n')
    print(*snake, '\n', sep='') if len(snake) <= 6 else print(*snake[:3], '...', *snake[-3:], '\n', sep='')
    print("Your pieces:")
    for num, piece in enumerate(player_pieces):
        print(f"{num + 1}: {piece}")
    if len(player_pieces) == 0:
        print("\nStatus: The game is over. You won!")
        break
    if len(computer_pieces) == 0:
        print("\nStatus: The game is over. The computer won!")
        break
    if win_snake(snake) and turn_num == 0:
        print("\nStatus: The game is over. You won!")
        break
    if win_snake(snake) and turn_num == 1:
        print("\nStatus: The game is over. The computer won!")
        break
    if turn_num % 2 == 0:
        turn_num += 1
        print("\nStatus:", player_turn)
        user_input = input()
        if user_input.isdigit() and int(user_input) in range(-len(player_pieces), len(player_pieces) + 1):
            turn_func(user_input, player_pieces)
        else:
            print("Invalid input. Please try again.")
            turn_num -= 1
            continue
    else:
        turn_num += 1
        print("\nStatus:", computer_turn)
        input()
        computer_choice = str(choice(range(-len(computer_pieces), len(computer_pieces) + 1)))
        turn_func(computer_choice, computer_pieces)