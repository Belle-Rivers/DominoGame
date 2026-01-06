from random import shuffle
from itertools import combinations_with_replacement
# define turn function
def turn_func(func_input, func_pieces):
    if int(func_input) == 0 and len(bone_yard) == 0:
        return None
    elif int(func_input) == 0 and len(bone_yard) > 0:
        func_pieces.append(bone_yard[-1])
        bone_yard.remove(bone_yard[-1])
        return None
    if int(func_input) > 0:
        piece_to_end = func_pieces[int(func_input) - 1]
        if piece_to_end[1] == snake[-1][-1]:
            piece_to_end.reverse()
        snake.append(piece_to_end)
        func_pieces.remove(func_pieces[int(func_input) - 1])
    else:
        piece_to_start = func_pieces[-int(func_input) - 1]
        if piece_to_start[0] == snake[0][0]:
            piece_to_start.reverse()
        snake.insert(0, piece_to_start)
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
player_won = 'The game is over. You won!'
computer_won = 'The game is over. The computer won!'
turn_num = 0 if len(player_pieces) > len(computer_pieces) else 1
while True:
    print('=' * 70)
    print('Stock size:', len(bone_yard))
    print('Computer pieces:', len(computer_pieces), '\n')
    print(*snake, '\n', sep='') if len(snake) <= 6 else print(*snake[:3], '...', *snake[-3:], '\n', sep='')
    print("Your pieces:")
    for num, piece in enumerate(player_pieces):
        print(f"{num + 1}: {piece}")
    if len(player_pieces) == 0:
        print("\nStatus:", player_won)
        break
    if len(computer_pieces) == 0:
        print("\nStatus:", computer_won)
        break
    if win_snake(snake) and turn_num == 0:
        print("\nStatus:", player_won)
        break
    if win_snake(snake) and turn_num == 1:
        print("\nStatus:", computer_won)
        break
    connection_keys = [snake[0][0], snake[-1][-1]]
    if len(bone_yard) == 0 and \
            any([verb[1] for verb in player_pieces + computer_pieces if verb[0] in connection_keys]):
        print("\nStatus: The game is over. It's a draw!")
        break
    if turn_num % 2 == 0:
        turn_num += 1
        print("\nStatus:", player_turn)
        user_input = input()
        if user_input.lstrip("-").isdigit() and int(user_input) in range(-len(player_pieces), len(player_pieces) + 1):
            if int(user_input) == 0:
                turn_func(user_input, player_pieces)
                continue
            current_piece = player_pieces[int(user_input) - 1] if int(user_input) > 0 \
                else player_pieces[-int(user_input) - 1]
            if connection_keys[-1] in current_piece and int(user_input) > 0 or \
                    connection_keys[0] in current_piece and int(user_input) < 0:
                turn_func(user_input, player_pieces)
            else:
                print("Illegal move. Please try again.")
                turn_num -= 1
                continue
        else:
            print("Invalid input. Please try again.")
            turn_num -= 1
            continue
    else:
        turn_num += 1
        print("\nStatus:", computer_turn)
        input()
        for piece in computer_pieces:
            if piece[0] == connection_keys[-1]:
                turn_func(str(computer_pieces.index(piece) + 1), computer_pieces)
                break
            elif piece[1] == connection_keys[0]:
                turn_func(str(-computer_pieces.index(piece) - 1), computer_pieces)
                break
        else:
            turn_func('0', computer_pieces)