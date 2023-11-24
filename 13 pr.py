# Шаг 1: Создаем метакласс
class SwordMeta(type):
    def __new__(cls, name, bases, dct):
        dct['_meta_class'] = cls
        return super().__new__(cls, name, bases, dct)


class Sword(metaclass=SwordMeta):
    def __init__(self, damage, rarity):
        self.damage = damage
        self.rarity = rarity

    def __str__(self):
        return f"Меч с уроном {self.damage} и редкостью {self.rarity}"

sword_collection = []
for i in range(10, 101):
    class_name = f"Меч{i}"
    sword_class = SwordMeta(class_name, (Sword,), {})
    sword_collection.append(sword_class)

# Шаг 4: Демонстрация созданных классов
for sword_class in sword_collection:
    instance = sword_class(damage=10, rarity="Обычный")
    print(instance)
