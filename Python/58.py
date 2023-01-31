class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        word = s.split(" ")

        for i in range(len(word)-1, -1, -1):
            if len(a[i]) > 0:
                return len(a[i])

        return 0