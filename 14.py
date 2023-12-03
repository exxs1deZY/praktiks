nums = (28, -144, 50, 831, 72, 140, 90, 120)
max_num = 0

try:
    with open("output.txt", "w") as file:
        for num in nums:
            if num % 5 == 0 and num > max_num:
                max_num = num
        file.write(f"Самое большое число, кратное 5, в кортеже: {max_num}")
    print("Данные успешно записаны в файл.")
except Exception as e:
    print(f"Произошла ошибка при записи данных в файл: {e}")

try:
    with open("output.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка при чтении данных из файла: {e}")
