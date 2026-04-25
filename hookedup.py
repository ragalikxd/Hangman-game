import random
stages = [
'_|_',
""" |    
 |
 |
 |
_|_""",
""" ______
 |    |
 |
 |
 |
_|_""",
""" ______
 |    |
 |    o
 |
 |
_|_""",
""" ______
 |    |
 |    o
 |   /|\\
 |
_|_""",
""" ______
 |    |
 |    o
 |   /|\\
 |   / \\
_|_"""
]

with open("words_base.txt", "r", encoding='utf-8') as file:
    words_list = [str_word.strip() for str_word in file]

word = random.choice(words_list)
letters = list(word)
printed_word = ''

first_random_letter = random.choice(letters)

print('/'*73)
print('                 Добро пожаловать в игру Виселица!')
print('Правила игры очень просты. Программа случайно выберает слово из списка. \nВам необходимо отгадать слово, называя буквы русского алфавита. Перед \nвами отобразится количество букв в слове в виде символов "_". \nВы вводите по одной букве. Если такая буква есть в слове, она откроется \nна всех своих позициях. Если буквы нет, засчитывается ошибка, и часть \nвиселицы с человечком добавляется на экран. Всего допускается 6 ошибок. \nИгра заканчивается победой, если вы откроете все буквы до того, как \nчеловечек будет полностью нарисован. Игра заканчивается поражением, \nесли человечек повешен, а слово не отгадано. Вводите только одну \nбукву за раз, цифры и другие символы не принимаются. Удачи!')
print('/'*73)

for i in letters:
    if i == first_random_letter:
        printed_word += i
    else:
        printed_word += '_'

print('\nЗагаданное слово:')
print(' '.join(printed_word))

players_letter = str(input('\nВведите букву: '))

count = 0
used_letters = set()

while '_' in printed_word:

    if len(players_letter) != 1:
        print('Ошибка! Нужно ввести только одну букву')
        players_letter = str(input('\nВведите букву: '))
        
    elif not(players_letter.isalpha()):
        print('Ошибка, вы ввели число')
        players_letter = str(input('\nВведите букву: '))

    elif players_letter in used_letters:
        print(f'Вы уже вводили букву "{players_letter}" Попробуйте еще раз')
        players_letter = str(input('\nВведите букву: '))
    
    elif players_letter in letters:
        used_letters.add(players_letter)
        letters_list = [i for i in printed_word]
        for i in range(len(letters)):
            if letters[i] == players_letter:
                letters_list[i] = players_letter
        printed_word = ''.join(letters_list)

        if '_' not in printed_word:
            print('Вы угадали слово!')
            break
            
        print(' '.join(printed_word))
        players_letter = str(input('\nВведите букву: '))  

    

    elif players_letter not in letters:
        
        used_letters.add(players_letter)
        count += 1    
        
        print(f'\nБуквы "{players_letter}" нету в слове. Попробуй еще раз')

        print (f'осталось попыток {6 - count}/6')

        print(stages[count-1])
        
        if count == 6:
            print('Вы проиграли :(')
            print (f'загаданное слово - {word}')
            break
            
        print(' '.join(printed_word))

        players_letter = str(input('\nВведите букву: '))

print(' '.join(printed_word))
