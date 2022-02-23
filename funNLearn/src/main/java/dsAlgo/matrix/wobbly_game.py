
"""
    Tag: matrix, recursive, game, wobbly

    You are given a grid of letters eg: ["acxl", "ptoa", "uekr", "qotm"]
    
    A C X L
    P T O A
    U E K R
    Q O T M

    find out all the words that can be formed by moving sequentially in the grid.
    During the movement you can move horizontally, vertically and diagonally, but can not revisit a letter.
    words formed in above grid: {'quote', 'a', 'tap', 'pat', 'act'}
"""
class WordDictionary:
    def __init__(self, words):
        self.words = words
    
    def is_word(self, word):
        return word in self.words

    def word_starts_with(self, partial_word):
        for word in self.words:
            if word.startswith(partial_word):
                return True
        return False


dictionary = WordDictionary(['a', 'act', 'pat', 'tap', 'quote', 'bicycle', 'car', 'peek', 'alarm'])


def find_words(grid):
    words = set()

    # helper recursive function    
    def helper(curr_word, i, j, included):
        # print(curr_word, i, j, included)
        if not dictionary.word_starts_with(curr_word):
            return

        if dictionary.is_word(curr_word):
            words.add(curr_word)
            
        curr_included = set(included)
        curr_included.add((i, j))

        for x in [i, i-1, i+1]:            # for all neighboring x
            if x >= 0 and x < len(grid):          # valid x 
                for y in [j, j-1, j+1] :                  # for all neighboring y
                    if y >= 0 and y < len(grid[x]):            # valid y

                        # Skip for itself and all already included co-ordinates
                        if (x, y) in curr_included:
                            continue
                        
                        # recursively call helper function
                        helper(curr_word + grid[x][y], x, y, curr_included)

    # traverse through each letter as starting letter for the word
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            helper(grid[a][b], a, b, set())

    return words


grid = ["acxl", "ptoa", "uekr", "qotm"]
# print(find_words(grid))
assert(find_words(grid) == {'quote', 'a', 'tap', 'pat', 'act'})
print('Tests Passed!')
