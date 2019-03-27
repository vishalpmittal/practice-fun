"""
    Tag: string, array, integer

    You are given a string, s, and a list of words, words, that are all of 
    the same length. Find all starting indices of substring(s) in s that 
    is a concatenation of each word in words exactly once and without any 
    intervening characters.

    Example 1:
    Input:
    s = "barfoothefoobarman",
    words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" 
    respectively.
    The output order does not matter, returning [9,0] is fine too.

    Example 2:
    Input:
    s = "wordgoodgoodgoodbestword",
    words = ["word","good","best","word"]
    Output: []
"""

class Solution(object):
    """
        First of all consider s as several series of words with length wl starting 
        at [0, wl-1]. For example "barfoothe" with wl = 3, can be view as ["bar", "foo", "the"] 
        for i=0 and ["arf", "oot"] for i = 1 and ["rfo", "oth"] for i = 2.

        Thus we need to check each of these series and find out the valid index 
        by definition.

        For each series, we just need to check if there exist a range [l, r) where 
        the occurrence or "spectrum" of the words in the range is the same as our 
        given word list's "spectrum". We use dictionary to store the spectrum and 
        maintain it as we loop through s.

        collections.Counter class may save a bit of code on updating the counts 
        of the dictionary. However plain dict wins on the speed.

    """
    def _findSubstring(self, lp, rp, sl, wl, twl, s, wc_map, ans):
        """
            left pointer, right pointer, string length, word length, total word length, 
            string, word count map, answer list
        """
        curr = {}
        while rp + wl <= sl:
            ss = s[rp : rp+wl]   # sub string from rp to rp+wl
            rp += wl
            if ss not in wc_map:
                lp = rp
                curr.clear()
            else:
                curr[ss] = curr[ss] + 1 if ss in curr else 1
                while curr[ss] > wc_map[ss]:
                    curr[s[lp:lp + wl]] -= 1
                    lp += wl
                if rp - lp == twl:
                    ans.append(lp)

    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []
        sl = len(s)    # string length
        wl = len(words[0])    # word length
        twl = len(words) * wl   # total word length
        wc_map = {}             # word count map
        ans = []

        for w in words:
            wc_map[w] = wc_map[w] + 1 if w in wc_map else 1

        for i in xrange(min(wl, sl - twl + 1)):
            print "i: {}, sl: {}, wl: {}, twl: {}, s: {}, wc_map: {}, ans: {}".format(
                i, sl, wl, twl, s, wc_map, ans
            )

            self._findSubstring(i, i, sl, wl, twl, s, wc_map, ans)
        return ans

def test_code():
    obj = Solution()
    assert obj.findSubstring('barfoothefoobarman', ['foo','bar']) == [0, 9]
    print "Tests passed!"

test_code()
