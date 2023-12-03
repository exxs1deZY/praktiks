import os

try:
    os.remove("output.txt")
except Exception as e:
    print(f"Произошла ошибка: {e}")
