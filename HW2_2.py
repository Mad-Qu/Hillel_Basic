variable = input('Введите число с дробным значением: ')
x = 0;


# Функция проверки на возможность конвертации введенного числа в float
def is_float(str_var):
    try:
        float(str_var)
        return True
    except ValueError:
        return False


# Цикл для проверки ввода числа с дробным значением(float),
# Заканчивается только в случае ввода числа с дробным значением(float)
# в текстовом виде
while x == 0:
    if is_float(variable) and ("." in variable):
        x = 1
    else:
        variable = input("ВВЕСТИ НУЖНО число с дробным значением!: ")

variable = int(float(variable))
print('Целочисельное представление переменной =', variable, type(variable))
