class Sword:
    total_swords = 0

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        Sword.total_swords += 1

    @staticmethod
    def get_total_swords():
        return Sword.total_swords

    def __str__(self):
        return f"Имя меча: {self.name}, Урон меча: {self.damage}"

class Katana(Sword):
    def __init__(self, name, damage, rarity):
        super().__init__(name, damage)
        self.rarity = rarity

    def __str__(self):
        return f"Имя меча: {self.name}, Урон меча: {self.damage}, Редкость: {self.rarity}"

class Sabre(Katana):
    def __init__(self, name, damage, rarity):
        super().__init__(name, damage, rarity)

    def __str__(self):
        return f"Имя меча: {self.name}, Урон меча: {self.damage}, Редкость: {self.rarity}"


sword1 = Sword("Клинок Тьмы", 45)
sword2 = Sword("Острие Справедливости", 190)
sword3 = Sabre("Пронзающий Небеса", 470, "Эпический")
sword4 = Katana("Жнец Вечной Пустоты", 780, "Легендарный")



print(sword1)
print(sword2)
print(sword3)
print(sword4)

print(f"Общее количество мечей: {Sword.get_total_swords()}")
