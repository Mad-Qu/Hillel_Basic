# Boolean understanding test

# Test 1
print()
print('Вопрос №1')
print('Введите целое значение "X", при котором выражение:')
print('(11 + 9) == (4 + X) выдаст результат True')
answer1 = int(input('X = '))
my_bool1: bool = (11 + 9) == (4 + answer1)

if my_bool1:
    print()
    print('Верно!')
    print('Результат ( 20 = 20 ) и это ...', my_bool1)
else:
    print()
    print('Не правильно!')
    print('Результат ( 20 не равно', 4 + answer1, ") а это ...", my_bool1)


# Test 2
print()
print('Вопрос №2')
print('Введите целое значение "Y", при котором выражение:')
print('(11 - 8) == (1 + Y) выдаст результат True')
answer2 = int(input('Y = '))
my_bool2: bool = (11 - 8) == (1 + answer2)

if my_bool2:
    print()
    print('Верно!')
    print('Результат ( 3 = 3 ) и это ...', my_bool2)
else:
    print()
    print('Не правильно!')
    print('Результат ( 3 не равно', 1 + answer2, ") а это ...", my_bool2)


# Result
print()
if my_bool1 and my_bool2:
    print('Тест пройден, Вы дали 100% правильных ответов')
elif not my_bool1 and not my_bool2:
    print('Тест провален, Вы дали 0% правильных ответов')
else:
    print('Вам еще стоит потренироваться, Вы дали 50% правильных ответов')