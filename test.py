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

def word_pick():
    with open("words_base.txt", "r", encoding='utf-8') as file:
        words_list = [str_word.strip() for str_word in file]

    word = random.choice(words_list)
    return word


def random_letter(word):
    first_random_letter = random.choice(word)
    return first_random_letter


def hidden_word(word, letter):
    printed_word = ''
    for i in word:
        if i == letter:
            printed_word += i
        else:
            printed_word += '_'
           
    return ''.join(printed_word)


def word_update(players_letter, printed_word, word):
    letters_list = list(printed_word)
    for letter in range(len(word)):
        if word[letter] == players_letter:
              letters_list[letter] = players_letter

    return ''.join(letters_list)
    

def play_game():
    word = word_pick()
    print(word)
    letter = random_letter(word)
    
    printed_word = hidden_word(word, letter)
    print(printed_word)
    
    players_letter = str(input("Введите букву: "))
    
    players_letters_list = []
    
    count = 0
    
    while '_' in printed_word:
        
        if players_letter in players_letters_list:
            print(f'\nВы уже вводили букву {players_letter}')
            
            players_letter = str(input("\nВведите букву: "))
   
        elif players_letter in word:
            
            players_letters_list.append(players_letter)
            
            upd = word_update(players_letter, printed_word, word)
            print(upd)
            printed_word = upd
            
            if '_' not in printed_word:
                
                print('\nВы угадали слово')
                print(f'Все введенные буквы: {players_letters_list}')
                break
            
            players_letter = str(input("\nВведите букву: "))

            
        elif players_letter not in word:
            
            players_letters_list.append(players_letter)
            
            count += 1
            
            print(f'\nБуквы {players_letter} нету в слове')
            print(stages[count - 1])
            
            if count == 6:
                print('Вы проиграли :(')
                print(f'Закагаданное слово - {word}')
                print(f'Все введенные буквы: {players_letters_list}')
                break
            
            players_letter = str(input("\nВведите букву: "))
            
print(play_game())
