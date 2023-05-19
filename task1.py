
#Создание словаря для таблицы Виженера

nonsplit_alphabet = 'А,Б,В,Г,Д,Е,Ж,З,И,Й,К,Л,М,Н,О,П,Р,С,Т,У,Ф,Х,Ц,Ч,Ш,Щ,Ъ,Ы,Ь,Э,Ю,Я'
split_alphabet = nonsplit_alphabet.split(',')
dict_alphabet = {}

for i in range(32):
    dict_alphabet[split_alphabet[i]] = i

print(dict_alphabet)

alphabet = {}
for i in range(32):
    alphabet[i] = split_alphabet[i:i+32:1] + split_alphabet[0:i]

for i in range(32):
    print(alphabet[i])

# Получение и преобразование данных
text1 = ''
with open('text1.txt', mode='r', encoding='utf-8') as file:
    text1 = file.readline()
    file.close()
print(text1)

codeword1 = ''
with open('codeword1.txt', mode='r', encoding='utf-8') as file:
    codeword1 = file.readline()
print(codeword1)

text1 = text1.replace(' ', '')
print(text1)

n = int(len(text1) / len(codeword1) + 1)
wordstr = codeword1 * n
wordstr = wordstr[:len(text1)]

print(wordstr)
print(len(wordstr))
print(len(text1))

# шифрование
# Индексиование букв
text_numbers = []
word_numbers = []
for i, j in zip(text1, wordstr):
    text_numbers.append(dict_alphabet[i])

    try:
        word_numbers.append(dict_alphabet[j])
    except KeyError:
        print(' ')
print(text_numbers)
print('-'*30)
print(word_numbers)

new_text = ''
for i, j in zip(text_numbers, word_numbers):
    new_text += alphabet[i][j]
print(new_text)

with open('shifr1.txt', mode='a', encoding='utf-8') as file:
    file.write(new_text)
    file.close()