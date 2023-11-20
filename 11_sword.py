class Sword:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Katana(Sword):
    def __init__(self, name, damage, rarity):
        super().__init__(name, damage)
        self.rarity = rarity

class Sabre(Katana):
    def __init__(self, name, damage, rarity):
        super().__init__(name, damage, rarity)


sword1 = Sword("Клинок Тьмы", 45)
sword2 = Sword("Острие Справедливости", 190)
sword3 = Katana("Жнец Вечной Пустоты", 780, "Легендарный")
sword4 = Sabre("Пронзающий Небеса", 480, "Эпический")


print(f"Имя меча: {sword1.name}")
print(f"Урон меча: {sword1.damage}")

print(f"Имя меча: {sword2.name}")
print(f"Урон меча: {sword2.damage}")

print(f"Имя меча: {sword3.name}")
print(f"Урон меча: {sword3.damage}")
print(f"Редкость: {sword3.rarity}")

print(f"Имя меча: {sword4.name}")
print(f"Урон меча: {sword4.damage}")
print(f"Редкость: {sword4.rarity}")














