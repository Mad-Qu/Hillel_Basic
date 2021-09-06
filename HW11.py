import random


class Unit:
    def __init__(self, name, clan, base_skill=None,
                 health=100, strength=1, agility=1, intelligence=1):
        self.name = name
        self.clan = clan
        self.base_skill = base_skill
        self.health = health
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence

    def __str__(self):
        return f'Профессия: {self.__class__.__name__} \n' \
               f'Имя: {self.name} \n' \
               f'Клан: {self.clan} \n' \
               f'Здоровье: ({self.health}/100) \n' \
               f'Оружие: '

    def do_healing(self):
        if self.health < 91:
            self.health += 10
        else:
            self.health = 100

    def do_skill_up(self):  # вариант когда нам известны ВСЕ существующие хар-ки персонажей
        if self.base_skill == 'intelligence' and self.intelligence < 10:
            self.intelligence += 1
        if self.base_skill == 'agility' and self.agility < 10:
            self.agility += 1
        if self.base_skill == 'strength' and self.strength < 10:
            self.strength += 1


class Mage(Unit):
    def __init__(self, name, clan, base_skill='intelligence', __weapon=None):
        super(Mage, self).__init__(name, clan)
        self.base_skill = base_skill
        self.__weapon = random.choice(['Air', 'Fire', 'Water'])
        self.health = random.randint(59, 89)  # удобней проверять do_healing

    def __str__(self):
        result = super(Mage, self).__str__()
        return f'{result} {self.__weapon} \n' \
               f'Баз.навык [{self.base_skill}] = {self.intelligence}'


class Archer(Unit):
    def __init__(self, name, clan, base_skill='agility', __weapon=None):
        super(Archer, self).__init__(name, clan)
        self.base_skill = base_skill
        self.__weapon = random.choice(['Bow', 'Arbalest', 'Sling'])
        self.health = random.randint(59, 89)  # удобней проверять do_healing

    def __str__(self):
        result = super(Archer, self).__str__()
        return f'{result} {self.__weapon} \n' \
               f'Баз.навык [{self.base_skill}] = {self.agility}'


class Knight(Unit):
    def __init__(self, name, clan, base_skill='strength', __weapon=None):
        super(Knight, self).__init__(name, clan)
        self.base_skill = base_skill
        self.__weapon = random.choice(['Sword', 'Axe', 'Pike'])
        self.health = random.randint(59, 89)  # удобней проверять do_healing

    def __str__(self):
        result = super(Knight, self).__str__()
        return f'{result} {self.__weapon} \n' \
               f'Баз.навык [{self.base_skill}] = {self.strength}'


mage_1 = Mage('Harry Potter', 'Hogwarts School')  # меняем имя профессии(класса)

print(mage_1, '\n')

mage_1.do_skill_up()  # 2 раза повышаем базовый навык
mage_1.do_skill_up()
mage_1.do_healing()  # 2 раза пополняем здоровье +10
mage_1.do_healing()
print(mage_1)
