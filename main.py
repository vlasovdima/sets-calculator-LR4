# калькулятор множеств

def read_set(path):
    # читаем файл и делаем множество
    with open(path, "r") as f:
        data = f.read().split()
        return set(data)


def set_calculator(file1, file2):

    A = read_set(file1)
    B = read_set(file2)

    print("Множество A:", A)
    print("Множество B:", B)

    while True:
        print("\nВыбери операцию:")
        print("1 - объединение (A ∪ B)")
        print("2 - пересечение (A ∩ B)")
        print("3 - разность (A - B)")
        print("4 - симметрическая разность")
        print("0 - выход")

        choice = input(">> ")

        if choice == "1":
            print("Результат:", A | B)

        elif choice == "2":
            print("Результат:", A & B)

        elif choice == "3":
            print("Результат:", A - B)

        elif choice == "4":
            print("Результат:", A ^ B)

        elif choice == "0" or choice == "exit":
            print("Выход")
            break

        else:
            print("Неправильный ввод")


# запуск
if __name__ == "__main__":
    file1 = input("Введите путь к первому файлу: ")
    file2 = input("Введите путь ко второму файлу: ")

    set_calculator(file1, file2)
