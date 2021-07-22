variable = input('Введите целочисельное значение: ')
x = 0;


# Функция проверки на возможность конвертации введенного числа в int
def is_integer(str_var):
    try:
        int(str_var)
        return True
    except ValueError:
        return False


# Цикл для проверки ввода целого числа(int),
# Заканчивается только в случае ввода целогочисла(int)
# включая отрицательные
while x == 0:
    if is_integer(variable):
        x = 1
    else:
        variable = input("ВВЕСТИ НУЖНО целое число!: ")

variable = str(variable)
print('Текстовое представление переменной =', variable, type(variable))

variable = float(variable)
print('Дробное представление переменной =', variable, type(variable))
