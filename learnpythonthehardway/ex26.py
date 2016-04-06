#typed by my Hand
def break_words(stuff):
    'This function will break up words for us.'
    words = stuff.split('')
    return words

def sort_words(words):
    'sorts the words'
    return sorted(words)

def print_first_word(words):
    'Prints the first word after poping it off.'
    word = words[0]
    print word
    
print_first_word('iseeyou')