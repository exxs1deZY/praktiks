from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(f"Факториал 5: {factorial(5)}")
print(f"Факториал 3: {factorial(3)}")  # Уже в кэше
