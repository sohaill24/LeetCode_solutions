class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = set()
        left = 0
        max_lenght = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            max_lenght = max(max_lenght, right - left + 1)

        return max_lenght    


