# Given a 32-bit signed integer, 
# reverse digits of an integer.


class Solution():
    # # number approach
    # def reverse(self, x):
    #     input = abs(x)
    #     result = 0
    #     while(input != 0):
    #         result = result * 10 + input % 10
    #         input = input // 10
    #     if (x < 0):
    #         result *= -1
    #     if (result >= -(pow(2, 31)) and result <= (pow(2, 31)- 1)):
    #         return result
    #     return 0

    # string approach
    def reverse(self, x):
        input = str(abs(x))
        input = input[::-1]
        input = int(input)
        if (x < 0):
            input = -input
        if ( input >= -pow(2, 31) and input <= pow(2, 31) - 1):
            return input
        return 0


instance = Solution()
result = instance.reverse(-120)
print(result)

