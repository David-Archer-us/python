class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if len(strs) == 0: return prefix
        search_string = min(strs, key=len)
        if search_string == '': return prefix
        for i, letter in enumerate(search_string):
            if all([letter == string[i] for string in strs]):
                prefix += letter
            else: return prefix
        return prefix


instance = Solution()
strs = ["flower","flow","flight"]
print(instance.longestCommonPrefix(strs))