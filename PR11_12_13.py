
class Base_Weapon:

    def __init__(self, type_weapon, range_weapon, damage_weapon):
        self.type, self.range, self.damage = type_weapon, range_weapon, damage_weapon



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
    def Name_weapon(self):
        return self.__weapon.type

    @Name_weapon.setter
    def Name_weapon(self, value):
        self.__weapon.type = value

    @property
    def Range(self):
        return self.__weapon.range

    @Range.setter
    def Range(self, value):
        self.__weapon.range += Base_class.__typeTest(value)

    @property
    def Damage(self):
        return self.__weapon.damage

    @Damage.setter
    def Damage(self, value):
        self.__weapon.damage += Base_class.__typeTest(value)

    @classmethod
    def event(cls, lvl=1, health=100):
        cls.__LVL, cls.__HEALTH = Base_class.__typeTest(lvl), Base_class.__typeTest(health)

    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError('Должно быть int')


    def __str__(self):
        return f'Уровень:{self.Lvl}\nКласс:{self.__class__.__name__}\nИмя:{self.Name}\nПол:{self.Gender}\nЗдоровье:{self.Health}\nОружие:{self.Name_weapon}\nРадиус атаки:{self.Range}\nУрон:{self.Damage}\nЩит:{self.Shield}\nЗащита:{self.Protection}\n'


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
    from json import loads, dumps
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
                weapon = Base_Weapon('Лук', 100, 40)
            elif j == 2:
                weapon = Base_Weapon('Арбалет', 200, 70)
            obj = Archer(gender, name, weapon)
        elif i == 2:
            print('', 'Введите тип оружия', '1: Одноручный меч', '2: Двуручный меч', sep='\n')
            j = int(input('Введите номер понравившегося оружия: ')) 
            if j == 1:
                weapon = Base_Weapon('Одноручный меч', 1, 20)
            elif j == 2:
                weapon = Base_Weapon('Двуручный меч', 2, 40)
            obj = Warrior(gender, name, weapon)
        elif i == 3:
            print('', 'Введите тип оружия', '1: Щит + Одноручный меч', '2: Щит + Кистень(Булава на цепочке)', sep='\n')
            j = int(input('Введите номер понравившегося оружия: '))
            if j == 1:
                weapon = Base_Weapon('Одноручный меч', 1, 20)
            elif j == 2:
                weapon = Base_Weapon('Кистень', 1, 30)
            obj = Tank(gender, name, weapon, 'Есть', 20)

        Character = {
            'lvl':        obj.Lvl,
            'class':      obj.__class__.__name__,
            'name':       obj.Name,
            'gender':     obj.Gender,
            'health':     obj.Health,
            'weapon':     obj.Name_weapon,
            'range':      obj.Range,
            'damage':     obj.Damage,
            'shield':     obj.Shield,
            'protection': obj.Protection
        }

        Characters_json.append(dumps(Character, ensure_ascii=False))
    #---------------------------------------------------------------------------------------


    
    with open('Players.txt', 'a', encoding='utf-8') as write_f_txt:
        for w in Characters_json:
            write_f_txt.write(w + '\n')


    with open('Players.txt', encoding='utf-8') as read_f_txt:
        Character = [loads(r) for r in read_f_txt]


    @printer
    def out(f):
        count1 = create_counter()
        for Char in f:
            print(f'-------Пользователь {count1()} -------')
            for key, value in Char.items():
                print(f"{key}:{value}")
    out(Character)
    



if __name__ == '__main__':
    main()