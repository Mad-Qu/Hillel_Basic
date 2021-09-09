import string
import random
import zipfile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем.
    Возвращает результат операции (bool)
    """
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        # print(e)  # закоментил ненужный вывод неудачных попыток
        return False


def pw_gen(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def hack_archive(file_name):
    """
    Функция перебирает пароли
    """
    file_to_open = zipfile.ZipFile('hack_me.zip')  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток

    password = ''
    while True:
        """
        Здесь необходимо реализовать: 
            1. Случайную генерацию пароля, который будет соответствовать условиям:
                * длина - 4 символа (`PASSWORD_LENGTH`)
                * допустимые символы пароля - только цифры
                * type(password) == str
            2. Открытие архива со сгенерированым паролем - `extract_archive(file_to_open, password)`
            При удачном открытии (True) - прервать цикл
            При неудачи (False) - добавить пароль в список `wrong_passwords` и больше не проверять данный пароль
            3. Счетчий неудачных попыток
        """
        password = pw_gen()

        if extract_archive(file_to_open, password):
            break
        else:
            wrong_passwords.append(password)
            tries += 1

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')


filename = 'hack_me.zip'
hack_archive(filename)
