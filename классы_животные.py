class Animals:
    def __init__(self, name = None, weight = None):
            self.name = name
            self.weight = weight
    def eat(self, eat = None):
        return "{} покормили".format(self.name)

# class Dog(Animals):
#     def __init__(self, name, breed = None):
#         super().__init__(name)
#         self.breed = breed
#     def say(self):
#         return "Собака по имени {0} кричит: гав-гааав-гав".format(self.name)
#     def milk(self):
#         return "Собаку {0} нельзя доить!".format(self.name)
#     def hair(self):
#         return "Собаку {0} нельзя стричь!".format(self.name)
#     def eggs(self):
#         return "У собаки {0} нельзя собирать яица!".format(self.name)

class Goose(Animals):
    total_weight = 0
    max_weight = 0
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        Goose.total_weight = Goose.total_weight + self.weight
        if Goose.max_weight<self.weight:
            Goose.max_weight = self.weight
    def say(self):
        return "Гусь по имени {0} с весом {1}грамм кричит: га-га-га".format(self.name, self.weight)
    def milk(self):
        return "Гуся {0} нельзя доить!".format(self.name)
    def hair(self):
        return "Гуся {0} нельзя стричь!".format(self.name)
    def eggs(self):
        return "Яйца у гуся {0} собраны!".format(self.name)

class Cow(Animals):
    total_weight = 0
    max_weight = 0
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        Cow.total_weight = Cow.total_weight + self.weight
        if Cow.max_weight<self.weight:
            Cow.max_weight = self.weight
    def say(self):
        return "Корова по имени {0} с весом {1}грамм кричит: муу-уу-уу".format(self.name, self.weight)
    def milk(self):
        return "Корову по имени {0} подоили".format(self.name)
    def hair(self):
        return "Корову {0} нельзя стричь!".format(self.name)
    def eggs(self):
        return "У коровы {0} нельзя собирать яица!".format(self.name)

class Sheep(Animals):
    total_weight = 0
    max_weight = 0
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        Sheep.total_weight = Sheep.total_weight + self.weight
        if Sheep.max_weight<self.weight:
            Sheep.max_weight = self.weight
    def say(self):
        return "Овца по имени {0} с весом {1}грамм кричит: бяя-яя-яя".format(self.name, self.weight)
    def milk(self):
        return "Овцу {0} нельзя доить!".format(self.name)
    def hair(self):
        return "Овца {0} пострижена!".format(self.name)
    def eggs(self):
        return "У овцы {0} нельзя собирать яица!".format(self.name)

class Chicken(Animals):
    total_weight = 0
    max_weight = 0
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        Chicken.total_weight = Chicken.total_weight + self.weight
        if Chicken.max_weight<self.weight:
            Chicken.max_weight = self.weight
    def say(self):
        return "Курица по имени {0} с весом {1}грамм кричит: цып-цып-цып".format(self.name, self.weight)
    def milk(self):
        return "Курицу {0} нельзя доить!".format(self.name)
    def hair(self):
        return "Курицу {0} нельзя стричь!".format(self.name)
    def eggs(self):
        return "Яйца у курицы {0} собраны".format(self.name)

class Goat(Animals):
    total_weight = 0
    max_weight = 0
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        Goat.total_weight = Goat.total_weight + self.weight
        if Goat.max_weight<self.weight:
            Goat.max_weight = self.weight
    def say(self):
        return "Коза по имени {0} с весом {1}грамм кричит: Ме-е-е-е".format(self.name, self.weight)
    def milk(self):
        return "Козу по имени {0} подоили".format(self.name)
    def hair(self):
        return "Козу {0} нельзя стричь!".format(self.name)
    def eggs(self):
        return "У козы {0} нельзя собирать яица!".format(self.name)

class Duck(Animals):
    total_weight = 0
    max_weight = 0
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
        Duck.total_weight = Duck.total_weight + self.weight
        if Duck.max_weight<self.weight:
            Duck.max_weight = self.weight
    def say(self):
        return "Утка по имени {0} с весом {1}грамм кричит: кряк-кряк".format(self.name, self.weight)
    def milk(self):
        return "Утку {0} нельзя доить!".format(self.name)
    def hair(self):
        return "Утку {0} нельзя стричь!".format(self.name)
    def eggs(self):
        return "Яйца у утки {0} собраны!".format(self.name)

goose1 = Goose("Серый",1000)
goose2 = Goose("Белый",1200)
cow = Cow("Манька",6000)
sheep1 = Sheep("Барашек",3000)
sheep2 = Sheep("Кудрявый",3300)
chicken1 = Chicken("Ко-Ко",800)
chicken2 = Chicken("Кукареку",820)
goat1 = Goat("Рога",300)
goat2 = Goat("Копыта",320)
duck = Duck("Кряква",200)
# print(dog.name)
# print(goose1.name)
# print(goose2.name)
# print(cow.name)
# print(sheep1.name)
# print(sheep2.name)
# print(chicken1.name)
# print(chicken2.name)
# print(goat1.name)
# print(goat2.name)
# print(duck.name)
# print("Слушаем звуки животных:")
# print(dog1.say())
# print(dog2.say())
# print(goose1.say())
# print(goose2.say())
# print(cow.say())
# print(sheep1.say())
# print(sheep2.say())
# print(chicken1.say())
# print(chicken2.say())
# print(goat1.say())
# print(goat2.say())
# print(duck.say())
# print("\nДоим животных:")
# print(dog1.milk())
# print(dog2.milk())
# print(goose1.milk())
# print(goose2.milk())
# print(cow.milk())
# print(sheep1.milk())
# print(sheep2.milk())
# print(chicken1.milk())
# print(chicken2.milk())
# print(goat1.milk())
# print(goat2.milk())
# print(duck.milk())
# print("\nСтрижка животных:")
# print(dog1.hair())
# print(dog2.hair())
# print(goose1.hair())
# print(goose2.hair())
# print(cow.hair())
# print(sheep1.hair())
# print(sheep2.hair())
# print(chicken1.hair())
# print(chicken2.hair())
# print(goat1.hair())
# print(goat2.hair())
# print(duck.hair())
# print("\nСбор яиц на ферме:")
# print(dog1.eggs())
# print(dog2.eggs())
# print(goose1.eggs())
# print(goose2.eggs())
# print(cow.eggs())
# print(sheep1.eggs())
# print(sheep2.eggs())
# print(chicken1.eggs())
# print(chicken2.eggs())
# print(goat1.eggs())
# print(goat2.eggs())
# print(duck.eggs())


print('На ферме у Дядюшки Джо есть животные:'
      '\n1: гуси "Серый" и "Белый"'
      '\n2: корова "Маньку"'
      '\n3: овцы "Барашек" и "Кудрявый"'
      '\n4: куры "Ко-Ко" и "Кукареку"'
      '\n5: козы "Рога" и "Копыта"'
      '\n6: утка "Кряква"')
print('Введите номер животного и я покажу, как звучит животное: ')
x = int(input())
if x == 1:
    print(goose1.say())
    print(goose2.say())
elif x == 2:
    print(cow.say())
elif x == 3:
    print(sheep1.say())
    print(sheep2.say())
elif x == 4:
    print(chicken1.say())
    print(chicken2.say())
elif x == 5:
    print(goat1.say())
    print(goat2.say())
elif x == 6:
    print(duck.say())


#общий вес всех животных
total_weight = Goose.total_weight + Cow.total_weight + Sheep.total_weight + Chicken.total_weight + Goat.total_weight + Duck.total_weight
print("\nОбщий вес всех животных на ферме", total_weight)

# #название самого тяжелого животного
# print(Goose.max_weight)
# print(Cow.max_weight)
# print(Sheep.max_weight)
# print(Chicken.max_weight)
# print(Goat.max_weight)
# print(Duck.max_weight)

dict = {}
dict["Гусь"] = Goose.max_weight
dict["Корова"] = Cow.max_weight
dict["Овца"] = Sheep.max_weight
dict["Курица"] = Chicken.max_weight
dict["Коза"] = Goat.max_weight
dict["Утка"] = Duck.max_weight

max_weight = max(dict.values())
final_dict = {k:v for k, v in dict.items() if v == max_weight}

print('Самое тяжелое животное:',final_dict)