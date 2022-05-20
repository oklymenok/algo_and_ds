class Solution:
    def romanToInt(self, s: str) -> int:
        # Parse individual numbers

        # I 1
        # V 5
        # X 10
        # L 50
        # C 100
        # D 500
        # M 1000

        roma_nums = {
          'V': 5,
          'L': 50,
          'D': 500,
        }

        end = len(s)
        i = 0
        dec_nums = []
        
        if end == 0:
            return 0
        
        while i < end:

            if s[i] == 'I':
                if i+1 < end:
                    if s[i+1] == 'V':
                        # Jump to the next dec number
                        i = i + 2
                        dec_nums.append(4)
                        continue
                    elif s[i+1] == 'X':
                        # Jump to the next dec number
                        i = i + 2
                        dec_nums.append(9)
                        continue
                    elif s[i+1] == 'I':
                        i = i + 2
                        dec_nums.append(2)
                        continue
                else:
                    dec_nums.append(1)
                    break

            # Parse X        
            if s[i] == 'X':
                if i+1 < end:
                    if s[i+1] == 'L':
                        i = i + 2
                        dec_nums.append(40)
                        continue
                    elif s[i+1] == 'C':
                        i = i + 2
                        dec_nums.append(90)
                        continue
                    elif s[i+1] == 'X':
                        i = i + 2
                        dec_nums.append(20)
                        continue        
                else:
                    dec_nums.append(10)
                    break
                dec_nums.append(10)
                i = i + 1
                continue

            # Parse C
            if s[i] == "C":
                if i + 1 < end:
                    if s[i+1] == "D":
                        i = i + 2
                        dec_nums.append(400)
                        continue
                    elif s[i+1] == "M":
                        i = i + 2
                        dec_nums.append(900)
                        continue
                    elif s[i+1] == "C":
                        i = i + 2
                        dec_nums.append(200)
                        continue
                else:
                    dec_nums.append(100)
                    break
                dec_nums.append(100)
                i = i + 1
                continue

            # Parse M
            if s[i] == "M":
                if i + 1 < end:
                    if s[i+1] == "M":
                        dec_nums.append(2000)
                        i = i + 2
                        continue
                    else:
                        dec_nums.append(1000)
                        i = i + 1
                        continue
                else:
                    dec_nums.append(1000)
                    break

            # Parse 5, 50, 500
            r_num = roma_nums.get(s[i]) 
            if r_num is not None:
                dec_nums.append(r_num)
                i = i + 1

        return sum(dec_nums)    

s = Solution()
# r = s.romanToInt('III')
# r = s.romanToInt('IV')
# r = s.romanToInt('IX')
# r = s.romanToInt('XII')
# r = s.romanToInt('XIII')
# r = s.romanToInt('XVII')
# r = s.romanToInt('LVIII')
# r = s.romanToInt('MCMXCIV')
r = s.romanToInt('MMMDCCLXV')

print(r)
