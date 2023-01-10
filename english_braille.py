# COMP 202 A2 Part 5
# Author: Felis Sedano

from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
# You may want to define more global variables here
Quote_left = '“'

Quote_right = '”'

Num_op = '⠼'

Num_ed = '⠰'

####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''
    # ADD CODE HERE

    #put the two function two gether and that's it

    text = two_letter_contractions(whole_word_contractions(text))
    return text


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    # ADD CODE HERE
    
    #two make sure the quotes for each direction
    #stil use str.replace function but limit each
    #conversion to only one time
    for i in range(len(text)):
        if '"' in text:
           text = text.replace( '"',Quote_left, 1)
           text = text.replace( '"', Quote_right, 1) 

    return text 


####################################################
# Put your own helper functions here!


def convert_frnumber(text):
    '''(str) -> str
    Convert number to English way of writting braille
    >>> convert_frnumber('Felis"IQ is 08')
    'Felis"IQ is \u283c\u281a\u2813\u2830'
    >>> convert_frnumber('COMP 202 ANd89 9')
    'COMP \u283c\u2803\u281a\u2803\u2830 ANd\u283c\u2813\u280a\u2830 \u283c\u280a\u2830'
    >>> convert_frnumber('101 250')
    '\u283c\u2801\u281a\u2801\u2830 \u283c\u2803\u2811\u281a\u2830'
    >>> convert_frnumber(' It consists of 250 or so letters')
    ' It consists of \u283c\u2803\u2811\u281a\u2830 or so letters'
    '''
    # since for French braille there is NUMBER sign for every single number
    # I decided to change numbers to letters that use the same braille and
    # convert them to braille before other texts are so that these numbers
    # will not affect other characters

    # 'j' is at the beginning because 0 and "j' use the same braille
    a = 'jabcdefghi'
    n = '0123456789'

    x = 0
    z = ''
    y = ''
    while x < (len(text)):
        # that x!=len(text)-1) is to make sure x is not out of range
        if str.isdigit(text[x]) and x != (len(text)-1):
            # y takes the original number string and z takes the
            # similar letter string
            y = y + text[x]
            z = z + a[int(text[x])]

        # if x is out of range or the next character is not a number
        # then convert z to braille and replace characters that 
        # contain y, then clear y and z so that they are ready for the
        # next loop of operation (or stop if out of range)

        elif str.isdigit(text[x]) and x == (len(text)-1):
            y = y + text[x]
            z = z + a[int(text[x])]
            z = text_to_braille(z)
            text= text.replace(y,Num_op + z + Num_ed)
            z = ''
            y = ''


        else:
            if z != '' and y != '':
                z = text_to_braille(z)
                text = text.replace(y,Num_op + z + Num_ed)
                z = ''
                y = ''
        x += 1
   
    return text
    


def convert_frpunctuation(text):
    '''(str)->str
    convert English punctuation to the corresponding Francais
    >>> convert_frpunctuation('?')
    '('
    >>> convert_frpunctuation('()')
    '""'
    >>> convert_frpunctuation(Quote_left + Quote_right)
    '()'
    >>> convert_frpunctuation(Quote_left + '()(??')
    '("""(('
    '''

    # This function was easier, just need to check if
    # each of the characters is in text and replace them
    # with french characters that use same braille
    
    if "(" or ")" in text:
        text = text.replace('(','"')
        text = text.replace(')','"')

    if Quote_left in text or Quote_right in text:
        text = text.replace(Quote_left,'(')
        text = text.replace(Quote_right,')')
    
    if "?" in text:
        text = text.replace('?','(')

    return text



def remove_exceeding(text):
    '''(str)->str
    delete all the overlapping braille for sign of number and
    ending within a seires of number
    >>> remove_exceeding('⠼⠃⠰⠼⠑⠚⠰')
    '⠼⠃⠑⠚⠰'
    
    '''
    # The reason that this function exist was pretty complicated.
    # I was failling test4 and test5 after using convert_frnumber
    # so I checked the text, and realize that some numbers that have
    # more than one character has their first character with Num_op
    # on left side and Num_ed on right side, then another Num_op and
    # this time Number_ed appeared at the end of the last chatacter
    # in that number, so I decided to write another function that fix
    # this problem, and I finally passed all test!(crying)
    
    x = 0
    while x < len(text):
        if Num_ed in text[x] and x+1 < len(text):
            if Num_op in text[x+1]:
                text = text[:x] + text[x:x+2].replace(text[x:x+2],'',2) + text[x+2:]


        x +=1

    return text
            
    
####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250')
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    # You may want to put code after this comment. You can also delete this comment. 
    text = convert_frnumber(text)

    text = convert_quotes(text)

    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text)

    # You may want to put code after this comment. You can also delete this comment
    text = convert_frpunctuation(text)
    

    #Run the text through the French Braille translator
    text = text_to_braille(text)

    # You may want to put code after this comment. You can also delete this comment.
    text = remove_exceeding(text)

    # Replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))


    return text


def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()    # you may want to comment/uncomment along the way
    # and add tests down here
