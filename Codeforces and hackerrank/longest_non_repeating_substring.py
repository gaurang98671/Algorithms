class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        last = 0
        max_len = 0
        for i in range(0, len(s)):

            if s[i] not in d:
                d[s[i]] = i
            else:
                max_len = max(max_len, len(d))
                while s[last] != s[i]:
                    del d[s[last]]
                    last += 1

                last += 1
                d[s[i]] = i

        max_len = max(max_len, len(d))
        return max_len





