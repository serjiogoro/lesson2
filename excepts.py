resp = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "язык":"python"}
def ask_user1():
    try:
        user_say = input('Пользователь: ')
        while True:
            if user_say not in resp:
                print('Программа: хз че сказать :)')
                break
            else:
                print(f'Программа: {resp[user_say]}')
                user_say = input('Пользователь: ')
    except(KeyboardInterrupt):
        print('\n')
        print('Пока!')
ask_user1()