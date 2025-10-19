class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        st = 0
        end = len(s)-1
        while st < end:
            s[st], s[end] = s[end], s[st]
            st += 1
            end -= 1
        