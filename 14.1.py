import json

a = (-2, 5, -10, 8, -15, 20)
positive_numbers = [num for num in a if num > 0]

with open("output.json", "w") as file:
    json.dump({"positive_numbers": positive_numbers}, file)

with open("output.json", "r") as file:
    data = json.load(file)
    print("Список положительных чисел из исходного кортежа:")
    print(data["positive_numbers"])
