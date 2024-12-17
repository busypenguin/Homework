with open("web_clients_correct.csv", "r", encoding='UTF-8') as f:
    for str_ in f:
        name, device_type, browser, sex, age, bill, region = str_.split(',')
        if sex == 'male':
            sex = 'мужского'
            verb = 'совершил'
        else:
            sex = 'женского'
            verb = 'совершила'
        if device_type == 'mobile':
            device_type = 'телефона'
        elif device_type == 'tablet':
            device_type = 'планшета'
        elif device_type == 'desktop':
            device_type = 'компьютера'
        elif device_type == 'laptop':
            device_type = 'ноутбука'
        with open("web_clients_correct.txt", "a") as f:
            f.write(f'Пользователь {name} {sex} пола, {age} лет {verb} покупку на {bill} у.е. с {device_type} в  браузере {browser}. Регион, из которого совершалась покупка: {region}.')
