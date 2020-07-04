# Given a string containing just the characters 
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # use a stack
        if len(s) == 0: return True
        elif len(s) == 1: return False
        dict = {'(': ')', '{': '}', '[': ']'}
        stack = ''
        for char in s:
            if char in dict: stack += char
            else:
                if stack == '': return False
                else:
                    if char == dict[stack[-1]]: stack = stack[:-1]
                    else: return False
        return not stack


        # # remove the pairs
        # if (len(s)%2 != 0): return False
        # input = s
        # if input.count('()') or input.count('[]') or input.count('{}'): 
        #     input = input.replace('()', '')
        #     input = input.replace('[]', '')
        #     input = input.replace('{}', '')
        # return not input


instance = Solution()
string = "[]]"
print(instance.isValid(string))