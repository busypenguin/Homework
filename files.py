import json
import csv


def process_logs(purchase_log_path, visit_log_path, funnel_path):
    """
    Обрабатывает логи покупок и визитов, добавляет категории и записывает результат.
    """
    try:
        with open(purchase_log_path, 'r', encoding='utf-8') as f:
            purchase_log = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: Файл {purchase_log_path} не найден.")
        return

    purchase_categories = {}
    for line in purchase_log[1:]:   # Пропускаем первую строку (заголовок)
        try:
            record = json.loads(line)
            purchase_categories[record['user_id']] = record['category']
        except json.JSONDecodeError:
            print(f"Ошибка: Не удалось распарсить JSON в строке: {line}")
        except KeyError:
            print(f"Ошибка: Отсутствует ключ 'user_id' или 'category' в строке: {line}")

    try:
        with open(visit_log_path, 'r', encoding='utf-8') as visit_log, \
            open(funnel_path, 'w', encoding='utf-8', newline='') as funnel:
            reader = csv.reader(visit_log, delimiter=',')
        writer = csv.writer(funnel, delimiter=',')
        writer.writerow(['user_id', 'source', 'category'])

        next(reader) # Пропускаем заголовок из visit_log.csv

        for row in reader:
            user_id = row[0]
            if user_id in purchase_categories:
                row.append(purchase_categories[user_id])
                writer.writerow(row)
    except FileNotFoundError:
        print(f"Ошибка: Файл {visit_log_path} не найден.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

    # Пример использования:
    process_logs('purchase_log.txt', 'visit_log__1___2_.csv', 'funnel.csv')
