"""
    tag: recursive, db, string

    give two strings find the edit distance between them.
"""


def edit_dist_recursive(s1: str, s2: str) -> int:
    def edit_dist(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return m + n

        if s1[m - 1] == s2[n - 1]:
            return edit_dist(m - 1, n - 1)

        return 1 + min(
            edit_dist(m - 1, n),  # remove
            edit_dist(m, n - 1),  # append
            edit_dist(m - 1, n - 1),  # replace
        )

    return edit_dist(len(s1), len(s2))


def edit_dist_dp(s1: str, s2: str, m: int, n: int) -> int:
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i - 1][j - 1] = dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j - 1],  # Insert
                    dp[i - 1][j],  # Remove
                    dp[i - 1][j - 1],  # Replace
                )
    
    for i in dp:
        print(i)
    return dp[m][n]


print(edit_dist_recursive("saturday", "sunday"))
print(edit_dist_dp("saturday", "sunday", len("saturday"), len("sunday")))
print(edit_dist_dp("top", "ton", len("top"), len("ton")))
