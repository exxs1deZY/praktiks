class Sword:
    total_swords = 0

    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage
        Sword.total_swords += 1

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    @staticmethod
    def get_total_swords():
        return Sword.total_swords


sword1 = Sword("Острие Справедливости", 190)
sword2 = Sword("Клинок Тьмы", 45)
sword3 = Sword("Жнец Вечной Пустоты", 780)


print(f"Имя меча 1: {sword1.get_name()}")
print(f"Урон меча 1: {sword1.get_damage()}")

print(f"Имя меча 2: {sword2.get_name()}")
print(f"Урон меча 2: {sword2.get_damage()}")

print(f"Имя меча 3: {sword3.get_name()}")
print(f"Урон меча 3: {sword3.get_damage()}")

print(f"Общее количество мечей: {Sword.get_total_swords()}")
