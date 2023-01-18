# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import *
import os

print('Перед вами 2021 конфета.')

print('Правила простые: за ход можно брать не более 28 конфет.\nСделавший последний ход, получает все конфеты.\nНачинаем.')

# message = ['твоя очередь', 'да бери уже', 'бери больше', 'не корову проигрываешь',
#           'бери быстрее', 'да харош, так долго думать уже']

# Метод игры человек против человека
# def p_v_p():
#     all_cand = 2021
#     max_take = 28
#     play_1, play_2 = input('Имя первого игрока: '), input('Имя второго игрока: ')
#     counter = 0
#     print('\nОпределим кто ходит первый жеребьёвкой: ')
#     vol = randint(1, 2)
#     if vol == 1:
#         lucky = play_1
#         loser = play_2
#     else:
#         lucky = play_2
#         loser = play_1
#     print(f'{lucky} ходит первым.')

#     while all_cand > 0:
#         if counter == 0:
#             step = int(input(f'{lucky} введите количество конфет (число от 1 до 28): '))
#             if step > all_cand or step > max_take:
#                 step = int(input(
#                     f'\nВведено неверное значение. {lucky}, попробуйте еще раз: '))
#             all_cand = all_cand - step
#         if all_cand > 0:
#             print(f'\nОстаток: {all_cand}')
#             counter = 1
#         else:
#             print('Конфеты закончились.')

#         if counter == 1:
#             step = int(input(f'{loser} введите количество конфет (число от 1 до 28): '))
#             if step > all_cand or step > max_take:
#                 step = int(input(
#                     f'\nВведено неверное значение. {lucky}, попробуйте еще раз: '))
#             all_cand = all_cand - step
#         if all_cand > 0:
#             print(f'\nОстаток: {all_cand}')
#             counter = 0
#         else:
#             print('Конфеты закончились.')

#     if counter == 1:
#         print(f'Победитель {loser}')
#     if counter == 0:
#         print(f'Победитель {lucky}')

# p_v_p()

# Метод игры человек против компьютера
def p_v_pc():
    all_cand = 2021
    max_take = 28
    play_1 = input('Имя игрока: ')
    play_2 = 'Компьютер'
    players = [play_1, play_2]
    print('\nОпределим кто ходит первый жеребьёвкой: ')
    lucky = randint(-1, 0)
    print(f'{players[lucky+1]} ходит первым.')
    while all_cand > 0:
        lucky += 1
        if players[lucky % 2] == 'Компьютер':
            print(
                f'\nХодит {players[lucky%2]} \nОстаток: {all_cand}.: ')
            if all_cand < 29:
                step = all_cand
            else:
                delenie = all_cand//28
                step = all_cand - ((delenie*max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'\nХодит {players[lucky%2]} \nОстаток: {all_cand}:  '))
            while step > max_take or step > all_cand:
                step = int(input(f'\nНеверное значение, попробуйте еще раз: '))
        all_cand = all_cand - step
    print(f'Остаток {all_cand} \nПобедил {players[lucky%2]}')

p_v_pc()