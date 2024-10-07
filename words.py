word = input("Введите слово, состоящее только из латинских букв: ")
length = len(word)
if length % 2 == 0:
    mid1 = word[length // 2 - 1]
    mid2 = word[length // 2]
    print(f"Результат: {mid1 + mid2}")
else:
    mid = word[length // 2]
    print(f"Результат: {mid}")
