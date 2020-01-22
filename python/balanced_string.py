from collections import Counter

# THE PROBLEM (Leetcode: 1234):
# You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
# A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
# Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
# Return 0 if the string is already balanced.

# Example 1:
#
# Input: s = "QWER"
# Output: 0
# Explanation: s is already balanced.
#
# Example 2:
#
# Input: s = "QQWE"
# Output: 1
# Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
#
# Example 3:
#
# Input: s = "QQQW"
# Output: 2
# Explanation: We can replace the first "QQ" to "ER".
#
# Example 4:
#
# Input: s = "QQQQ"
# Output: 3
# Explanation: We can replace the last 3 'Q' to make s = "QWER".
#
#
#
# Constraints:
#
#     1 <= s.length <= 10^5
#     s.length is a multiple of 4
#     s contains only 'Q', 'W', 'E' and 'R'.

# Super slow solution, but well commented and explains sliding window approach
def min_substr(s):

    occurance_required = int(len(s)/4)
    char_counter = Counter(s)

    # Handling base case for 'QWER' which is balanced
    if sum(char_counter.values()) == 4 and len(char_counter.keys()) == 4:
        return 0

    # Find excess. For example. We in 'QQQWEERR' we have an excess of 1 'Q'
    char_excess = {}
    for char, count in char_counter.items():
        if (count - occurance_required) > 0:
            char_excess[char] = count - occurance_required

    # Now start from minimal subtr and try to find it. Increase its length every
    # by 1 if we did not find substr that contains excess of necessary characters

    win_size_increment = 0
    start_pos = 0
    end_pos = sum(char_excess.values())

    # First loop that increases window size. We search until window is smaller than
    # the original string
    while s[start_pos:end_pos] != s:
        start_pos = 0
        end_pos = sum(char_excess.values()) + win_size_increment

        # Second loop shifts the window and checks if substring contains required
        # or more number of characters that are in excess list
        while end_pos <= len(s):

            # Current window members
            win_subst_members = Counter(s[start_pos:end_pos])

            if all([count <= win_subst_members.get(char, 0) for char, count in char_excess.items()]):
                return len(s[start_pos:end_pos])
            else:
                start_pos += 1
                end_pos += 1
        win_size_increment += 1

    return len(s)

test_cases = {
    "QWER": 0,
    "WQWRQQQW": 3,
    "QQWW": 2,
    "WWEQERQWQWWRWWERQWEQ": 4,
    "EQWEEEWERRWERQQQWWQEQWEEWQRWQWWWQWRWEWERWQEWWQWWQRRQWQERWWQRERRRRRWQEQRERRWRREEEERRWERQRQEWREQREWWEWRRRERWRRWEQWQQRRWQEREEEERWQWEWQEWRWREWQEREQWQEQWRQQQWRWWRWERWQWWQQREWREEWRWWQRWQRWWQWWREWWWEWQRWRRWQEWRRRWWQRRQREQRWRRQWREQWEQRWQRWQRWERRREEREEQQEREREWQQWRWEWEQQRWEWEQWEEQEEERWWWEQRRRWRQWWQQEQRWRWRWEQRRQRQRQWWWEQWERWEQRWQRERWQQQWWWQWRWEREWRQWQWERRQQWRQWRWQQQEEQREQWRWWEQRWWWEEERQWQWEWRQQRWQWEQQEWEWRQWWERERQREWWEEREQRRWQRRRWQEEWEWQEEEQRQQEWREQWQWRRWREQQQEEEWWRQEEEWQQEQEQWWREEWRQQQRQQEERQQQEEQWERRQEEQQRQQQWWEQEEQWRQWEQWEEQQEEQQEERQEEWQEEEWQRERRERQRQQQQWRQRRQQWQEEWRRQEWQWREWERWQRQQWEEERREQEEQWQQRWERWRWEEQWEREREWRWREEWRRRQEQQERRRERQRQWRWWREQQWWEQQWQWRRWEQRWEQQEQWWWQWWEWWEEEWEWRQWQWWQQQQEWRQEQWWRWWEQRRRWREREWRQQERQRQEQWWQQWRQRRQRWRQEEEWRRQREWRRERRQEEREERWEQQQWEWWEERWQWQQWWEQWWQWERRRWQWEEEEQEEWQRRWRWEEEWEWRREWWEQQERRQWQEWQQQRWEWRQEQWREWEWEEWWWWWWWWEQRWRRQQEEEERQEWQQEQQEEEWWRWRQQQQWRREEWRWWWQRWRWRWQWWEREQQEEEWREERQEWEERQWQREEQRQWEQEREQWWEWEEWREREWRQQWREEEEQRRWRWRQRRRWRQQQRRQQRQEWEEQQEREWQEEWEWWEQRRQWRQRQQREREQRWWQEEERREWRREWRRRQQQRQEQEWQWEEQQERQRRRWRRWWEEQRWQQQQQQWREWEWWRQREWREQRRQEQEERRQERWEEQRWWQRWQRWWERQEWEQERWRWQRQEEQEQEWWQWWRREEWEWWRRQEQQWEERWEWWWQEWWRRWRWQEERQRQWEQQEWWRRRRWQEWQQQQWWEEE": 16
}

for test_string, result in test_cases.items():
    assert min_substr(test_string) == result