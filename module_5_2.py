class House: # Создаем Класс
    def __init__(self, name, number_is_floors): # Метод и атрибуты
        self.name = name
        self.number_is_floors = number_is_floors
    def __len__(self):
        return self.number_is_floors


    def __str__(self):
        return str(f'Название Жк: {self.name}, кол-во этажей {self.number_is_floors}')



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))