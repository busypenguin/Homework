def hanoi(rings, first_rod, third_rod, second_rod, count=0):
    """
    Рекурсивная функция для решения задачи Ханойской башни.

    Args:
        rings: Количество колец.
        first_rod: Стержень, с которого нужно переместить диски.
        second_rod: Вспомогательный стержень.
        third_rod: Стержень, на который нужно переместить диски.
        count: Текущее количество ходов (используется для рекурсии).

    Returns:
        Количество ходов, необходимых для решения задачи.
    """
    if rings == 1:
        print(f"Переместить кольцо {rings} с {first_rod} на {third_rod}")
        with open("решение.txt", "a") as f:   # Создаём или открываем файл и записываем ход в него
            f.write(f"Переместить кольцо {rings} с {first_rod} на {third_rod}\n")
        return count + 1
    else:
        count = hanoi(rings - 1, first_rod, second_rod, third_rod, count)
        print(f"Переместить кольцо {rings} с {first_rod} на {third_rod}")
        with open("решение.txt", "a") as f:   # Создаём или открываем файл и записываем ход в него
            f.write(f"Переместить кольцо {rings} с {first_rod} на {third_rod}\n")
        count = (hanoi(rings - 1, second_rod, third_rod, first_rod, count))  # Считаем количество ходов
        return count + 1


if __name__ == "__main__":
    rings = int(input("Введите количество колец: "))
    with open("решение.txt", "a") as f:    # Открываем файл и записываем количество колец в файл
        f.write(f"\nРешение для количества колец: {rings} \n")

    first_rod = "A"
    second_rod = "B"
    third_rod = "C"
    total_moves = hanoi(rings, first_rod, third_rod, second_rod)
    print(f"\nЧтобы переместить количество колец: {rings}, необходимо количество ходов: {total_moves}.")
