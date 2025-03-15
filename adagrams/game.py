from random import randint

def draw_letters():
    hand = []
    letters_dictionary ={
    'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 
    'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 
    'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1
    }

    letters_list = []
    for letter, count in letters_dictionary.items():
        letters_list.extend(letter * count)
    
    for i in range(10):
        random_letter_index = randint(0, len(letters_list) - 1)
        letter = letters_list[random_letter_index]
        hand.append(letter)
        letters_list.pop(random_letter_index)

    return hand
def uses_available_letters(word, letter_bank):
    word_upper = word.upper()
    bank_dict = {}
    for i in letter_bank:
        if i in bank_dict:
            bank_dict[i] += 1
        else:
            bank_dict[i] = 1

    for i in word_upper:
        if i not in bank_dict or bank_dict[i] == 0:
            return False
        bank_dict[i] -= 1

    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass
