# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
from termcolor import colored, cprint
import emojis

welcome_text = colored('<<< Игра Крестики-нолики PvP >>>', "magenta", attrs=["bold"])
print(welcome_text)
board = list(range(1,10))

def dr_board(board):
    row = colored('-', "green", attrs=["bold"])
    col = colored('|', "green")
    print(row * 13)
    for i in range(3):
        print(col, board[0+i*3], col, board[1+i*3], col, board[2+i*3], col)
        print(row * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(f'Введите номер ячейки, куда поставить {player_token}? (число от 1 до 9): ')
        try:
            player_answer = int(player_answer)
        except:
            cprint('Некорректный ввод. Повторите.', "red")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in 'XO'):
                board[player_answer-1] = player_token
                valid = True
            else:
                cprint('Эта клетка занята!', "red")
        else:
            cprint('Некорректный ввод. Введите число от 1 до 9.', "red")

def check_win(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        dr_board(board)
        if counter % 2 == 0:
            x = colored('X', "red")
            take_input(x)
        else:
            o = colored('O', "cyan")
            take_input(o)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                congr = colored('Поздравляем!',"white", "on_magenta")
                print(f'{congr} {emojis.encode(":wave:")} "{tmp}" победил!{emojis.encode(":medal_sports:")}')
                win = True
                break
        if counter == 9:
            draw = colored('Ничья!', "white", "on_magenta")
            print(draw + emojis.encode(':handshake:'))
            break
    dr_board(board)

main(board)
input('---Нажмите Enter---')