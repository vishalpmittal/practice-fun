'''
    tag: string, frequently


    Most frequent 2 words in the text.
    -------------I/P-------------
    hello How are you doing?
    I am doing great.
    Thank You. How you doing.
    you.
    --------------O/P------------
    ["you", "doing"]
    -------------------------

    Args: Text > 3000 chars
'''

from typing import List
import re
from collections import Counter


def most_freq_n_words(text: str, n: int) -> List[str]:
    return (Counter(re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())).most_common()[:n])


def most_frequent_two(text: str) -> List[str]:
    # normalize and extract words (letters and apostrophes)
    words = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())
    # count frequencies
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1

    # find top two without sorting
    top1_word, top1_count = None, 0
    top2_word, top2_count = None, 0

    for w, c in counts.items():
        if c > top1_count or (c == top1_count and (top1_word is None or w < top1_word)):
            # demote top1 to top2
            top2_word, top2_count = top1_word, top1_count
            top1_word, top1_count = w, c
        elif c > top2_count or (c == top2_count and (top2_word is None or w < top2_word)):
            top2_word, top2_count = w, c

    result = []
    if top1_word is not None:
        result.append(top1_word)
    if top2_word is not None:
        result.append(top2_word)
    return result


# Example using the sample from the attachment:
if __name__ == "__main__":
    text = """
    hello How are you doing?
    I am doing great.
    Thank You. How you doing.
    you."""
    print(most_frequent_two(text))
    print(most_frequent_two('w1 w2 w3 w4 w2 w1 w2'))
    print(most_frequent_two('w1 w2 w1 w2'))
    print(most_frequent_two('w1 w1 w2 w2 w2'))
    print(most_freq_n_words(text, 3))
