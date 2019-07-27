import re
# Lesson №8

# Задание:

s = 'Good evening and we proceed to the assignment'
m = 'ab@com, jfuf@mail, ldfet@ru, dfjktu@in'
d = 'ghbt 12-04-1999, kgkhe 25-12-2011, dfhd 21-03-1994 tyet'
nomber = ['8029386827', '8 029 38 68 278', '7876393473']
line = 'Good evening and we proceed to the assignment'

print('Задание №1:')
# 1. вернуть первое слово из строки
result = re.findall(r'^\w+', s)
print(result)

print('Задание №2:')
# 2. вернуть первые 2 символа каждого слова
result = re.findall(r'\b\w.', s)
print(result)

print('Задание №3:')
# 3. вернуть список доменов из списка адресов эл.почты
result = re.findall(r'@\w+.\w+', m)
print(result)

print('Задание №4:')
# 4. извлечь дату из строки
result = re.findall(r'\d{2}.\d{2}.\d{4}', d)
print(result)

print('Задание №5:')
# 5. извлечь все слова, начинающиеся на гласную
result = re.findall(r'\b[eyuioaEYUIOA]\w+', s)
print(result)

print('Задание №6:')
# 6. Проверить телефонный номер (номер должен быть длиной 10 знаков и начинаться с 8 или 9)

for result in nomber:
    if re.match(r'[8-9]{1}[0-9]{9}', result) and len(result) == 10:
        print('Yes')
    else:
        print('No')

print('Задание №7:')
# 7. Разбить строку по нескольким разделителям

result = re.split(r'[;,\s]', line)
print(result)
