def welcome():
    print("------------------------")
    print("Добро пожаловать в игру ")
    print("    Крестики-нолики     ")
    print("------------------------")
    print("    для хода выберете   ")
    print("       номер поля       ")
    print("     и нажмите Enter    ")
    print("------------------------")

gboard = list(range(1, 10))

def draw_board(gboard):    # отрисовка игрового поля
    print("-" * 13)
    for i in range(3):
        print("|", gboard[0+i*3], "|", gboard[1+i*3], "|", gboard[2+i*3], "|")
        print("-" * 13)

def player_input(player_token):    # ввод значений и проверка ввода пользователем
    valid = False
    while not valid:
        player_answer = input("Выберете поле " + player_token+" ")
        try:
            player_answer = int(player_answer)    # приведение к формату int
        except:
            print("Неверный ввод. Введите число!")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(gboard[player_answer-1]) not in "XO"):
                gboard[player_answer-1] = player_token
                valid = True
            else:
                print("Это поле уже занято!")
        else:
            print("Неверный ввод. Введите число от 1 до 9!")

def check_win(gboard):    # описание выйгрышных вариантов и проверка на выйгрыш
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if gboard[each[0]] == gboard[each[1]] == gboard[each[2]]:
            return gboard[each[0]]
    return False

welcome()

def main(gboard):
    counter = 0    # счетчик ходов
    win = False
    while not win:
        draw_board(gboard)
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            log_ = check_win(gboard)
            if log_:
                print(log_, "выиграл!")
                win = True
                break
        if counter == 9:    # максимальное число ходов для ничейного результата
            print("Ничья!")
            break
    draw_board(gboard)
main(gboard)

input("Нажмите Enter для выхода!")
