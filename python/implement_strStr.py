# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(haystack, needle):

        if haystack == needle:
            return 0

        if len(needle) == 0 or needle == " ":
            return 0

        current_needle_length = 0
        start_pos = 0
        i = 0

        while i < len(haystack):

            if current_needle_length == 0:
                start_pos = i
                for ch in needle:
                    if ch == haystack[i]:
                        current_needle_length += 1
                    else:
                        break

                    # If the next increment will be > than len of haystack
                    if i + 1 >= len(haystack):
                        if current_needle_length == len(needle):
                            return start_pos
                        else:
                            return -1
                    else:
                        i += 1

                if current_needle_length == len(needle):
                    return start_pos

                current_needle_length = 0
                i = start_pos
            i += 1

        return -1

# "aaa"
# "aaa"

haystack = "mississippi"
needle = "issip"
r = Solution.strStr(haystack, needle)
print(r)