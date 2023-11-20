class Sword:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return f"{self.name} наносит {self.damage} урона!"

class DoubleDamage:
    def __init__(self, sword):
        self.sword = sword

    def attack(self):
        return f"{self.sword.attack()}\nДвойной урон! {self.sword.name} теперь наносит {self.sword.damage * 2} ед. урона!"


original_sw = Sword(name="Sekiro", damage=10)
double_damage_sw = DoubleDamage(original_sw)

print(double_damage_sw.attack())
