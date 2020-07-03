# Determine whether an integer is a palindrome. 
# An integer is a palindrome when 
# it reads the same backward as forward.
# Coud you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0): return False
        input = x
        reverse = 0
        while(input != 0):
            reverse = reverse * 10 + input % 10
            input = input // 10
        return reverse == x


instance = Solution()
result = instance.isPalindrome(-121)
print(result)