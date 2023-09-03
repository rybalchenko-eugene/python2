import task4 as source


class Fabrika(source.Animal):
    """
    Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
    Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
    """

    def __init__(self, *args):
        self.anymal_type = args[0]
        super().__init__(args[1], args[2])
        self.param = args[3:]

    def creation(self):
        match self.anymal_type:
            case 'Dog':
                model = source.Dog(self.name, self.age, self.param[0], self.param[1], self.param[2])
            case 'Kotopes':
                model = source.Kotopes(self.name, self.age, self.param[0])
            case 'Fish':
                model = source.Fish(self.name, self.age, self.param[0], self.param[1])
            case _:
                model = None
        return model

    def __str__(self):
        return f'{self.__dict__}'


if __name__ == '__main__':
    param1 = 'Dog', 'Rex14', 5, 'рыжая', 'овчарка', True
    param2 = 'Kotopes', 'Murzilka', 5, 2 #error data
    param3 = 'Fish', 'Nemo', 3, False, 2


    animal1 = Fabrika(*param1).creation()
    animal2 = Fabrika(*param2).creation()
    animal3 = Fabrika(*param3).creation()

    print(f'{animal1.__class__} {animal1}')
    print(f'{animal2.__class__} {animal2}')
    print(f'{animal3.__class__} {animal3}')
