import time

class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

list = list(range(1000000))


# Использование индексов
start_time = time.time()
max_num = 0
for i in range(len(list)):
    num = list[i]
    if num % 5 == 0 and num > max_num:
        max_num = num
end_time = time.time()
print(f"Самое большое число, кратное 5, в списке с использованием индексов: {max_num}")
print("Время выполнения с использованием индексов:", end_time - start_time)

# Использование итераторов и цикла while
start_time = time.time()
max_num = 0
iterator = ListIterator(list)
while True:
    try:
        num = next(iterator)
        if num % 5 == 0 and num > max_num:
            max_num = num
    except StopIteration:
        break
end_time = time.time()
print(f"Самое большое число, кратное 5, в списке с использованием итераторов: {max_num}")
print("Время выполнения с использованием итераторов:", end_time - start_time)
