class Sword:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return f"{self.name} наносит {self.damage} урона!"

def double_damage(cls):
    original_attack = cls.attack

    def new_attack(self):
        original_result = original_attack(self)
        return f"{original_result}\nДвойной урон! {self.name} теперь наносит {self.damage * 2} ед. урона!"

    cls.attack = new_attack
    return cls

@double_damage
class SwordWithDoubleDamage(Sword):
    pass

sword = SwordWithDoubleDamage(name="Sekiro", damage=10)
print(sword.attack())
