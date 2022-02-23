"""
    Tag: string

    We want to design a language called pig latin with following rules. 

    1. General rule: take the first letter of a word, move it to the end, and add "ay". Example: "hello" becomes "ellohay".
    2. A phrase with multiple words should translate each word: "hello world" becomes "ellohay orldway"
    3. A word which begins with a vowel keeps its first letter, and just adds "way" to the end of the word: "eat apples" becomes "eatway applesway"
    4. A word which is capitalized should remain capitalized after translation: "Hello world" becomes "Ellohay orldway"
    5. A phrase with punctuation should maintain the position of the punctuation: "Hello, world!" becomes "Ellohay, orldway!"
    6. consonents stay to drunk unkdr
    7. Q and U stays together
"""

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}


def piglatin(word: str) -> str:
    if not word:
        return ''
    
    punctuation = None
    if not word[-1].isalnum():
        punctuation = word[-1]
        word = word[:-1]

    is_upper = False
    if word[0].isupper():
        is_upper=True

    out_word = ''
    if word[0] in vowels:
        out_word = word + 'way'
    else: 
        out_word = word[1:] + word[0] + 'ay'
    
    out_word = out_word.title() if is_upper else out_word
    return out_word if not punctuation else out_word + punctuation


def pig_latin_phrase(phrase: str) -> str:
    words = phrase.split(' ')

    output_phrase = ''
    for word in words:
        output_phrase += piglatin(word) + ' '
    return output_phrase[:-1]


assert(piglatin("hello") == "ellohay")
assert(pig_latin_phrase("") == "")
assert(pig_latin_phrase("Hello") == "Ellohay")
assert(pig_latin_phrase("Hello world") == "Ellohay orldway")
assert(pig_latin_phrase("eat apples") == "eatway applesway")
assert(pig_latin_phrase("eat hello apples world") == "eatway ellohay applesway orldway")
assert(pig_latin_phrase("Eat Hello apples world") == "Eatway Ellohay applesway orldway")
assert(pig_latin_phrase("Eat! Hello# apples world hi^") == "Eatway! Ellohay# applesway orldway ihay^")

print("Tests passed!")
