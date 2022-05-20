class Solution:
    def longestCommonPrefix(strs):
        
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        shortest_word = min(strs, key=len)
        prefix_len = []
        
        
        
        for word in strs:
            cur_match_len = 0
            for i,char in enumerate(shortest_word):
                if char == word[i]:
                    cur_match_len += 1
                else:
                    prefix_len.append(cur_match_len)
                    break
            prefix_len.append(cur_match_len)
                    
        if len(prefix_len) == 0:
            return ""
        max_prefix_len = min(prefix_len)
        if max_prefix_len > 0:
            return shortest_word[:max_prefix_len]
        return ""

#data = ["ab", "a"]
data = ["flower","flow","flight"]
r = Solution.longestCommonPrefix(data)
print(r)
