mass = [['','',''],['','',''],['','','']]

def show_game():
    for i in range(3):
        print(mass[i])

def ask(mov):
    x = int(input())
    y = int(input())
    if x>-1 or x<3 or y>-1 or y<3:
        if mass[x][y] == '':
            if mov%2==1:
                mass[x][y]='X'
            else:
                mass[x][y]='O'
        else:
            print('Клетка занята, введи другую')
            ask(mov)
    else:
        print('Выходите за пределы игрового поля')
        ask(mov)
    check_win()

def game_over():
    global count
    count = 8
    return False

def check_win():
    for i in range(3):
        if mass[i][0] == mass[i][1] == mass[i][2] == 'X':
            print(f'Выиграли {mass[i][0]}')
            game_over()
        elif mass[0][i] == mass[1][i] == mass[2][i] == 'X':
            print(f'Выиграли {mass[i][0]}')
            game_over()
        elif mass[0][0] == mass[1][1] == mass[2][2] == 'X':
            print(f'Выиграли {mass[i][0]}')
            game_over()
        elif mass[0][2] == mass[1][1] == mass[2][0] == 'X':
            print(f'Выиграли {mass[i][0]}')
            game_over()
        elif mass[i][0] == mass[i][1] == mass[i][2] == 'O':
            print(f'Выиграли {mass[i][0]}')
            game_over()
        elif mass[0][i] == mass[1][i] == mass[2][i] == 'O':
            print(f'Выиграли {mass[i][0]}')
            game_over()
        elif mass[0][0] == mass[1][1] == mass[2][2] == 'O':
            print(f'Выиграли {mass[i][0]}')
            game_over()
        elif mass[0][2] == mass[1][1] == mass[2][0] == 'O':
            print(f'Выиграли {mass[i][0]}')
            game_over()

count=0
while True:
    show_game()
    count+=1
    if count==9:
        print('Игра окончена')
        break
    if count%2==1:
        print('Куда поставить крестик?')
    else:
        print('Куда поставить нолик?')
    ask(count)


