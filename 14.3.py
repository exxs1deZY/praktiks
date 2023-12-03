import csv

nums = (28, -144, 50, 831, 72, 140, 90, 120)

max_num = 0

with open("output.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([f"Самое большое число, кратное 5, в кортеже: {max_num}"])

with open("output.csv", "r") as file:
    reader = csv.reader(file)
    content = next(reader)
    print(content[0])
