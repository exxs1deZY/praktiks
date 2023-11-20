nums = (28, -144, 50, 831, 72, 140, 90, 120)

max_num = 0

for num in nums:
    if num % 5 == 0 and num > max_num:
        max_num = num

print(f"Самое большое число, кратное 5, в кортеже: {max_num}")
