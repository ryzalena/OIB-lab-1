
# открытие файлов
litter_frequency = {}
with open('frequency.txt', mode='r', encoding='utf-8') as file:
    for i in range(33):
        r = file.readline()
        r=r.split('\n')
        r=r[0].split('=')
        litter_frequency[r[0]] = [r[1]]
    file.close()
print(litter_frequency)

text = ''
with open('text2.txt', mode='r', encoding='utf-8') as file:
    text = file.read()
    file.close()
print(text)

# определение частоты в тексте

text_frequency = {}
l = len(text)
text_litters = []
for i in text:
    if text_litters.count(i) == 0:
        text_litters.append(i)
print(text_litters)

for i in text_litters:
    text_frequency[i] = text.count(i) / l


print(text_frequency)
print('-'*10)
text_frequency = sorted(text_frequency.items(), key = lambda item: item[1])
text_frequency = dict(text_frequency[::-1])
print(text_frequency)

item_litter_frequency = tuple(litter_frequency.items())
item_text_frequency = tuple(text_frequency.items())
for i in range (32):
    print(i, ' ', item_litter_frequency[i], '\t\t', item_text_frequency[i])


# расшифровка

new_text = text
print('Й -> Т')
new_text = new_text.replace(item_text_frequency[7][0], item_litter_frequency[6][0])
print('Ф -> Й')
new_text = new_text.replace(item_text_frequency[24][0], item_litter_frequency[25][0])
print('Ш -> Ф')
new_text = new_text.replace(item_text_frequency[25][0], item_litter_frequency[24][0])
print('Ы -> Ш')
new_text = new_text.replace(item_text_frequency[31][0], item_litter_frequency[29][0])
print('\' \' -> Ы')
new_text = new_text.replace(item_text_frequency[17][0], item_litter_frequency[17][0])
print('M -> \' \'')
new_text = new_text.replace(item_text_frequency[0][0], item_litter_frequency[0][0])
print('2 -> М')
new_text = new_text.replace(item_text_frequency[15][0], item_litter_frequency[10][0])
print('О -> В')
new_text = new_text.replace(item_text_frequency[8][0], item_litter_frequency[9][0])
print('Е -> О')
new_text = new_text.replace(item_text_frequency[1][0], item_litter_frequency[1][0])
print('> -> Е')
new_text = new_text.replace(item_text_frequency[4][0], item_litter_frequency[3][0])
print('Д -> Н')
new_text = new_text.replace(item_text_frequency[5][0], item_litter_frequency[5][0])
print('Р -> Д')
new_text = new_text.replace(item_text_frequency[10][0], item_litter_frequency[12][0])
print('И -> С')
new_text = new_text.replace(item_text_frequency[6][0], item_litter_frequency[7][0])
print('У -> И')
new_text = new_text.replace(item_text_frequency[2][0], item_litter_frequency[2][0])
print('Ч -> У')
new_text = new_text.replace(item_text_frequency[19][0], item_litter_frequency[19][0])
print('К -> Ю')
new_text = new_text.replace(item_text_frequency[22][0], item_litter_frequency[26][0])
print('Х -> К')
new_text = new_text.replace(item_text_frequency[13][0], item_litter_frequency[14][0])
print('Щ -> Х')
new_text = new_text.replace(item_text_frequency[20][0], item_litter_frequency[23][0])
print('Ь -> Щ')
new_text = new_text.replace(item_text_frequency[28][0], item_litter_frequency[30][0])
print('5 -> Б')
new_text = new_text.replace(item_text_frequency[29][0], item_litter_frequency[27][0])
print('Л -> Я')
new_text = new_text.replace(item_text_frequency[14][0], item_litter_frequency[13][0])
print('1 -> Л')
new_text = new_text.replace(item_text_frequency[11][0], item_litter_frequency[11][0])
print('Ъ -> Ц')
new_text = new_text.replace(item_text_frequency[23][0], item_litter_frequency[28][0])
print('А -> Ь')
new_text = new_text.replace(item_text_frequency[18][0], item_litter_frequency[18][0])
print('4 -> A')
new_text = new_text.replace(item_text_frequency[3][0], item_litter_frequency[4][0])
print('П -> Г')
new_text = new_text.replace(item_text_frequency[26][0], item_litter_frequency[22][0])
print('r -> П')
new_text = new_text.replace(item_text_frequency[12][0], item_litter_frequency[15][0])
print('t -> Р')
new_text = new_text.replace(item_text_frequency[9][0], item_litter_frequency[8][0])
print('7 -> Ж')
new_text = new_text.replace(item_text_frequency[27][0], item_litter_frequency[21][0])
print('< -> Ч')
new_text = new_text.replace(item_text_frequency[21][0], item_litter_frequency[20][0])
print('8 -> З')
new_text = new_text.replace(item_text_frequency[16][0], item_litter_frequency[16][0])

print(new_text)

with open('result.txt', mode='a', encoding='utf-8') as file:
    file.write(new_text)
    file.close()
