def ask_user():
    user_say = input('Как дела?: ')
    while True:
        if user_say == 'Хорошо':
            break
        else:
            print('Вот и молоджец! )')
            user_say = input('Как дела?: ')
ask_user()
#-------------------------------------------
print('#-------------------------------------------')
#-------------------------------------------
resp = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "язык":"python"}
def ask_user1():
    user_say = input('Пользователь: ')
    while True:
        if user_say not in resp:
            print('Программа: хз че сказать :)')
            break
        else:
            print(f'Программа: {resp[user_say]}')
            user_say = input('Пользователь: ')
ask_user1()