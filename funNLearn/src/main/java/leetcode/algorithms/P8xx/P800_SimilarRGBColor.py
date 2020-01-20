"""
    Tag: integer, bit

    In the following, every capital letter represents some hexadecimal digit 
    from 0 to f.

    The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  
    For example, "#15c" is shorthand for the color "#1155cc".

    Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" 
    is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

    Given the color "#ABCDEF", return a 7 character color that is most similar 
    to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

    Example 1: Input: color = "#09f166" Output: "#11ee66"
    Explanation:  
    The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
    This is the highest among any shorthand color.

    Note:
    -  color is a string of length 7.
    -  color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
    -  Any answer which has the same (highest) similarity as the best answer will be accepted.
    -  All inputs and outputs should use lowercase letters, and the output is 7 characters.
"""
from typing import List


class Solution:
    def similarRGB(self, color: str) -> str:
        """
            For each possible shorthand-RGB color from "#000" to "#fff", let's find 
            it's similarity to the given color. We'll take the best one.

            To iterate over each shorthand color, we'll use an integer based approach, 
            (though other ones exist.) Each digit in the shorthand "#RGB" could be 
            from 0 to 15. This leads to a color of 
            17 * R * (1 << 16) + 17 * G * (1 << 8) + 17 * B. 
            The reason for the 17 is because a hexadecimal value of 0x22 is equal 
            to 2 * 16 + 2 * 1 which is 2 * (17). The other values for red and green 
            work similarly, just shifted up by 8 or 16 bits.

            To determine the similarity between two colors represented as integers, 
            we'll sum the similarity of each of their colored components separately. 
            For a color like hex1, it has 3 colored components 
            r1 = (hex1 >> 16) % 256, g1 = (hex1 >> 8) % 256, b1 = (hex1 >> 0) % 256. 
            Then, the first addend in the similarity is -(r1 - r2) * (r1 - r2), etc.

            To convert an integer back to a hex string, we'll use String.format. 
            The 06 refers to a zero padded string of length 6, while x refers to 
            lowercase hexadecimal.

            Finally, it should be noted that the answer is always unique. Indeed, 
            for two numbers that differ by 17, every integer is closer to one than 
            the other. For example, with 0 and 17, 8 is closer to 0 and 9 is closer 
            to 17 - there is no number that is tied in closeness.
        """
        def similarity(hex1, hex2):
            r1, g1, b1 = hex1 >> 16, (hex1 >> 8) % 256, hex1 % 256
            r2, g2, b2 = hex2 >> 16, (hex2 >> 8) % 256, hex2 % 256
            return -(r1 - r2)**2 - (g1 - g2)**2 - (b1 - b2)**2

        hex1 = int(color[1:], 16)
        ans = 0
        for r in range(16):
            for g in range(16):
                for b in range(16):
                    hex2 = 17 * r * (1 << 16) + 17 * g * (1 << 8) + 17 * b
                    if similarity(hex1, hex2) > similarity(hex1, ans):
                        ans = hex2

        return '#{:06x}'.format(ans)

    def similarRGB_1(self, color: str) -> str:
        """
            Because color similarity is a sum of the similarity of individual 
            color components, we can treat each colored component separately 
            and combine the answer.

            As in the previous approach, we want the colored component to be 
            the closest to a multiple of 17. We can just round it to the closest 
            such value.
        """
        def f(comp):
            q, r = divmod(int(comp, 16), 17)
            if r > 8:
                q += 1
            return '{:02x}'.format(17 * q)

        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])


assert Solution().similarRGB("#09f166") == "#11ee66"
print('Tests Passed!!')
