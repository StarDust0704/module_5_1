class House:
    name = 'ЖК Эльбрус'
    # Метод __init__ вызывается при создании нового объекта класса House
    def __init__(self, name, number_of_floors):
        # Присваиваем переданное название дому
        self.name = name
        # Присваиваем переданное количество этажей дому
        self.number_of_floors = number_of_floors

    # Метод go_to принимает новый этаж, на который нужно подняться
    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            # Если этаж находится в допустимом диапазоне, выводим номера этажей от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # Выводим сообщение об ошибке, если этаж вне диапазона
            print("Такого этажа не существует")

# Создаем объект класса House с именем 'ЖК Эльбрус' и 30 этажами
my_house = House('ЖК Эльбрус', 30)

# Вызываем метод go_to для подъема на 15-й этаж
my_house.go_to(31)
