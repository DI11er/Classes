
class Base_Weapon:

    def __init__(self, type_weapon, range_weapon, damage):
        self.__type, self.__range, self.__damage = type_weapon, range_weapon, damage

    @property
    def Damage(self):
        return self.__damage

    @Damage.setter
    def Damage(self, value):
        self.__damage += Base_Weapon.__typeTest(value)

    @property
    def Range(self):
        return self.__range

    @Range.setter
    def Range(self, value):
        self.__range += Base_Weapon.__typeTest(value)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Должно быть int')


class Base_class:
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__gender', '__name', '__weapon', '__shield', '__protection']

    def __init__(self, gender, name, weapon, shield=None, protection=0):
        self.__lvl, self.__health, self.__gender, self.__name, self.__weapon, self.__shield, self.__protection = Base_class.__LVL, Base_class.__HEALTH, gender, name, weapon, shield, protection

    @property
    def Lvl(self):
        return self.__lvl

    @Lvl.setter
    def Lvl(self, value):
        self.__lvl += Base_class.__typeTest(value)

    @property
    def Health(self):
        return self.__health

    @property
    def Gender(self):
        return self.__gender

    @property
    def Name(self):
        return self.__name

    @property
    def Shield(self):
        return self.__shield

    @property
    def Protection(self):
        return self.__protection

    @property
    def Type_weapon(self):
        return self.__weapon._Base_Weapon__type

    @property
    def Range(self):
        return self.__weapon._Base_Weapon__range

    @property
    def Damage(self):
        return self.__weapon._Base_Weapon__damage

    @classmethod
    def event(cls, lvl=1, health=100):
        cls.__LVL, cls.__HEALTH = Base_class.__typeTest(lvl), Base_class.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Должно быть int')

    # Это вариант как можно использовать перегрузку
    """ def __add__(self, other):
        if not isinstance(other, Base_class):
            raise ArithmeticError('Правый оперранд должен быть Clock')
        return Base_class(self.Gender,self.Name,self.__weapon, self.shield, self.__protection + other.Protection) """

    def __str__(self):
        return f'Уровень:{self.Lvl}\nКласс:{self.__class__.__name__}\nИмя:{self.Name}\nПол:{self.Gender}\nЗдоровье:{self.Health}\nОружие:{self.Type_weapon}\nРадиус атаки:{self.Range}\nУрон:{self.Damage}\nЩит:{self.Shield}\nЗащита:{self.Protection}\n'


class Archer(Base_class):
    __HEALTH = 150

    def __init__(self, gender, name, weapon, shield=None, protection=0):
        super().__init__(gender, name, weapon, shield=shield, protection=protection)
        self.__health = Archer.__HEALTH

    @property
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value):
        self.__health += Archer.__typeTest(value)

    @classmethod
    def event(cls, health=150, power=25):
        cls.__HEALTH, cls.__POWER = Archer.__typeTest(health), Archer.__typeTest(power)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Должно быть int')


class Warrior(Base_class):
    __HEALTH = 250

    def __init__(self, gender, name, weapon, shield=None, protection=0):
        super().__init__(gender, name, weapon, shield=shield, protection=protection)
        self.__health = Warrior.__HEALTH

    @property
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value):
        self.__health += Warrior.__typeTest(value)

    @classmethod
    def event(cls, health=250, power=20):
        cls.__HEALTH, cls.__POWER = Warrior.__typeTest(health), Warrior.__typeTest(power)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Должно быть int')


class Tank(Base_class):
    __HEALTH = 350

    def __init__(self, gender, name, weapon, shield=None, protection=0):
        super().__init__(gender, name, weapon, shield=shield, protection=protection)
        self.__health = Tank.__HEALTH

    @property
    def Health(self):
        return self.__health

    @Health.setter
    def Health(self, value):
        self.__health += Tank.__typeTest(value)
        
    @classmethod
    def event(cls, health=350, power=15):
        cls.__HEALTH, cls.__POWER = Tank.__typeTest(health), Tank.__typeTest(power)
    
    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Должно быть int')


class Small_arms(Base_Weapon):

    def __init__(self, type_weapon, range_weapon, damage, type_of_ammunition):
        super().__init__(type_weapon, range_weapon, damage)
        self.__type_of_ammunition = type_of_ammunition


class Cutting_weapons(Base_Weapon):

    def __init__(self, type_weapon, range_weapon, damage):
        super().__init__(type_weapon, range_weapon, damage)


class Shotgun_weapons(Base_Weapon):

    def __init__(self, type_weapon, range_weapon, damage):
        super().__init__(type_weapon, range_weapon, damage)


def printer(f):
    def wrapper(a):
        print('===============================')
        f(a)
        print('===============================')
    return wrapper

def create_counter():
    i = 0
    def iner():
        nonlocal i
        i += 1
        return i 
    return iner

def main():
    import json
    Characters_json = []
    count = create_counter()
    for _ in range(int(input('Сколько игроков: '))):
    #---------------------------------------------------------------------------------------
        print(f'-------Пользователь {count()} -------')
        print('Выберите класс персонажа', '1: Лучник', '2: Воин', '3: Танк', sep='\n')
        
        i, name, gender = int(input('Введите номер понравившегося класса: ')), input('Введите имя: '), input('Выберите пол: ')

        if i == 1:
            print('', 'Введите тип оружия', '1: Лук', '2: Арбалет', sep='\n')
            j = int(input('Введите номер понравившегося оружия: ')) 
            if j == 1:
                weapon = Small_arms('Лук', 100, 40, 'стрелы')
            elif j == 2:
                weapon = Small_arms('Арбалет', 200, 70, 'болты')
            obj = Archer(gender, name, weapon)
        elif i == 2:
            print('', 'Введите тип оружия', '1: Одноручный меч', '2: Двуручный меч', sep='\n')
            j = int(input('Введите номер понравившегося оружия: ')) 
            if j == 1:
                weapon = Cutting_weapons('Одноручный меч', 1, 20)
            elif j == 2:
                weapon = Cutting_weapons('Двуручный меч', 2, 40)
            obj = Warrior(gender, name, weapon)
        elif i == 3:
            print('', 'Введите тип оружия', '1: Щит + Одноручный меч', '2: Щит + Кистень(Булава на цепочке)', sep='\n')
            j = int(input('Введите номер понравившегося оружия: '))
            if j == 1:
                weapon = Cutting_weapons('Одноручный меч', 1, 20)
            elif j == 2:
                weapon = Shotgun_weapons('Кистень', 1, 30)
            obj = Tank(gender, name, weapon, 'Есть', 20)

        Character = {
            'lvl':        obj.Lvl,
            'class':      obj.__class__.__name__,
            'name':       obj.Name,
            'gender':     obj.Gender,
            'health':     obj.Health,
            'weapon':     obj.Type_weapon,
            'range':      obj.Range,
            'damage':     obj.Damage,
            'shield':     obj.Shield,
            'protection': obj.Protection
        }

        Characters_json.append(json.dumps(Character, ensure_ascii=False))
    #---------------------------------------------------------------------------------------


    
    with open('Players.txt', 'a', encoding='utf-8') as write_f_txt:
        for w in Characters_json:
            write_f_txt.write(w + '\n')

    Characters = []
    with open('Players.txt', 'r', encoding='utf-8') as read_f_txt:
        for i in read_f_txt:
            Characters.append(json.loads(i))

    count1 = create_counter()

    @printer
    def out(f):
        for Char in f:
            print(f'-------Пользователь {count1()} -------')
            for key, value in Char.items():
                print(f"{key}:{value}")
    out(Characters)
    
# Это вариант как можно использовать перегрузку
"""weapon_t1 = Small_arms('Лук', 20, 50, 'стрелы')
t1 = Archer('Мужчина', 'Alex', weapon_t1)
weapon_t2 = Shotgun_weapons('Кистень', 1, 30)
t2 = Tank('Мужчина', 'Bone_man', weapon_t2, 'Есть', 30)

print(t1)
print(t2)
t3 = t1 + t2
print(t3) """

if __name__ == '__main__':
    main()