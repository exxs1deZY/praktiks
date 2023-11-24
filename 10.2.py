class Person:
    total_persons = 0

    def __init__(self, name):
        self.name = name
        Person.total_persons += 1

    @classmethod
    def get_total_persons(cls):
        return cls.total_persons

person1 = Person("Максончик")
person2 = Person("Боб")
print(f"Всего людей: {Person.get_total_persons()}")
