import re

def validate_car_number(car_id: str) -> tuple[str, str] or tuple[None, None]:
    """
    Проверяет валидность транспортного номера и возвращает номер и регион.

    Args:
        car_id: Строка, представляющая транспортный номер.

    Returns:
        Кортеж (номер, регион), если номер валиден, иначе (None, None).
    """
    # Регулярное выражение для проверки номера: 1 буква, 3 цифры, 2 буквы, 2-3 цифры
    pattern = r'^([АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2})(\d{2,3})$'  # Используем только допустимые буквы
    match = re.match(pattern, car_id.upper())

    if match:
        number = match.group(1)
        region = match.group(2)
        return number, region
    else:
        return None, None


# Примеры использования:
car_id1 = 'А222BС96'
number1, region1 = validate_car_number(car_id1)
if number1:
    print(f"Номер {number1} валиден. Регион: {region1}.")
else:
    print("Номер не валиден.")


car_id2 = 'АБ22ВВ193'
number2, region2 = validate_car_number(car_id2)
if number2:
    print(f"Номер {number2} валиден. Регион: {region2}.")
else:
    print("Номер не валиден.")


car_id3 = 'В123СС12'
number3, region3 = validate_car_number(car_id3)
if number3:
    print(f"Номер {number3} валиден. Регион: {region3}.")
else:
    print("Номер не валиден.")

car_id4 = 'X123AA123' # латинская буква
number4, region4 = validate_car_number(car_id4)
if number4:
    print(f"Номер {number4} валиден. Регион: {region4}.")
else:
    print("Номер не валиден.")

