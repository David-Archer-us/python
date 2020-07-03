class Solution(object):
    def romanToInt(self, s):
        # iterate the string in one character
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 
                'C':100, 'D':500, 'M':1000}
        previous, current, total = 0, 0, 0
        for char in s:
            current = dict[char]
            if previous == 0: 
                previous = current
            else:
                if previous < current: 
                    total += current - previous
                    previous = 0
                else: 
                    total += previous
                    previous = current
        total += previous
        return total

        # # iterator the string in two and one characters
        # dict = {'I':1, 'V':5, 'X':10, 'L':50, 
        #         'C':100, 'D':500, 'M':1000,
        #         'IV':4, 'IX':9, 'XL':40, 'XC':90,
        #         'CD':400, 'CM':900}
        # input = s
        # total = 0
        # while input:
        #     if input[:2] in dict:
        #         total += dict[input[:2]]
        #         input = input[2:]
        #     else:
        #         total += dict[input[0]]
        #         input = input[1:]
        # return total


        # # treat the exceptions first then iterate the string
        # input = s
        # result = 0
        # if 'IV' in input: 
        #     result += 4
        #     input  = input.replace('IV', '')
        # if 'IX' in input:
        #     result += 9
        #     input = input.replace('IX', '')
        # if 'XL' in input:
        #     result += 40
        #     input = input.replace('XL', '')
        # if 'XC' in input:
        #     result += 90
        #     input = input.replace('XC', '')
        # if 'CD' in input:
        #     result += 400
        #     input = input.replace('CD', '')
        # if 'CM' in input:
        #     result += 900
        #     input = input.replace('CM', '')
        # for char in input:
        #     if char == 'I': result += 1
        #     if char == 'V': result += 5
        #     if char == 'X': result += 10
        #     if char == 'L': result += 50
        #     if char == 'C': result += 100
        #     if char == 'D': result += 500
        #     if char == 'M': result += 1000
        # return result


instance = Solution()
input = 'MCMXCIV'
result = instance.romanToInt(input)
print(result)
