import random

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
           
    return ' '.join(printed_word)


def test_func():
    word = word_pick()
    letter = random_letter(word)
    
    printed_word = hidden_word(word, letter)
    
    return printed_word

print(test_func())




