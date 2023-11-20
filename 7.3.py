def check_super_set(set1, set2):
    return set1.issuperset(set2)

if __name__ == "__main__":
    elements_set1 = input("Введите элементы первого множества: ").split()
    elements_set2 = input("Введите элементы второго множества: ").split()

    set1 = set(elements_set1)
    set2 = set(elements_set2)

    if check_super_set(set1, set2):
        print("Первое множество является супермножеством второго.")
    else:
        print("Первое множество не является супермножеством второго.")
