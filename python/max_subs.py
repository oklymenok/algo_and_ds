#!/bin/env python

# Longest Substring Without Repeating Characters
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def main():

  s = "abcabcbb"
  s = "jbpnbwwd"

  max_subs_length = 0
  tmp_str = []
        
  for i,_ in enumerate(s):
      for j,v in enumerate(s[i:]):
          if v in tmp_str:
              tmp_max = len(tmp_str)
              if tmp_max > max_subs_length:
                  max_subs_length = tmp_max
              tmp_str = []
              break
          else:
              tmp_str.append(v)

  print(max_subs_length)

main()
